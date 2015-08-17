"""
Usage: python -m workfront.generate --help
"""
from argparse import ArgumentParser
import logging
from os import path
import ssl

from workfront import Session


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
# generated from {url}
from .meta import Object
"""


class_template = """

class {class_name}(Object):
    code = "{obj_code}"
"""


class_name_override = dict(
    OPTASK='Issue'
)


if __name__=='__main__':
    args = parse_args()
    logging.basicConfig(level=args.log_level)
    generate(args.protocol, args.domain, args.version, args.unsafe_certs, args.output_path)
