import logging
import ssl
from argparse import (
    ArgumentParser,
    ArgumentDefaultsHelpFormatter,
    RawDescriptionHelpFormatter
)

from workfront import Session


class SaneFormatter(RawDescriptionHelpFormatter, ArgumentDefaultsHelpFormatter):
    pass


def parser_with_standard_args(name, description):
    parser = ArgumentParser(
        prog='python -m workfront.'+name,
        description=description,
        formatter_class=SaneFormatter,
    )
    parser.add_argument('--unsafe-certs', action='store_true',
                        help='use an unverified ssl context in case of '
                             'company imposed man-in-the-middle '
                             'situations')
    parser.add_argument('--log-level', default=logging.WARNING, type=int,
                        metavar='LEVEL',
                        help='pass a lower number to see more logging')

    group = parser.add_argument_group('API options')
    group.add_argument('--protocol', default='https',
                       help='url protocol')
    group.add_argument('--domain', default='api-cl01',
                       help='the bit before the dot of your On Demand url.')
    group.add_argument('--version', default='unsupported',
                       help='api version to use')

    group = parser.add_argument_group('Override API url')
    group.add_argument('--url',
                       help='full base url to Workfront API. '
                            'Should end in an API version string and overrides'
                            ' --protocol, --domain and --version')

    return parser


def script_setup(parser):
    args = parser.parse_args()

    if any(getattr(args, name)!= parser.get_default(name)
            for name in ('protocol', 'domain', 'version')) and args.url:
        parser.error('--url can not be used with '
                     '--protocol, --domain or --version')

    logging.basicConfig(level=args.log_level)

    if args.unsafe_certs:
        ssl_context = ssl._create_unverified_context()
    else:
        ssl_context = None

    if args.url:
        session = Session(None,
                          url_template=args.url,
                          ssl_context=ssl_context)
    else:
        session = Session(protocol=args.protocol,
                          domain=args.domain,
                          api_version=args.version,
                          ssl_context=ssl_context)

    return args, session
