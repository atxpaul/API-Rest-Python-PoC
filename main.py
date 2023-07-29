from flask import Flask
from app.controllers.time_controller import time_bp

app = Flask(__name__)

app.register_blueprint(time_bp)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
