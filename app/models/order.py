from .. import db


class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    decision = db.Column(db.Boolean, default=False)
    organisation_id = db.Column(db.Integer, db.ForeignKey('organisations.id', ondelete="CASCADE"), nullable=True)


class Project(db.Model):
    __tablename__ = 'project'
    id = db.Column(db.Integer, primary_key=True)
    organisation_id = db.Column(db.Integer, db.ForeignKey('organisations.id', ondelete="CASCADE"), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    name = db.Column(db.String(64), index=True)
    questions = db.relationship("Question")
    screener_questions = db.relationship("ScreenerQuestion")
    multi_choice_questions = db.relationship("MultipleChoiceQuestion")
    scale_questions = db.relationship("ScaleQuestion")
    project_counters = db.relationship("ProjectCounter")
    
    @property
    def org_name(self):
        from app.models import Organisation
        return Organisation.get(self.organisation_id).org_name
    def __repr__(self):
        return u'<{self.__class__.__name__}: {self.id}>'.format(self=self)

class ProjectCounter(db.Model):
    __tablename__ = 'project_counter'
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    organisation_id = db.Column(db.Integer, db.ForeignKey('organisations.id', ondelete="CASCADE"), nullable=True)
    question_type = db.Column(db.String(64), index=True)
    count_of_questions = db.Column(db.Integer)

    def __repr__(self):
        return u'<{self.__class__.__name__}: {self.id}>'.format(self=self)

class Question(db.Model):
    __tablename__ = 'question'
    id = db.Column(db.Integer, primary_key=True)
    organisation_id = db.Column(db.Integer, db.ForeignKey('organisations.id', ondelete="CASCADE"), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    
    screener_question = db.relationship("ScreenerQuestion")
    scale_question = db.relationship("ScaleQuestion")
    multiple_choice_question = db.relationship("MultipleChoiceQuestion")
    
    @property
    def org_name(self):
        from app.models import Organisation
        return Organisation.get(self.organisation_id).org_name

    def __repr__(self):
        return u'<{self.__class__.__name__}: {self.id}>'.format(self=self)

class ScreenerQuestion(db.Model):
    __tablename__ = 'screener_questions'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(64), index=True)
    description = db.Column(db.String(64), index=True)
    required_answer = db.Column(db.String(64), index=True)
    
    project_id = db.Column(db.Integer, db.ForeignKey('project.id', ondelete="CASCADE"))
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete="CASCADE"))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"))


class MultipleChoiceQuestion(db.Model):
    __tablename__ = 'multiple_choice_questions'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True)
    description = db.Column(db.String(64), index=True)
    multiple_choice_option_one = db.Column(db.String(64), index=True)
    multiple_choice_option_two = db.Column(db.String(64), index=True)
    multiple_choice_option_three = db.Column(db.String(64), index=True)
    multiple_choice_option_four = db.Column(db.String(64), index=True)
    multiple_choice_option_five = db.Column(db.String(64), index=True)
    
    project_id = db.Column(db.Integer, db.ForeignKey('project.id', ondelete="CASCADE"))
    option = db.relationship('Option', backref='options')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"))

    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete="CASCADE"))


class ScaleQuestion(db.Model):
    __tablename__ = 'scale_questions'
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id', ondelete="CASCADE"))
    title = db.Column(db.String(64), index=True)
    description = db.Column(db.String(64), index=True)
    
    option_one = db.Column(db.String(64), index=True)
    option_two = db.Column(db.String(64), index=True)
    option_three = db.Column(db.String(64), index=True)
    option_four = db.Column(db.String(64), index=True)
    option_five = db.Column(db.String(64), index=True)
    
    option_one_scale = db.Column(db.String(64), index=True)
    option_two_scale = db.Column(db.String(64), index=True)
    option_three_scale = db.Column(db.String(64), index=True)
    option_four_scale = db.Column(db.String(64), index=True)
    option_five_scale = db.Column(db.String(64), index=True)
    #project = db.relationship('Project', backref='scale')
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"))

    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete="CASCADE"))

class Option(db.Model):
    __tablename__ = 'options'
    id = db.Column(db.Integer, primary_key=True)
    multiple_choice_question_id = db.Column(db.Integer, db.ForeignKey('multiple_choice_questions.id'))
    option_one = db.Column(db.String(64), index=True)
    option_two = db.Column(db.String(64), index=True)
    option_three = db.Column(db.String(64), index=True)
    option_four = db.Column(db.String(64), index=True)
    option_five = db.Column(db.String(64), index=True)
    multichoice = db.relationship('MultipleChoiceQuestion', backref='options')


class ScaleOption(db.Model):
    __tablename__ = 'scale_options'
    id = db.Column(db.Integer, primary_key=True)
    scale_questions_id = db.Column(db.Integer, db.ForeignKey('scale_questions.id'))
    option = db.Column(db.String(64), index=True)
    scale = db.Column(db.Integer, index=True)
    scale_question = db.relationship('ScaleQuestion', backref='scale_options')
