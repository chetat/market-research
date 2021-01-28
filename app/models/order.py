from .. import db


class Association(db.Model):
    __tablename__ = 'association'
    id = db.Column(db.Integer, primary_key=True)
    organisation_id = db.Column(db.Integer, db.ForeignKey('organisations.id', ondelete="CASCADE"), nullable=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    line_items_id = db.Column(db.Integer, db.ForeignKey('line_items.line_item_id'))
    
    screener_question_id = db.Column(db.Integer, db.ForeignKey('screener_questions.id'))
    scale_question_id = db.Column(db.Integer, db.ForeignKey('scale_questions.id'))
    multiple_choice_question_id = db.Column(db.Integer, db.ForeignKey('multiple_choice_questions.id'))
    
    screener_answer_id = db.Column(db.Integer, db.ForeignKey('screener_answers.id'))
    scale_answer_id = db.Column(db.Integer, db.ForeignKey('scale_answers.id'))
    multiple_choice_answer_id = db.Column(db.Integer, db.ForeignKey('multiple_choice_answers.id'))
    
    screener_question = db.relationship("ScreenerQuestion", uselist=False, order_by=id)
    multiple_choice_question = db.relationship("MultipleChoiceQuestion", uselist=False, order_by=id)
    scale_question = db.relationship("ScaleQuestion", uselist=False, order_by=id)
    
    multiple_choice_answer = db.relationship("MultipleChoiceAnswer", uselist=False, order_by=id)
    scale_answer = db.relationship("ScaleAnswer", uselist=False, order_by=id)
    screener_answer = db.relationship("ScaleAnswer", uselist=False, order_by=id)
    line_items = db.relationship("LineItem", uselist=False, order_by=id)

class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    organisation_id = db.Column(db.Integer, db.ForeignKey('organisations.id', ondelete="CASCADE"), nullable=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    delivered = db.Column(db.Boolean(), default=False)
    project = db.relationship("Project", backref=db.backref('orders', order_by=id))
    org = db.relationship("Organisation", backref=db.backref('orders', order_by=id))
    def __repr__(self):
        return "Order(project_id={self.project_id}, " \
                      "delivered={self.delivered})".format(self=self)


class Project(db.Model):
    __tablename__ = 'project'
    id = db.Column(db.Integer, primary_key=True)
    organisation_id = db.Column(db.Integer, db.ForeignKey('organisations.id', ondelete="CASCADE"), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    name = db.Column(db.String(64), index=True)
    order_quantity = db.Column(db.Integer)
    service_type = db.Column(db.String(150))
    currency = db.Column(db.String(150))
    order_status = db.Column(db.String(64), index=True)
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
     order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
     project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
     question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))
     scale_questions_id = db.Column(db.Integer, db.ForeignKey('scale_questions.id'))
     multiple_choice_questions_id = db.Column(db.Integer, db.ForeignKey('multiple_choice_questions.id'))
     quantity = db.Column(db.Integer)
     currency = db.Column(db.String(3))
     service_type = db.Column(db.String(10))
     unit_amount = db.Column(db.Float(12, 2))
     name = db.Column(db.String(64), index=True)
     order = db.relationship("Order", backref=db.backref('line_items',
                         order_by=line_item_id))
     project = db.relationship("Project", backref=db.backref('line_items',
                         order_by=line_item_id))
     question = db.relationship("Question", uselist=False, order_by=line_item_id)
     scale_question = db.relationship("ScaleQuestion", uselist=False, order_by=line_item_id)
     multiple_choice_question = db.relationship("MultipleChoiceQuestion", uselist=False, order_by=line_item_id)


class ScreenerQuestion(db.Model):
    __tablename__ = 'screener_questions'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(90), index=True)
    description = db.Column(db.String)
    required_answer = db.Column(db.String(64), index=True)
    answer_option_one = db.Column(db.String(64), index=True)
    answer_option_two = db.Column(db.String(64), index=True)
    answer_option_three = db.Column(db.String(64), index=True)
    
    project_id = db.Column(db.Integer, db.ForeignKey('project.id', ondelete="CASCADE"))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"))
    screener_answers = db.relationship('Answer', backref='screenerquestion', lazy='dynamic')

class ScreenerAnswer(db.Model):
    __tablename__ = 'screener_answers'
    id = db.Column(db.Integer, primary_key=True)
    required_answer = db.Column(db.String(64), index=True)
    answer_option_one = db.Column(db.String(64), index=True)
    answer_option_two = db.Column(db.String(64), index=True)
    answer_option_three = db.Column(db.String(64), index=True)
    
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
    
    option_one = db.Column(db.String(64), index=True)
    option_two = db.Column(db.String(64), index=True)
    option_three = db.Column(db.String(64), index=True)
    option_four = db.Column(db.String(64), index=True)
    option_five = db.Column(db.String(64), index=True)
    
    option_one_scale = db.Column(db.Integer)
    option_two_scale = db.Column(db.Integer)
    option_three_scale = db.Column(db.Integer)
    option_four_scale = db.Column(db.Integer)
    option_five_scale = db.Column(db.Integer)
    #project = db.relationship('Project', backref='scale')
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"))
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id', ondelete="CASCADE"))
    scale_answers = db.relationship('ScaleAnswer', backref='scalequestion', lazy='dynamic')

class ScaleAnswer(db.Model):
    __tablename__ = 'scale_answers'
    id = db.Column(db.Integer, primary_key=True)
    scale_question_id = db.Column(db.Integer, db.ForeignKey('scale_questions.id', ondelete="CASCADE"))
    
    option_one_answer = db.Column(db.String(64), index=True)
    option_two_answer = db.Column(db.String(64), index=True)
    option_three_answer = db.Column(db.String(64), index=True)
    option_four_answer = db.Column(db.String(64), index=True)
    option_five_answer = db.Column(db.String(64), index=True)
    
    #project = db.relationship('Project', backref='scale')
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"))

