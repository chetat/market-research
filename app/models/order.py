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
    name = db.Column(db.String(64), index=True)
    description = db.Column(db.String(64), index=True)


class ScreenerQuestion(db.Model):
    __tablename__ = 'screener_questions'
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    title = db.Column(db.String(64), index=True)
    description = db.Column(db.String(64), index=True)
    required_answer = db.Column(db.String(64), index=True)
    options = db.Column(db.String(64), index=True)
    question = db.relationship('Question', backref='screener')


class MultipleChoiceQuestion(db.Model):
    __tablename__ = 'multiple_choice_questions'
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    title = db.Column(db.String(64), index=True)
    description = db.Column(db.String(64), index=True)
    question = db.relationship('Question', backref='multichoice')
    options = db.relationship('Option', backref='options')

class Option(db.Model):
    __tablename__ = 'options'
    id = db.Column(db.Integer, primary_key=True)
    multiple_choice_question_id = db.Column(db.Integer, db.ForeignKey('multiple_choice_questions.id'))
    text = db.Column(db.String(64), index=True)

class ScaleQuestion(db.Model):
    __tablename__ = 'scale_questions'
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    title = db.Column(db.String(64), index=True)
    description = db.Column(db.String(64), index=True)
    question = db.relationship('Question', backref='scale')

class ScaleOption(db.Model):
    __tablename__ = 'scale_options'
    id = db.Column(db.Integer, primary_key=True)
    scale_questions_id = db.Column(db.Integer, db.ForeignKey('scale_questions.id'))
    option = db.Column(db.String(64), index=True)
    scale = db.Column(db.Integer, index=True)
