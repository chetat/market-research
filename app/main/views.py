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




#@main.route('/order/<int:org_id>/<int:project_id>/')
#def index(org_id, project_id):
@main.route('/pay')
def index():


    projects = Project.query.filter_by(user_id=current_user.id).first()
    #project = projects.organisation_id
    #order = Order.query.filter_by(Order.project_id == project.id).first()
    
    return render_template('main/index.html', projects=projects, user=current_user)

@main.route('/cancel')
def cancel():
    return render_template('main/cancel.html')


@main.route('/stripe_pay')
def stripe_pay():

    quantity = project.order_quantity
    service_type = project.service_type 
    currency = project.currency
    if currency == "NGN" and service_type == "Silver":
        unit_amount = 660
    elif currency == "NGN" and service_type == "Gold":
        unit_amount = 900
    elif currency == "NGN" and service_type == "Platinum":
        unit_amount = 1200
    elif currency == "USD" and service_type == "Silver":
        unit_amount = 2000
    elif currency == "USD" and service_type == "Gold":
        unit_amount = 2500
    elif currency == "USD" and service_type == "Platinum":
        unit_amount = 3000
    elif currency == "GBP" and service_type == "Silver":
        unit_amount = 2000
    elif currency == "GBP" and service_type == "Gold":
        unit_amount = 2500
    elif currency == "GBP" and service_type == "Platinum":
        unit_amount = 3000
    else:
        unit_amount = 2500
        
    name = project.name
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
          'price_data': {
            'currency': 'usd',
            'product_data': {
              'name': name,
            },
            'unit_amount': unit_amount,
          },
          'quantity': quantity,
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
