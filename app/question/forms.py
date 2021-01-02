from flask_wtf import FlaskForm
from wtforms import ValidationError
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.fields import (
    PasswordField,
    StringField,
    SubmitField,
    SelectField
)
from wtforms.fields.html5 import EmailField
from wtforms.validators import (
    Email,
    EqualTo,
    InputRequired,
    Length,
)

from app import db
from app.models import Role, User


class AddQuestionForm(FlaskForm):
    name = StringField(
        'Project Name', validators=[InputRequired(),
                                  Length(1, 64)])
    description = StringField(
        'description', validators=[InputRequired(),
                                  Length(1, 90)])
    submit = SubmitField('Submit')

class AddScreenerQuestionForm(FlaskForm):
    title = StringField(
        'Screener Question Title', validators=[InputRequired(),
                                  Length(1, 64)])
    description = StringField(
        'description', validators=[InputRequired(),
                                  Length(1, 90)])
    required_answer = SelectField(u'What is the required screener answer?', choices=[('Yes', 'Yes'), ('No', 'No')])
    options = SelectField(u'Please choose either Yes or No', choices=[('Yes', 'Yes'), ('No', 'No')])
    submit = SubmitField('Submit')


class AddMultipleChoiceQuestionForm(FlaskForm):
    title = StringField(
        'Screener Question Title', validators=[InputRequired(),
                                  Length(1, 64)])
    description = StringField(
        'description', validators=[InputRequired(),
                                  Length(1, 90)])
    submit = SubmitField('Submit')

class AddOptionForm(FlaskForm):
     text = StringField(
        'Add Text', validators=[InputRequired(),
                                  Length(1, 64)])
     submit = SubmitField('Submit')   


class AddScaleQuestionForm(FlaskForm):
    title = StringField(
        'Screener Question Title', validators=[InputRequired(),
                                  Length(1, 64)])
    description = StringField(
        'description', validators=[InputRequired(),
                                  Length(1, 90)])
    submit = SubmitField('Submit')
    
class AddScaleOptionForm(FlaskForm):
    option = SelectField(u'Please choose either Yes or No', choices=[('Strongly Agree', 'Strongly Agree'), ('Agree', 'Agree'),
                                                                     ('Undecided', 'Undecided'), ('Disagree', 'Disagree'),
                                                                     ('Strongly Disagree', 'Strongly Disagree'), ('Not at all useful', 'Not at all useful'),
                                                                     ('Slightly useful', 'Slightly useful'), ('Moderately useful', 'Moderately useful'),
                                                                     ('Very useful', 'Very useful'), ('Extremely useful', 'Extremely useful'),
                                                                     ('Most useful', 'Most useful'), ('Least useful', 'Least useful')])
    scale = SelectField(u'Please choose the scale for the question', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')])
    submit = SubmitField('Submit')
