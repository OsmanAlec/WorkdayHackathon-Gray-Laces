from app import app
from app.routes import chatbot_bp
app.register_blueprint(chatbot_bp)

if __name__ == "__main__":
    app.run(debug=True)
