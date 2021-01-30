from flask_wtf import FlaskForm
from wtforms import ValidationError
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.fields import (
    PasswordField,
    StringField,
    SubmitField,
    SelectField,
    RadioField
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




class AddScreenerAnswerForm(FlaskForm):
    answer_option_one = RadioField(u'Please choose either Yes or No or Maybe options', choices=[('Yes', 'Yes'), ('No', 'No') , ('Maybe', 'Maybe')])
    submit = SubmitField('Submit')


class AddMultipleChoiceQuestionForm(FlaskForm):
    title = StringField(
        'Question', validators=[InputRequired(),
                                  Length(1, 90)])
    description = StringField(
        'Description', validators=[InputRequired(),
                                  Length(1, 90)])
    multiple_choice_option_one = StringField(
        'Required answer option e.g "Yes" ', validators=[InputRequired(),
                                  Length(1, 64)])

    multiple_choice_option_two = StringField(
        'Required answer option e.g "No" ', validators=[InputRequired(),
                                  Length(1, 64)])
    multiple_choice_option_three = StringField(
        'Optional answer option. You can leave it empty if you selected "Yes" or "No" in the previous ones ')
    multiple_choice_option_four = StringField(
        'Optional answer option. You can leave it empty if you selected "Yes" or "No" in the previous ones')
    multiple_choice_option_five = StringField(
        'Optional answer option. You can leave it empty if you selected "Yes" or "No" in the previous ones')
    submit = SubmitField('Submit')


class AddMultipleChoiceAnswerForm(FlaskForm):
    multiple_choice_option_one = StringField(
        'Required answer option e.g "Yes" ', validators=[InputRequired(),
                                  Length(1, 64)])

    multiple_choice_option_two = StringField(
        'Required answer option e.g "No" ', validators=[InputRequired(),
                                  Length(1, 64)])
    multiple_choice_option_three = StringField(
        'Optional answer option. You can leave it empty if you selected "Yes" or "No" in the previous ones ')
    multiple_choice_option_four = StringField(
        'Optional answer option. You can leave it empty if you selected "Yes" or "No" in the previous ones')
    multiple_choice_option_five = StringField(
        'Optional answer option. You can leave it empty if you selected "Yes" or "No" in the previous ones')
    submit = SubmitField('Submit')


class AddScaleAnswerForm(FlaskForm):
    options = RadioField(u'Please choose your answer options', choices=[('Strongly Agree', 'Strongly Agree'), ('Agree', 'Agree'),
                                                                     ('Undecided', 'Undecided'), ('Disagree', 'Disagree'),
                                                                     ('Strongly Disagree', 'Strongly Disagree'), ('Not at all useful', 'Not at all useful'),
                                                                     ('Slightly useful', 'Slightly useful'), ('Moderately useful', 'Moderately useful'),
                                                                     ('Very useful', 'Very useful'), ('Extremely useful', 'Extremely useful'),
                                                                     ('Most useful', 'Most useful'), ('Least useful', 'Least useful')])
    submit = SubmitField('Submit')
