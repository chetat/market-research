from flask import (
    Blueprint,
    abort,
    flash,
    redirect,
    render_template,
    request,
    url_for,
    jsonify,
    send_from_directory
)
from flask_login import current_user, login_required
from flask_rq import get_queue

from app import db
from app.answer.forms import *
from app.decorators import admin_required, respondent_required
from app.email import send_email
from app.models import *
from sqlalchemy import func


answer = Blueprint('answer', __name__)



@answer.route('/<int:project_id>/<int:question_id>/<question>/add/', methods=['Get', 'POST'])
@respondent_required
def add_screener_answer(project_id, question_id, question):
    
    project = db.session.query(Project).filter_by(user_id=current_user.id).filter(Project.id==project_id).first()
    question = LineItem.query.filter(LineItem.project_id == project_id).first()

    #question = MultipleChoiceQuestion.query.filter_by(user_id=current_user.id).filter_by(id=question_id).first_or_404()
    #if not question:
        #abort(404)
    #if current_user.id != question.user_id:
        #abort(404)
    screener_question = ScreenerQuestion.query.filter_by(user_id=current_user.id).filter_by(id=question_id).first_or_404()

    form = AddScreenerAnswerForm()
    if form.validate_on_submit():
        appt = ScreenerAnswer(
            screener_questions_id=screener_question.id,
            answer_option_one=form.answer_option_one.data,
            user_id=current_user.id
            )
        db.session.add(appt)
        db.session.commit()
        flash("Answer submitted.", 'success')
        return redirect(url_for('question.question_details', project_id=project.id, name=project.name))
    return render_template('answer/add_screener_answer.html', screener_question=screener_question, form=form)

@answer.route('/<int:project_id>/<int:question_id>/<question>/add/', methods=['Get', 'POST'])
@respondent_required
def add_scale_answer(project_id, question_id, question):
    
    project = db.session.query(Project).filter_by(user_id=current_user.id).filter(Project.id==project_id).first()
    question = LineItem.query.filter(LineItem.project_id == project_id).first()

    scale_question = ScaleQuestion.query.filter_by(user_id=current_user.id).filter_by(id=question_id).first_or_404()

    form = AddScaleAnswerForm()
    if form.validate_on_submit():
        appt = ScaleAnswer(
            scale_questions_id=scale_question.id,
            answer_option_one=form.answer_option_one.data,
            user_id=current_user.id
            )
        db.session.add(appt)
        db.session.commit()
        flash("Answer submitted.", 'success')
        return redirect(url_for('question.question_details', project_id=project.id, name=project.name))
    return render_template('answer/add_scale_answer.html', scale_question=scale_question, form=form)
