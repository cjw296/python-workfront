"""
Foo bar

asda as da  asd a das ad
"""
import json

import os

from os.path import expanduser

import re
from logging import getLogger
from os import mkdir, path

from workfront.script import script_setup, parser_with_standard_args

logger = getLogger(__name__)

TARGET_ROOT = path.join(path.split(__file__)[0], 'versions')

CLASS_NAME_OVERRIDE = dict(
    OPTASK='Issue'
)

INIT_TEMPLATE = b"""\
from .generated import api
"""

HEADER = """\
# generated from {url}/metadata
from ...meta import APIVersion, Object, Field, Reference, Collection

api = APIVersion('{version}')
"""

CLASS_HEADER_TEMPLATE = """

class {class_name}(Object):
    code = '{obj_code}'
"""

CLASS_MEMBER_TEMPLATE = """\
    {python_name} = {type}('{workfront_name}')
"""

CLASS_FOOTER_TEMPLATE = """\

api.register({class_name})
"""

NAME_RE = re.compile('([a-z]|^)([A-Z]+)')


def name_subber(match):
    if match.group(1):
        start = match.group(1)+'_'
    else:
        start = ''
    return start+match.group(2).lower()


def dehump(name):
    """SomeThing -> some_thing"""
    return NAME_RE.sub(name_subber, name).lower()


def prepare_target(session):
    target = path.join(TARGET_ROOT, session.api.version.replace('.', ''))
    if not path.exists(target):
        mkdir(target)
    init = path.join(target, '__init__.py')
    if not path.exists(init):
        with open(init, 'wb') as output:
            output.write(INIT_TEMPLATE)
    return path.join(target, 'generated.py')


def get_with_cache(session, cache, path):
    if cache:
        cache_path = os.path.join(
            cache,
            session.api.version+path.replace('/', '_')+'.json'
        )
        if os.path.exists(cache_path):
            with open(cache_path) as source:
                return json.load(source)

    result = session.get(path)

    if cache:
        with open(cache_path, 'w') as dest:
            json.dump(result, dest)

    return result


def decorated_object_types(session, cache):
    for name, object_type in sorted(
        get_with_cache(session, cache, '/metadata')['objects'].items()
    ):
        code =  object_type['objCode']
        # this works around the broken urls Workfront serve for the
        # 'unsupported' api:
        detail = get_with_cache(session, cache, '/'+code.lower()+'/metadata')
        class_name = CLASS_NAME_OVERRIDE.get(code, detail['name'])
        yield class_name, code, detail


class ClassWriter(object):

    name_overrides = {
        ('Approval', 'url'): 'url_',
        ('Work', 'url'): 'url_',
    }

    def __init__(self, class_name, code, output):
        self.class_name = class_name
        self.code = code
        self.output = output
        self.members = {}

    def write_header(self):
        self.output.write(CLASS_HEADER_TEMPLATE.format(
            class_name=self.class_name,
            obj_code=self.code
        ))

    def write_members(self, type_, members):
        for workfront_name in sorted(members):
            python_name = self.name_overrides.get(
                (self.class_name, workfront_name),
                dehump(workfront_name)
            )
            if python_name in self.members:
                logger.error(
                    '{} has duplicate member name: '
                    '{!r}, first from {!r}, current from {!r}'.format(
                        self.class_name,
                        python_name, self.members[python_name], workfront_name
                    ))
            self.members[python_name] = workfront_name
            self.output.write(CLASS_MEMBER_TEMPLATE.format(
                type=type_,
                python_name=python_name,
                workfront_name=workfront_name
            ))

    def write_footer(self):
        self.output.write(CLASS_FOOTER_TEMPLATE.format(
            class_name=self.class_name,
        ))


def generate(session, cache, output_path):
    with open(output_path, 'w') as output:

        output.write(HEADER.format(url=session.url,
                                   version=session.api.version))

        for class_name, code, details in sorted(
            decorated_object_types(session, cache)
        ):

            writer = ClassWriter(class_name, code, output)
            writer.write_header()
            writer.write_members('Field',
                                 (name for name in details['fields']
                                  if name != 'ID'))
            writer.write_members('Reference', details['references'])
            writer.write_members('Collection', details['collections'])
            writer.write_footer()


def main():
    parser = parser_with_standard_args('generate', __doc__)
    parser.add_argument('--cache',
                        help='directory in which to cache metadata downloads',
                        type=expanduser)
    args, session = script_setup(parser)
    path = prepare_target(session)
    generate(session, args.cache, path)


if __name__ == '__main__':  # pragma: no cover
    main()
