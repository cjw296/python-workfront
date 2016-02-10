from .generated_objects import *


class Commentable(object):

    def add_comment(self, text):
        comment = self.session.api.Note(
            self.session,
            note_text = text,
            note_obj_code = self.code,
            obj_id = self.id
        )
        comment.save()
        return comment


class NoteCommentable(object):

    def add_comment(self, text):
        comment = self.session.api.Note(
            self.session,
            note_text = text,
            note_obj_code = self.note_obj_code,
            obj_id = self.obj_id,
            parent_note_id=self.id
        )
        comment.save()
        return comment


class IssueMixin(Commentable):

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
        return self.session.api.Task(self.session, ID=data['result'])


class UpdateMixin(object):

    @property
    def update_obj(self):
        return self.session.api.from_data(
            self.session, dict(
                ID=self.update_obj_id,
                objCode=self.update_obj_code
            ))
