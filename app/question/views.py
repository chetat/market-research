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
from app.question.forms import (
    AddMultipleChoiceQuestionForm,
    AddOptionForm,
    AddScaleOptionForm,
    AddScaleQuestionForm,
    AddScreenerQuestionForm,
    AddQuestionForm
    
)
from app.decorators import admin_required
from app.email import send_email
from app.models import Question, User, Organisation

question = Blueprint('question', __name__)


@question.route('/')
@login_required
def index():
    """Question dashboard page."""
    return render_template('question/index.html')


@question.route('/<org_id>/create/', methods=['Get', 'POST'])
@login_required
def new_question(org_id):
    org = Organisation.query.filter_by(user_id=current_user.id).filter_by(id=org_id).first_or_404()
    form = AddQuestionForm()
##    if form.validate_on_submit():
##        order_id = db.session.query(Organisation).filter_by(user_id=current_user.id).first()
##        appt = Question(
##            order_id=order_id.id,
##            name=form.name.data,
##            description=form.description.data,
##            creator_id=current_user.id
##            )
##        db.session.add(appt)
##        db.session.commit()
##        flash('Successfully created'.format(appt.name), 'form-success')
    return render_template('question/create_question.html', form=form, org=org)



@question.route('/<int:question_id>/<name>/')
def question_details(question_id, name):
    appts = Question.query.filter(Question.id == question_id).first_or_404()
    org_users = User.query.all()
    orgs = Organisation.query.filter(Organisation.user_id == User.id).all()
    return render_template('question/question_details.html', appt=appts, orgs=orgs, org_users=org_users)

@question.route('/<org_id>/list', methods=['Get', 'POST'])
@login_required
def list_questions(org_id):
    org = Organisation.query.filter_by(id=org_id).first_or_404()
    if current_user.id != org.user_id and current_user not in org.get_staff():
        abort(404)
    questions = Question.query.filter_by(organisation_id=org_id).all()
    return render_template('organisations/list_promos.html', questions=questions, org=org)

