from flask import (
    Blueprint,
    abort,
    flash,
    redirect,
    render_template,
    request,
    url_for, 
    jsonify,
    current_app,
    send_from_directory
)
from flask_login import current_user, login_required
from app import db
from app.models import EditableHTML, Project, Organisation, Order, User
from app.main.forms import AddOrderForm
import stripe
import os

main = Blueprint('main', __name__)


STRIPE_PUBLISHABLE_KEY="pk_test_oqKtiHQipsUaIuR81LYSiDW2"
STRIPE_SECRET_KEY="sk_test_hqoFMPptGIiQJSuk6Yg6B2Fr"
#STRIPE_ENDPOINT_SECRET="whsec_429KA0GICAAwyH3mVix0HYDLDZk9jybp"

# This is your real test secret API key.
stripe.api_key = 'sk_test_hqoFMPptGIiQJSuk6Yg6B2Fr'




@main.route('/order/<org_id>/<project_id>/form/', methods=['Get', 'POST'])
def index(org_id, project_id):
    org = Organisation.query.filter_by(user_id=current_user.id).filter_by(id=org_id).first()
    project = Project.query.filter(Project.id == project_id).first()
    order = Order.query.filter(Order.project_id == project_id).first()
    
    form = AddOrderForm(request.form)
    if request.method == 'POST' and form.validate():
        #order_quantity=request.form['order_quantity']
        #service_type=request.form['service_type']
        #currency=request.form['currency']
        appt = Order(
           project_id = project.id,
           organisation_id = org.id,
           order_quantity=form.order_quantity.data,
           service_type=form.service_type.data,
           currency=form.currency.data)
        db.session.add(appt)
        db.session.commit()
        flash('Successfully added service order details for '.format(project.name), 'form-success')
        return redirect(url_for('main.stripe_pay'))
    else:
        flash('ERROR! Data was not added.', 'error')
        
    return render_template('main/index.html', org_id=org.id, project_id=project.id,
                           project=project, org=org, order=order, form=form)

@main.route('/cancel')
def cancel():
    return render_template('main/cancel.html')


@main.route('/stripe_pay')
def stripe_pay():
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': 'price_1IC7MsHVpMGbwApFC7BjUL9G',
            'quantity': 1000,
        }],
        mode='payment',
        success_url=url_for('main.thanks', _external=True) + '?session_id={CHECKOUT_SESSION_ID}',
        cancel_url=url_for('main.cancel', _external=True),
    )
    return {
        'checkout_session_id': session['id'], 
        'checkout_public_key': "pk_test_oqKtiHQipsUaIuR81LYSiDW2"
    }

@main.route('/thanks')
def thanks():
    return render_template('main/thanks.html')

@main.route('/stripe_webhook', methods=['POST'])
def stripe_webhook():
    print('WEBHOOK CALLED')

    if request.content_length > 1024 * 1024:
        print('REQUEST TOO BIG')
        abort(400)
    payload = request.get_data()
    sig_header = request.environ.get('HTTP_STRIPE_SIGNATURE')
    endpoint_secret = 'whsec_429KA0GICAAwyH3mVix0HYDLDZk9jybp'
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        print('INVALID PAYLOAD')
        return {}, 400
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        print('INVALID SIGNATURE')
        return {}, 400

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        print(session)
        line_items = stripe.checkout.Session.list_line_items(session['id'], limit=1)
        print(line_items['data'][0]['description'])

    return {}
    
@main.route('/about')
def about():
    editable_html_obj = EditableHTML.get_editable_html('about')
    return render_template(
        'main/about.html', editable_html_obj=editable_html_obj)
