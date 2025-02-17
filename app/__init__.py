import os

from flask import Flask
from flask_assets import Environment
from flask_compress import Compress
from flask_login import LoginManager
from flask_mail import Mail
from flask_rq import RQ
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_share import Share
from flask_ckeditor import CKEditor
from flask_bootstrap import Bootstrap



from app.assets import app_css, app_js, vendor_css, vendor_js
from config import config as Config

basedir = os.path.abspath(os.path.dirname(__file__))

mail = Mail()
db = SQLAlchemy()
csrf = CSRFProtect()
compress = Compress()
images = UploadSet('images', IMAGES)
docs = UploadSet('docs', ('rtf', 'odf', 'ods', 'gnumeric', 'abw', 'doc', 'docx', 'xls', 'xlsx', 'pdf'))
share = Share()
#bootstrap = Boostrap()

# Set up Flask-Login
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'account.login'


def create_app(config):
    app = Flask(__name__)
    config_name = config

    if not isinstance(config, str):
        config_name = os.getenv('FLASK_CONFIG', 'default')

    app.config.from_object(Config[config_name])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # not using sqlalchemy event system, hence disabling it

    Config[config_name].init_app(app)

    # Set up extensions
    mail.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    compress.init_app(app)
    RQ(app)
    configure_uploads(app, images)
    configure_uploads(app, docs)
    CKEditor(app)
    share.init_app(app)
    Bootstrap(app)
    
    # Register Jinja template functions
    from .utils import register_template_utils
    register_template_utils(app)

    # Set up asset pipeline
    assets_env = Environment(app)
    dirs = ['assets/styles', 'assets/scripts']
    for path in dirs:
        assets_env.append_path(os.path.join(basedir, path))
    assets_env.url_expire = True

    assets_env.register('app_css', app_css)
    assets_env.register('app_js', app_js)
    assets_env.register('vendor_css', vendor_css)
    assets_env.register('vendor_js', vendor_js)

    # Configure SSL if platform supports it
    if not app.debug and not app.testing and not app.config['SSL_DISABLE']:
        from flask_sslify import SSLify
        SSLify(app)

    # Create app blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .public import public as public_blueprint
    app.register_blueprint(public_blueprint)
    
    from .account import account as account_blueprint
    app.register_blueprint(account_blueprint, url_prefix='/account')

    from .question import question as question_blueprint
    app.register_blueprint(question_blueprint, url_prefix='/question')

    from .answer import answer as answer_blueprint
    app.register_blueprint(answer_blueprint, url_prefix='/answer')

    from .project import project as project_blueprint
    app.register_blueprint(project_blueprint, url_prefix='/project')
    
    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    from .organisations import organisations as organisations_blueprint
    app.register_blueprint(organisations_blueprint, url_prefix='/organisations')

    from .blog import blog
    app.register_blueprint(blog, url_prefix='/blog')



    return app
