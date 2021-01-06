from flask import (
    Blueprint,
    abort,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)

from app.models import EditableHTML

main = Blueprint('main', __name__)


@main.route('/test')
def index():
    return render_template(
        'main/test.html')

@main.route('/')
def test():
    return redirect(url_for('public.home'))

@main.route('/about')
def about():
    editable_html_obj = EditableHTML.get_editable_html('about')
    return render_template(
        'main/about.html', editable_html_obj=editable_html_obj)
