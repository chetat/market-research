from .. import db


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
    
    project_id = db.Column(db.Integer, db.ForeignKey('project.id', ondelete="CASCADE"))
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id', ondelete="CASCADE"))
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
    option = db.relationship('Option', backref='options')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"))

    question_id = db.Column(db.Integer, db.ForeignKey('questions.id', ondelete="CASCADE"))


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
