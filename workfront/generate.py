"""
Usage: python -m workfront.generate --help
"""
from argparse import ArgumentParser
import logging
from os import path
import ssl
import re

from workfront import Session

name_re = re.compile('([a-z]|^)([A-Z]+)')

def name_subber(match):
    if match.group(1):
        start = match.group(1)+'_'
    else:
        start = ''
    return start+match.group(2).lower()

def dehump(name):
    "SomeThing -> some_thing"
    return name_re.sub(name_subber, name).lower()


def decorated_object_types(session):
    for object_type in session.get('/metadata')['objects'].values():
        class_name = class_name_override.get(object_type['objCode'], object_type['name'])
        yield class_name, object_type


def generate(protocol, domain, version, unsafe_certs, output_path):
    if unsafe_certs:
        ssl_context = ssl._create_unverified_context()
    else:
        ssl_context = None
    session = Session(protocol=protocol, domain=domain, api_version=version,
                      ssl_context=ssl_context)

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


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('--domain', default='api-cl01')
    parser.add_argument('--protocol', default='https')
    parser.add_argument('--version', default='v4.0')

    parser.add_argument('--output-path',
                        default=path.join(path.split(__file__)[0], 'generated_objects.py'))

    parser.add_argument('--unsafe-certs', action='store_true')
    parser.add_argument('--log-level', default=logging.WARNING, type=int)
    return parser.parse_args()


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


if __name__=='__main__':
    args = parse_args()
    logging.basicConfig(level=args.log_level)
    generate(args.protocol, args.domain, args.version, args.unsafe_certs, args.output_path)
