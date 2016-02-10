from unittest import TestCase

from testfixtures import Comparison as C, Replacer, compare

from tests.helpers import MockOpenHelper, MockOpen
from workfront.session import Session


class TestV40Mixins(TestCase):

    api_version = 'v4.0'

    def setUp(self):
        self.replace = Replacer()
        self.addCleanup(self.replace.restore)
        self.server = MockOpen(
            'https://test.attask-ondemand.com/attask/api/'+self.api_version
        )
        self.replace('urllib2.urlopen', self.server)
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


class TestVunsupportedMixins(TestV40Mixins):

    api_version = 'unsupported'
