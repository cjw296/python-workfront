python-workfront documentation
==============================

This is a Python client library for accessing the `Workfront`__ REST api.

__ https://www.workfront.com

Quickstart
----------

Install the package::

    $ pip install python-workfront

Generate an API key::

    $ python -m workfront.get_api_key --domain ${your_domain}
    username: your_user
    Password:
    Your API key is: '...'

.. note::

  If you have SAML authentication enabled, you may well need to disable it for
  for the specified user in order to obtain an API key. Once you have an API
  key, you can re-enable SAML authentication.

Make a session:

.. code-block:: python

    from workfront import Session
    session = Session('your domain', api_key='...')
    api = session.api

Search for a project:

.. code-block:: python

    project = session.search(api.Project,
                             name='my project name',
                             name_Mod='cicontains')[0]

Create an issue in that project:

.. code-block:: python

    issue = api.Issue(session,
                      name='a test issue',
                      description='some text here',
                      project_id=project.id)
    issue.save()

Add a comment to the issue just created:

.. code-block:: python

    issue.add_comment('a comment')

Detailed Documentation
----------------------

.. toctree::
   :maxdepth: 3

   use.rst
   api.rst
   development.rst
   changes.rst
   license.rst

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

