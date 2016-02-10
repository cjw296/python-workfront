from ...mixins import IssueMixin, Commentable, NoteCommentable, UpdateMixin
from .generated import api


class Issue(IssueMixin, api.Issue):
    pass

api.override(api.Issue, Issue)


class Note(NoteCommentable, api.Note):
    pass

api.override(api.Note, Note)


class Task(Commentable, api.Task):
    pass

api.override(api.Task, Task)


class Update(UpdateMixin, api.Update):
    pass

api.override(api.Update, Update)
