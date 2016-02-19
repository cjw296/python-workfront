Usage
=====

This documentation explains how to use the ``python-workfront`` package, but you
should consult the `Workfront API documentation`__ for details on the API
itself.

__ https://developers.workfront.com/api-docs/

Creating a :class:`~workfront.Session`
--------------------------------------

To interact with Workfront, a :class:`~workfront.Session` is needed, and for
this session to be useful, it needs to be authenticated using either an API key
or a username and password.

When using a username and password, you use the :meth:`~workfront.Session.login`
method to log in and obtain a session identifier:

>>> from workfront import Session
>>> session = Session('yourdomain')
>>> session.login('youruser', 'yourpassword')
>>> session.session_id
u'xyz123'

When using this authentication method, the UUID of the logged in user is
available on the session:

>>> session.user_id
u'abc456'

This can be used to load up your :class:`~workfront.versions.unsupported.User`
object, amongst other uses.

The session identifier is then passed with all subsequent requests issued by
that session until the :meth:`~workfront.Session.logout` method is called:

>>> session.logout()
>>> session.session_id is None
True
>>> session.user_id is None
True

When using an API key for authentication, you will first have to obtain an API
key. This can be done as described in the :ref:`quickstart` or by calling
:meth:`~workfront.Session.get_api_key` directly. Once you have an API key,
you can pass it during :class:`~workfront.Session` instantiation, it will then
be used for all requests issued by that session:

>>> session = Session('yourdomain', api_key='yourapikey')

To instantiate a :class:`~workfront.Session`, you only need to provide your
Workfront domain name, which is the bit before the first dot in the url you use
to access workfront. In this case, the latest version of the Workfront API,
known as ``unsupported``, will be used. If you wish to use a different version,
this can be specified:

>>> session = Session('yourdomain', api_version='v4.0')

If you wish to use the Workfront Sandbox instead, you can create a session using
a different url template:

>>> from workfront.session import SANDBOX_TEMPLATE
>>> session = Session('yourdomain', url_template=SANDBOX_TEMPLATE)

When instantiating a :class:`~workfront.Session`, you can also independently
specify the ``protocol`` or, in extremely circumstances, provide your own
``url_template`` that contains the exact base url for the API you wish to use.

Finding objects
---------------

Once you have a :class:`~workfront.Session`, you will want to obtain objects
from Workfront. This can be done using either :meth:`~workfront.Session.search`
or :meth:`~workfront.Session.load`.

Objects each have a type that is mapped to a concrete Python class of the same
name as used in the `API Explorer`_. These Python classes all subclass
:class:`~workfront.meta.Object` and can either be imported
from the API version module directly, which works better if you are using an
IDE, or obtained from the :class:`~workfront.Session.api` attribute of the
session, which works better if your code has to work with multiple version of
the workfront API. For example:

>>> from workfront import Session
>>> from workfront.versions.v40 import Task
>>> session = Session('yourdomain', api_version='v4.0')
>>> api = session.api
>>> api.Task is Task
True

To search for objects, you pass a particular :class:`~workfront.meta.Object`
type and a list of search parameters as described in the `search`__
documentation:

__ https://developers.workfront.com/api-docs/#Search

>>> results = session.search(api.Project,
...                          name='project name',
...                          name_Mod='cicontains')

When passing field names as search parameters, any of the Workfront name, the
Python name, or the :class:`~workfront.meta.Field` descriptor itself may be
used.

The search results will be a list of instances of the passed type matching the provided
search criteria:

>>> results[0]
<Project: ID=u'def789', name=u'The Project Name'>

By default, each object will be loaded with its standard set of fields. If you
need more fields, or want to load nested sub-objects, the ``fields`` parameter
can be passed:

>>> project = results[0]
>>> tasks = session.search(api.Task,
...                        project_id=project.id,
...                        status='CLS', status_Mod='ne',
...                        fields=['resolvables:*'])
>>> tasks
[<Task: ID=u'ghi101', name=u'Something to do', resolvables=[{...}]>]
>>> tasks[0].resolvables
(<Issue: ID=u'jkl112', objCode=u'OPTASK'>,)

If you know the UUID of an object, such as that for a project that you may
store in a config file, you can skip the search step and load the object
directly:

>>> session.load(api.Project, project.id)
<Project: ID=u'def789', name=u'The Project Name'>

You can load multiple objects in one go by passing a sequence of UUIDs. Even if
this sequence only contains one element, a sequence of objects will still be
returned:

>>> session.load(api.Project, [project.id])
[<Project: ID=u'def789', name=u'The Project Name'>]

Working with objects
--------------------

In the previous section we saw how to load objects from Workfront. To create
new content in Workfront, you instantiate the object, passing in a
:class:`~workfront.Session` and then save it:

>>> issue = api.Issue(session,
...                   name='something bad', description='details',
...                   project_id=project.id)
>>> issue.save()

To make changes to an object, set the attributes you want to change and then
use the save method again:

>>> issue.description += '\nautomatically appended text.'
>>> issue.save()

When saving changes to an existing object, only fields that have actually been
modified will be submitted back to Workfront.

Objects loaded from Workfront will, by default, only have a subset of their
fields loaded. If you access a field that has not been loaded, a
:class:`~workfront.meta.FieldNotLoaded` exception will be raised:

>>> issue.previous_status
Traceback (most recent call last):
 ...
FieldNotLoaded: previousStatus

Further fields can be retrieved from Workfront using
:class:`~workfront.meta.Object.load`:

>>> issue.load('previous_status')
>>> issue.previous_status
u'CLS'

To delete an object, call its :class:`~workfront.meta.Object.delete` method:

>>> issue.delete()

Any references or collections are reflected into the Python model using the
:class:`~workfront.meta.Reference` and :class:`~workfront.meta.Collection`
descriptors. Unlike plain fields, accessing these will make the request to
Workfront to load the necessary objects rather than raising a
:class:`~workfront.meta.FieldNotLoaded` exception.

References will return the referenced object or ``None``, if there is no
object referenced:

>>> issue.project
<Project: ID=u'def789', name=u'The Project Name', objCode=u'PROJ'>

References cannot be altered or set directly, instead
set the matching ``_id`` fields:

>>> issue.project_id = 'ghj1234'
>>> issue.save()

.. note::

  When you have set an ``_id`` field in this fashion, the referenced object
  will be stale. If you need it, you should re-load it:

  >>> issue.load('project')
  >>> issue.project
  <Project: ID=u'ghj1234', name=u'Another Project', objCode=u'PROJ'>

Collections will always return an immutable sequence of objects in the
collection:

>>> issue.resolvables
(<Task: ID=u'tsk345', objCode=u'TASK'>,)

This will be empty if there is no content in the Workfront collection.

Collections cannot be modified.

Workfront actions are made available as methods on objects:

>>> issue.mark_done(status='CLS')

If they return data, it will be returned from the Python method.

The ``python-workfront`` package also adds a few convenience methods to some
objects. Please consult the :doc:`api`.

Low-level requests
------------------

In the event that the existing object reflection, descriptors and methods do not
cover your use case, :class:`~workfront.Session` provides lower level methods
to perform requests in the form of :class:`~workfront.Session.get`,
:class:`~workfront.Session.post`, :class:`~workfront.Session.put` and
:class:`~workfront.Session.delete`.

They all take a ``path`` and an optional dictionary of parameters to pass as part
of the request. Requests will include any authentication set up on the session.
The methods return any data provided in the response from Workfront:

>>> session = Session('yourdomain', api_version='v4.0', api_key='my key')
>>> session.post('/something/New', params=dict(just='in case'))
[u'result', 42]

The lowest level way of issuing a request to Workfront is to use
:class:`~workfront.Session.request` directly. This will still include any
authentication set up on the :class:`~workfront.Session`, but gives you
additional control over the ``method`` used:

>>> session.request(method='TEST', path='/foo', params=dict(what='now'))
u'some data'

.. _API Explorer: https://developers.workfront.com/api-docs/api-explorer/
