from .generated_objects import *


class Commentable(object):

    def add_comment(self, text):
        comment = Note(self.session,
                       note_text = text,
                       note_obj_code = self.code,
                       obj_id = self.id)
        comment.save()
        return comment


class Issue(Commentable, Issue):

    def convert_to_task(self):
        data = self.session.put(
            self.api_url()+'/convertToTask',
            params=dict(
                updates=dict(
                    options=['preserveIssue',
                             'preservePrimaryContact',
                             'preserveUpdates'],
                    task=dict(name=self.name,
                              description=self.description,
                              enteredByID=self.entered_by_id,
                              )
            )))
        return Task(self.session, ID=data['result'])


class Note(Note):

    def add_comment(self, text):
        comment = Note(self.session,
                       note_text = text,
                       note_obj_code = self.note_obj_code,
                       obj_id = self.obj_id,
                       parent_note_id=self.id
                       )
        comment.save()
        return comment


class Task(Commentable, Task):
    pass


class Update(Update):

    @property
    def update_obj(self):
        return Object.from_data(self.session, dict(ID=self.update_obj_id,
                                                   objCode=self.update_obj_code))