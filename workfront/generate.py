"""
Foo bar

asda as da  asd a das ad
"""

import re
from os import mkdir, path

from workfront.script import script_setup, parser_with_standard_args

name_re = re.compile('([a-z]|^)([A-Z]+)')
TARGET_ROOT = path.join(path.split(__file__)[0], 'versions')

INIT_TEMPLATE = """\
from .generated import api
"""



def name_subber(match):
    if match.group(1):
        start = match.group(1)+'_'
    else:
        start = ''
    return start+match.group(2).lower()


def dehump(name):
    "SomeThing -> some_thing"
    return name_re.sub(name_subber, name).lower()


def prepare_target(session):
    target = path.join(TARGET_ROOT, session.api.version)
    if not path.exists(target):
        mkdir(target)
    init = path.join(target, '__init__.py')
    if not path.exists(init):
        with open(init, 'w') as output:
            output.write(INIT_TEMPLATE)
    return path.join(target, 'generated.py')


def decorated_object_types(session):
    for object_type in session.get('/metadata')['objects'].values():
        class_name = class_name_override.get(object_type['objCode'], object_type['name'])
        yield class_name, object_type


def generate(session, output_path):
    with open(output_path, 'w') as output:

        output.write(header.format(url=session.url))

        for class_name, object_type in sorted(decorated_object_types(session)):

            output.write(class_template.format(
                class_name=class_name,
                obj_code=object_type['objCode']
            ))

            type_detail = session.get(object_type['url'])

            for workfront_name in sorted(type_detail['fields']):

                if workfront_name == 'ID':
                    continue

                output.write(field_template.format(
                    python_name=dehump(workfront_name),
                    workfront_name=workfront_name
                ))

            for workfront_name, reference_type in sorted(
                    type_detail['references'].items()
            ):
                output.write(reference_template.format(
                    python_name=dehump(workfront_name),
                    workfront_name=workfront_name,
                ))

            for workfront_name, reference_type in sorted(
                    type_detail['collections'].items()
            ):
                output.write(collection_template.format(
                    python_name=dehump(workfront_name),
                    workfront_name=workfront_name,
                ))


def main():
    parser = parser_with_standard_args('generate', __doc__)
    parser.add_argument('--output-path',
                        default=path.join(path.split(__file__)[0],
                                          'generated_objects.py'))

    args, session = script_setup(parser)

    generate(args.output_path)


header = """\
# generated from {url}/metadata
from .meta import Object, Field, Reference, Collection
"""


class_template = """

class {class_name}(Object):
    code = "{obj_code}"
"""


field_template = """\
    {python_name} = Field('{workfront_name}')
"""


reference_template = """\
    {python_name} = Reference('{workfront_name}')
"""


collection_template = """\
    {python_name} = Collection('{workfront_name}')
"""


class_name_override = dict(
    OPTASK='Issue'
)


if __name__ == '__main__':  # pragma: no cover
    main()
