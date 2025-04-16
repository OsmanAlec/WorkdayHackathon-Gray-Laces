from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisisasecretkey'

from app.routes import chatbot_bp
app.register_blueprint(chatbot_bp)

from app import routes  # This can stay if you have other routes

