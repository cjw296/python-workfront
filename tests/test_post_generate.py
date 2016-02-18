# NB: python -m workfront.generate MUST be run for all API versions before
#     these tests will be meaningful!
import re
from testfixtures import Comparison as C, Replacer, compare, Replace
from unittest import TestCase

from tests.helpers import MockOpen
from workfront.generate import ClassWriter
from workfront.session import Session


class TestV40Specials(TestCase):

    api_version = 'v4.0'

    def setUp(self):
        self.replace = Replacer()
        self.addCleanup(self.replace.restore)
        self.server = MockOpen(
            'https://test.attask-ondemand.com/attask/api/'+self.api_version
        )
        self.replace('workfront.six.moves.urllib.request.urlopen', self.server)
        self.session = Session('test', api_version=self.api_version)
        self.api = self.session.api

    def test_issue_add_comment(self):
        obj = self.api.Issue(self.session, ID='xxx')
        self.server.add(
            url='/NOTE',
            params='method=POST&noteObjCode=OPTASK&noteText=some text&objID=xxx',
            response='{"data": {"objCode": "NOTE", "ID":"yyy"}}'
        )
        comment = obj.add_comment('some text')
        compare(comment, expected=C(
            self.api.Note,
            fields={
                u'objCode': u'NOTE',
                u'ID': u'yyy',
                'noteText': 'some text',
                'noteObjCode': 'OPTASK',
                'objID': 'xxx',
            },
            strict=False))

    def test_note_add_comment(self):
        obj = self.api.Note(self.session,
                            ID='xxx',
                            noteObjCode='NCDE',
                            objID='zzz')
        self.server.add(
            url='/NOTE',
            params='method=POST&noteObjCode=NCDE&noteText=some text'
                   '&objID=zzz&parentNoteID=xxx',
            response='{"data": {"objCode": "NOTE", "ID":"yyy"}}'
        )
        comment = obj.add_comment('some text')
        compare(comment, expected=C(
            self.api.Note,
            fields={
                u'objCode': u'NOTE',
                u'ID': u'yyy',
                'noteText': 'some text',
                'noteObjCode': 'NCDE',
                'objID': 'zzz',
                'parentNoteID': 'xxx',
            },
            strict=False))

    def test_task_add_comment(self):
        obj = self.api.Task(self.session, ID='xxx')
        self.server.add(
            url='/NOTE',
            params='method=POST&noteObjCode=TASK&noteText=some text&objID=xxx',
            response='{"data": {"objCode": "NOTE", "ID":"yyy"}}'
        )
        comment = obj.add_comment('some text')
        compare(comment, expected=C(
            self.api.Note,
            fields={
                u'objCode': u'NOTE',
                u'ID': u'yyy',
                'noteText': 'some text',
                'noteObjCode': 'TASK',
                'objID': 'xxx',
            },
            strict=False))

    def test_issue_convert_to_task(self):
        obj = self.api.Issue(self.session,
                             ID='xxx',
                             name='test issue',
                             description='a test',
                             entered_by_id='zzz')
        self.server.add(
            url='/OPTASK/xxx/convertToTask',
            params='method=PUT&updates={"task": {"description": "a test", '
                   '"enteredByID": "zzz", "name": "test issue"}, "options": '
                   '["preserveIssue", "preservePrimaryContact", '
                   '"preserveUpdates"]}',
            response='{"data": {"result": "yyy"}}'
        )
        task = obj.convert_to_task()
        compare(task, expected=C(
            self.api.Task,
            fields={u'ID': u'yyy'},
            strict=False))

    def test_update_obj(self):
        obj = self.api.Update(self.session,
                              ID='xxx',
                              update_obj_id='zzz',
                              update_obj_code='TASK')
        task = obj.update_obj
        compare(task, expected=C(
            self.api.Task,
            fields={u'ID': u'zzz', u"objCode": u"TASK"},
            strict=False))

    def test_action_full(self):
        obj = self.api.Schedule(self.session, ID='xxx')
        self.server.add(
            url='/SCHED/xxx/getNextCompletionDate',
            params='method=PUT&date=2001-01-01&costInMinutes=24',
            response='{"data": {"result": "yyy"}}'
        )
        result = obj.get_next_completion_date('2001-01-01', 24)
        compare(result, expected='yyy')

    def test_action_default_args(self):
        obj = self.api.Schedule(self.session, ID='xxx')
        self.server.add(
            url='/SCHED/xxx/getNextCompletionDate',
            params='method=PUT',
            response='{"data": {"result": "yyy"}}'
        )
        result = obj.get_next_completion_date()
        compare(result, expected='yyy')

    def test_action_no_args_or_return(self):
        obj = self.api.Project(self.session, ID='xxx')
        self.server.add(
            url='/PROJ/xxx/recallApproval',
            params='method=PUT',
            response='{"data": {}}'
        )
        result = obj.recall_approval()
        compare(result, expected=None)


class TestVunsupportedMixins(TestV40Specials):

    api_version = 'unsupported'


class TestGeneratedMethod(TestCase):

    def methods_to_test(self):
        for api in Session.version_registry.values():
            for type_ in api.by_code.values():
                for name, obj in type_.__dict__.items():
                    key = (type_.__name__, name)
                    not_override = key not in ClassWriter.method_overrides
                    if callable(obj) and not_override:
                        yield api.version, type_, name

    def test_generated_methods(self):
        for api_version, type_, name in self.methods_to_test():
            session = Session('test', api_version=api_version)
            obj = type_(session, ID='xxx')
            method = getattr(obj, name)
            workfront_name = re.search('``(.+?)``', method.__doc__).group(1)

            server = MockOpen(
                'https://test.attask-ondemand.com/attask/api/'+api_version
            )
            server.add(
                url='/{}/xxx/{}'.format(type_.code, workfront_name),
                params='method=PUT',
                response='{"data": {"result": null}}'
            )

            with Replace('workfront.six.moves.urllib.request.urlopen', server):
                method()


