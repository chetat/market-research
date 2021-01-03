from flask import (
    Blueprint,
    abort,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_login import current_user, login_required
from flask_rq import get_queue

from app import db
from app.question.forms import *
from app.decorators import admin_required
from app.email import send_email
from app.models import *

question = Blueprint('question', __name__)


@question.route('/')
@login_required
def index():
    """Question dashboard page."""
    orgs = current_user.organisations + Organisation.query.join(OrgStaff, Organisation.id == OrgStaff.org_id). \
        filter(OrgStaff.user_id == current_user.id).all()
    questions = db.session.query(Question).filter_by(creator_id=current_user.id).first()
    return render_template('question/question_dashboard.html', orgs=orgs, questions=questions)



@question.route('/<org_id>/create/', methods=['Get', 'POST'])
@login_required
def new_question(org_id):
    org = Organisation.query.filter_by(user_id=current_user.id).filter_by(id=org_id).first_or_404()
    form = AddQuestionForm()
    if form.validate_on_submit():
        order_id = db.session.query(Organisation).filter_by(user_id=current_user.id).first()
        appt = Question(
            order_id=order_id.id,
            name=form.name.data,
            description=form.description.data,
            creator_id=current_user.id
            )
        db.session.add(appt)
        db.session.commit()
        flash('Successfully created'.format(appt.name), 'form-success')
        return redirect(url_for('question.question_details',
                                question_id=appt.id, name=appt.name))
    else:
        flash('ERROR! Data was not added.', 'error')
    return render_template('question/create_question.html', form=form, org=org)



@question.route('/<int:question_id>/details/<name>/')
def question_details(question_id, name):
    appts = Question.query.filter(Question.id == question_id).first_or_404()
    org_users = User.query.all()
    #orgs = Organisation.query.filter(Organisation.user_id == User.id).all()
    orgs = current_user.organisations + Organisation.query.join(OrgStaff, Organisation.id == OrgStaff.org_id). \
        filter(OrgStaff.user_id == current_user.id).all()
    return render_template('question/question_details.html', appt=appts, orgs=orgs, org_users=org_users)


@question.route('/<int:question_id>/<name>/', methods=['Get', 'POST'])
@login_required
def edit_question(question_id, name):
##    question_instance = Question.query.filter_by(id=question_id).first()
##    if not question_instance:
##        abort(404)
##    question_form = AddQuestionForm(obj=question_instance)
##    screener_question_form = AddScreenerQuestionForm()
##    multi_choice_form = AddMultipleChoiceQuestionForm()
##    scale_question_form = AddScaleQuestionForm()
##    scale_option_form = AddScaleOptionForm()
##    return render_template("question/question_edit.html", question=question_instance, user=current_user,
##                           question_form=question_form,
##                           screener_question_form=screener_question_form, multi_choice_form=multi_choice_form,
##                           scale_question_form=scale_question_form, scale_option_form=scale_option_form
##                           )
    question_instance = Question.query.filter_by(id=question_id).first()
    if not question_instance:
        abort(404)
    question_form = EditQuestionForm(obj=question_instance)
    if question_form.validate_on_submit():
        order_id = db.session.query(Organisation).filter_by(user_id=current_user.id).first()
        appt = Question(
            order_id=order_id.id,
            name=question_form.name.data,
            description=question_form.description.data,
            creator_id=current_user.id
            )
        db.session.add(appt)
        db.session.commit()

    screener_question_instance = ScreenerQuestion.query.filter_by(question_id=question_id).first()
    screener_question_form = AddScreenerQuestionForm(obj=screener_question_instance)
    if screener_question_form.validate_on_submit():
        screener_question = ScreenerQuestion(
            question_id=question_id,
            title=screener_question_form.title.data,
            description=screener_question_form.description.data,
            required_answer=screener_question_form.required_answer.data,
            options=screener_question_form.options.data,
            )
        db.session.add(screener_question)
        db.session.commit()

    multiple_choice_question_instance = MultipleChoiceQuestion.query.filter_by(question_id=question_id).first()
    multiple_choice_question_form = AddMultipleChoiceQuestionForm(obj=multiple_choice_question_instance)
    if multiple_choice_question_form.validate_on_submit():
        multiple_choice = MultipleChoiceQuestion(
            question_id=question_id,
            title=multiple_choice_question_form.title.data,
            description=multiple_choice_question_form.description.data
            )
        db.session.add(multiple_choice)
        db.session.commit()
        
    appts = Question.query.filter(Question.id == question_id).first_or_404()
    org_users = User.query.all()
    #orgs = Organisation.query.filter(Organisation.user_id == User.id).all()
    orgs = current_user.organisations + Organisation.query.join(OrgStaff, Organisation.id == OrgStaff.org_id). \
        filter(OrgStaff.user_id == current_user.id).all()
    return render_template('question/question_edit.html', appt=appts, orgs=orgs, org_users=org_users,
                           question_form=question_form, screener_question_form=screener_question_form,
                           multiple_choice_question_form=multiple_choice_question_form
                           )


@question.route('/<int:multiple_choice_question_id>/<int:question_id>/<name>', methods=['Get', 'POST'])
@login_required
def edit_multiple_choice_question(multiple_choice_question_id, question_id, name):
    question_instance = Question.query.filter_by(id=question_id).first()
    if not question_instance:
        abort(404)
    multiple_choice_question_instance = MultipleChoiceQuestion.query.filter_by(question_id=question_id).first()
    multiple_choice_question_form = AddMultipleChoiceQuestionForm(obj=multiple_choice_question_instance)
    if multiple_choice_question_form.validate_on_submit():
        multiple_choice = MultipleChoiceQuestion(
            question_id=question_id,
            title=multiple_choice_question_form.title.data,
            description=multiple_choice_question_form.description.data,
            option_one=multiple_choice_question_form.option_one.data,
            option_two=multiple_choice_question_form.option_two.data,
            option_three = multiple_choice_question_form.option_three.data,
            option_four = multiple_choice_question_form.option_four.data,
            option_five = multiple_choice_question_form.option_five.data
            )
        db.session.add(multiple_choice)
        db.session.commit()
    appts = Question.query.filter(Question.id == question_id).first_or_404()
    org_users = User.query.all()
    #orgs = Organisation.query.filter(Organisation.user_id == User.id).all()
    orgs = current_user.organisations + Organisation.query.join(OrgStaff, Organisation.id == OrgStaff.org_id). \
        filter(OrgStaff.user_id == current_user.id).all()
    return render_template('question/multi_choice_question_edit.html', appt=appts, orgs=orgs, org_users=org_users,
                           multiple_choice_question_form=multiple_choice_question_form
                           )

@question.route('/<org_id>/list', methods=['Get', 'POST'])
@login_required
def list_questions(org_id):
    org = Organisation.query.filter_by(id=org_id).first_or_404()
    if current_user.id != org.user_id and current_user not in org.get_staff():
        abort(404)
    questions = Question.query.filter_by(organisation_id=org_id).all()
    return render_template('organisations/list_promos.html', questions=questions, org=org)

