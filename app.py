import secrets
from flask import Flask
from flask_wtf import CSRFProtect
from routes.main import main_bp
from routes.score import score_bp

app = Flask(__name__)

# Set a secret key for the application
foo = secrets.token_urlsafe(16)
app.secret_key = foo


# registering blueprints
app.register_blueprint(main_bp, url_prefix="/")
app.register_blueprint(score_bp, url_prefix="/score")

# Line required for flask_wtf
csrf = CSRFProtect(app)


if __name__ == '__main__':
    app.run(debug=True)
    