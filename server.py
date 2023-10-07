from config import Config
from flask_sqlalchemy import SQLAlchemy
import numpy as np
from flask import Flask
import redis

# Create App and connect Database

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = Config.SQLALCHEMY_DATABASE_URI
app.config["SECRET_KEY"] = Config.SECRET_KEY
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = Config.SQLALCHEMY_TRACK_MODIFICATIONS
db = SQLAlchemy()
db.init_app(app)
redis_client = redis.Redis(host="localhost", port=6379, decode_responses=False)

# Driver Function
if __name__ == "__main__":
    print("\n\nThis is not a web application! 🤡 \nDidn't you read readme?....\n")
    app.run(debug=True, host="0.0.0.0")
