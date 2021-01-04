from .. import db


class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    questions = db.relationship("Question")
    decision = db.Column(db.Boolean, default=False)
    organisation_id = db.Column(db.Integer, db.ForeignKey('organisations.id', ondelete="CASCADE"), nullable=True)

class Question(db.Model):
    __tablename__ = 'question'
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    organisation_id = db.Column(db.Integer, db.ForeignKey('organisations.id', ondelete="CASCADE"), nullable=True)
    question = db.Column(db.String(64), index=True)
    description = db.Column(db.String(64), index=True)
    option_one = db.Column(db.String(64), index=True)
    option_two = db.Column(db.String(64), index=True)
    option_three = db.Column(db.String(64), index=True)
    option_four = db.Column(db.String(64), index=True)
    option_five = db.Column(db.String(64), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"), nullable=False)

    #multiple_choice_questions_id = db.Column(db.Integer, db.ForeignKey('multiple_choice_questions.id', ondelete="CASCADE"), nullable=False)
    #multiple_choice_question = db.relationship('MultipleChoiceQuestion', backref='questions', cascade='all, delete')
    
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
    options = db.Column(db.String(64), index=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete="CASCADE"))
    question = db.relationship('Question', backref='screener')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"))


class MultipleChoiceQuestion(db.Model):
    __tablename__ = 'multiple_choice_questions'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True)
    description = db.Column(db.String(64), index=True)
    option_one = db.Column(db.String(64), index=True)
    option_two = db.Column(db.String(64), index=True)
    option_three = db.Column(db.String(64), index=True)
    option_four = db.Column(db.String(64), index=True)
    option_five = db.Column(db.String(64), index=True)
    question = db.relationship('Question', backref='multi_choice_questions')
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete="CASCADE"))
    option = db.relationship('Option', backref='options')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"))
    #def __repr__(self):
        #return "<MultipleChoiceQuestion(email_address='%s')>" % self.email_address

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

class ScaleQuestion(db.Model):
    __tablename__ = 'scale_questions'
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete="CASCADE"))
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
    question = db.relationship('Question', backref='scale')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"))

class ScaleOption(db.Model):
    __tablename__ = 'scale_options'
    id = db.Column(db.Integer, primary_key=True)
    scale_questions_id = db.Column(db.Integer, db.ForeignKey('scale_questions.id'))
    option = db.Column(db.String(64), index=True)
    scale = db.Column(db.Integer, index=True)
    scale_question = db.relationship('ScaleQuestion', backref='scale_options')
