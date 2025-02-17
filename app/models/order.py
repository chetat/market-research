from .. import db

from datetime import datetime
from logging import log
from time import time

class StripeData(db.Model):
    __tablename__ = 'stripe_data'
    id = db.Column(db.Integer, primary_key=True)
    currency = db.Column(db.String)
    payment_intent = db.Column(db.String(180))
    customer_email = db.Column(db.String(64))
    customer = db.Column(db.String(64))
    customer_details = db.Column(db.String(64))
    client_reference_id = db.Column(db.String(64))
    payment_method = db.Column(db.String(10))
    payment_status = db.Column(db.String(10))
    amount_total = db.Column(db.Integer)
    session_id = db.Column(db.String(90))


class StripeEvent(db.Model):
    __tablename__ = 'stripe_events'
    id = db.Column(db.Integer, primary_key=True)
   #currency = db.Column(db.String)
    payment_intent = db.Column(db.String(180))
    outcome = db.Column(db.String(64))
    customer = db.Column(db.String(64))
    payment_method = db.Column(db.String(10))
    payment_method_details = db.Column(db.String(10))
    billing_details = db.Column(db.String(10))
    disputed = db.Column(db.String(10))
    status = db.Column(db.String(10))
    amount = db.Column(db.Integer)
    application_fee_amount=db.Column(db.Integer)
    receipt_url = db.Column(db.String(64))
    type = db.Column(db.String(10))



class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    organisation_id = db.Column(db.Integer, db.ForeignKey('organisations.id', ondelete="CASCADE"), nullable=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id', ondelete="CASCADE"), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    line_item_id = db.Column(db.Integer, db.ForeignKey('line_items.line_item_id'))
    quantity = db.Column(db.Integer)
    currency = db.Column(db.String(3))
    payment_intent = db.Column(db.String(180))
    customer_email = db.Column(db.String(64))
    payment_method = db.Column(db.String(10))
    payment_status = db.Column(db.String(10))
    total_amount = db.Column(db.Integer)
    session_id = db.Column(db.String(90))
    delivered = db.Column(db.Boolean(), default=False)
    created_at = db.Column(db.DateTime, default=db.func.now())
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
    org = db.relationship("Organisation", backref=db.backref('orders', order_by=id))
    user = db.relationship("User", backref=db.backref('orders', order_by=id))
    project = db.relationship("Project", backref=db.backref('orders', order_by=id))
    line_item = db.relationship("LineItem", backref=db.backref('orders', order_by=id))
    
    def __repr__(self):
        return "Order(project_id={self.project_id}, " \
                      "delivered={self.delivered})".format(self=self)



class PaidProject(db.Model):
     __tablename__= 'paid_projects'
     id = db.Column(db.Integer, primary_key=True)
     order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
     project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
     question_id = db.Column(db.Integer)
     respondent_id = db.Column(db.Integer)
     question = db.Column(db.String)
     question_type = db.Column(db.String)
     description = db.Column(db.String)
     answer = db.Column(db.String)
     answer_option_one = db.Column(db.String)
     answer_option_two = db.Column(db.String)
     answer_option_three = db.Column(db.String)
     answer_option_four = db.Column(db.String)
     answer_option_five = db.Column(db.String)
     respondent_location = db.Column(db.String)

     project_name = db.Column(db.String(64), index=True)
     #order = db.relationship("Order", backref=db.backref('paid_projects', order_by=id))
     #project = db.relationship("Project", backref=db.backref('paid_projects', order_by=id))
     #screener_answers = db.relationship("ScreenerAnswer", backref=db.backref('paid_projects', order_by=id))
     #scale_answers = db.relationship("ScaleAnswer", backref=db.backref('paid_projects', order_by=id))
     #multiple_choice_answers = db.relationship("MultipleChoiceAnswer", backref=db.backref('paid_projects', order_by=id))
     #scale_questions = db.relationship("ScaleQuestion", backref=db.backref('paid_projects', order_by=id))
     #multiple_choice_questions = db.relationship("MultipleChoiceQuestion", backref=db.backref('paid_projects', order_by=id))
     #screener_questions = db.relationship("ScreenerQuestion", backref=db.backref('paid_projects', order_by=id))

class Project(db.Model):
    __tablename__ = 'project'
    id = db.Column(db.Integer, primary_key=True)
    organisation_id = db.Column(db.Integer, db.ForeignKey('organisations.id', ondelete="CASCADE"), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    name = db.Column(db.String(64), index=True)
    order_quantity = db.Column(db.Integer)
    service_type = db.Column(db.String(150))
    currency = db.Column(db.String(150))

    questions = db.relationship('Question', backref='project', lazy='dynamic')
    multiple_choice_questions = db.relationship('MultipleChoiceQuestion', backref='project', lazy='dynamic')
    scale_questions = db.relationship('ScaleQuestion', backref='project', lazy='dynamic')
    screener_questions = db.relationship('ScreenerQuestion', backref='project', lazy='dynamic')
    
    @property
    def org_name(self):
        from app.models import Organisation
        return Organisation.get(self.organisation_id).org_name
    def __repr__(self):
        return u'<{self.__class__.__name__}: {self.id}>'.format(self=self)

class LineItem(db.Model):
     __tablename__= 'line_items'
     line_item_id = db.Column(db.Integer, primary_key=True)
     project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
     quantity = db.Column(db.Integer)
     currency = db.Column(db.String(3))
     service_type = db.Column(db.String(10))
     unit_amount = db.Column(db.Integer)
     tax_amount = db.Column(db.Integer)
     tax_percentage = db.Column(db.Integer)
     name = db.Column(db.String(64), index=True)
     project = db.relationship("Project", backref=db.backref('line_items',
                         order_by=line_item_id))
     user = db.relationship("User", backref=db.backref('line_items',
                         order_by=line_item_id))


class ScreenerQuestion(db.Model):
    __tablename__ = 'screener_questions'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(90), index=True)
    description = db.Column(db.String)
    required_answer = db.Column(db.String(64), index=True)
    answer_option_one = db.Column(db.String(64), index=True)
    answer_option_two = db.Column(db.String(64), index=True)
    answer_option_three = db.Column(db.String(64), index=True)

    question_id = db.Column(db.Integer, db.ForeignKey('questions.id', ondelete="CASCADE"))    
    project_id = db.Column(db.Integer, db.ForeignKey('project.id', ondelete="CASCADE"))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"))
    screener_answers = db.relationship('ScreenerAnswer', backref='screenerquestion', lazy='dynamic')

    def __init__(self, question_id, user_id, required_answer, answer_option_one,
                 answer_option_two, answer_option_three, question, description):
        self.question_id = question_id
        self.user_id = user_id
        self.required_answer = required_answer
        self.answer_option_one = answer_option_one
        self.answer_option_two = answer_option_two
        self.answer_option_three = answer_option_three

    def __repr__(self):
        return ' [ScreenerQuestion {}]'.format(self.answer_option_one)

class ScreenerAnswer(db.Model):
    __tablename__ = 'screener_answers'
    id = db.Column(db.Integer, primary_key=True)
    answer_option_one = db.Column(db.String(64), index=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id', ondelete="CASCADE"))
    screener_questions_id = db.Column(db.Integer, db.ForeignKey('screener_questions.id', ondelete="CASCADE"))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"))
    

class MultipleChoiceQuestion(db.Model):
    __tablename__ = 'multiple_choice_questions'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(90), index=True)
    description = db.Column(db.String)
    multiple_choice_option_one = db.Column(db.String(64), index=True)
    multiple_choice_option_two = db.Column(db.String(64), index=True)
    multiple_choice_option_three = db.Column(db.String(64), index=True)
    multiple_choice_option_four = db.Column(db.String(64), index=True)
    multiple_choice_option_five = db.Column(db.String(64), index=True)
    
    project_id = db.Column(db.Integer, db.ForeignKey('project.id', ondelete="CASCADE"))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"))

    question_id = db.Column(db.Integer, db.ForeignKey('questions.id', ondelete="CASCADE"))
    multiple_choice_answers = db.relationship('MultipleChoiceAnswer', backref='multiplechoicequestion', lazy='dynamic')

class MultipleChoiceAnswer(db.Model):
    __tablename__ = 'multiple_choice_answers'
    id = db.Column(db.Integer, primary_key=True)
    multiple_choice_answer_one = db.Column(db.String(64), index=True)
    multiple_choice_answer_two = db.Column(db.String(64), index=True)
    multiple_choice_answer_three = db.Column(db.String(64), index=True)
    multiple_choice_answer_four = db.Column(db.String(64), index=True)
    multiple_choice_answer_five = db.Column(db.String(64), index=True)
    
    multiple_choice_question_id = db.Column(db.Integer, db.ForeignKey('multiple_choice_questions.id', ondelete="CASCADE"))
    project_id = db.Column(db.Integer, db.ForeignKey('project.id', ondelete="CASCADE"))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"))


class ScaleQuestion(db.Model):
    __tablename__ = 'scale_questions'
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id', ondelete="CASCADE"))
    title = db.Column(db.String(90), index=True)
    description = db.Column(db.String)
    
    options = db.Column(db.String(64), index=True)
    #project = db.relationship('Project', backref='scale')
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"))
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id', ondelete="CASCADE"))
    scale_answers = db.relationship('ScaleAnswer', backref='scalequestion', lazy='dynamic')

class ScaleAnswer(db.Model):
    __tablename__ = 'scale_answers'
    id = db.Column(db.Integer, primary_key=True)
    scale_question_id = db.Column(db.Integer, db.ForeignKey('scale_questions.id', ondelete="CASCADE"))
    
    option = db.Column(db.String(64), index=True)
    
    #project = db.relationship('Project', backref='scale')
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"))

