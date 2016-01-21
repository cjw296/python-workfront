"""
Prompt for a username and password and then request an API key,

eg: python -m workfront.get_api_key --domain mycompany

NB: Single Sign On must be disabled for the user requesting the key!
"""
from __future__ import print_function

from .six.moves import input
import getpass

from workfront.script import script_setup, parser_with_standard_args


def get_api_key(session):
    username = input('username: ')
    password = getpass.getpass()
    key = session.get_api_key(username, password)
    print('Your API key is:', repr(key))


def main():
    parser = parser_with_standard_args('get_api_key', __doc__)
    args, session = script_setup(parser)
    get_api_key(session)


if __name__ == '__main__':  # pragma: no cover
    main()
