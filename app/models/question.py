from .. import db
from datetime import datetime
from time import time


class Question(db.Model):
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    question_type = db.Column(db.String(64), index=True)

    multiple_choice_option_one = db.Column(db.String(64))
    multiple_choice_option_two = db.Column(db.String(64))
    multiple_choice_option_three = db.Column(db.String(64))
    multiple_choice_option_four = db.Column(db.String(64))
    multiple_choice_option_five = db.Column(db.String(64))

    option_one = db.Column(db.String(64))
    option_two = db.Column(db.String(64))
    option_three = db.Column(db.String(64))
    option_four = db.Column(db.String(64))
    option_five = db.Column(db.String(64))
    
    option_one_scale = db.Column(db.Integer)
    option_two_scale = db.Column(db.Integer)
    option_three_scale = db.Column(db.Integer)
    option_four_scale = db.Column(db.Integer)
    option_five_scale = db.Column(db.Integer)   
    
    timestamp = db.Column(db.DateTime, index=True, default=db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"))
    project_id = db.Column(db.Integer, db.ForeignKey('project.id', ondelete="CASCADE"))
    organisation_id = db.Column(db.Integer, db.ForeignKey('organisations.id', ondelete="CASCADE"), nullable=True)

    answers = db.relationship('Answer', backref='question', lazy='dynamic')
    screener_question = db.relationship("ScreenerQuestion", backref=db.backref('questions'))
    scale_question = db.relationship("ScaleQuestion", backref=db.backref('questions'))
    multiple_choice_question = db.relationship("MultipleChoiceQuestion", backref=db.backref('questions'))

    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    @property
    def org_name(self):
        from app.models import Organisation
        return Organisation.get(self.organisation_id).org_name

    @property
    def project_name(self):
        from app.models import Project
        return Project.get(self.project_id).name

    def __repr__(self):
        return u'<{self.__class__.__name__}: {self.id}>'.format(self=self)

class Answer(db.Model):
    __tablename__ = 'answers'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String, index=True)
    timestamp = db.Column(db.DateTime, index=True, default=db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"))
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id', ondelete="CASCADE"))
    respondent = db.relationship('User')
    
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    
