import os

BaseDir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "SECRET_HUSH!"
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URI"
    ) or "sqlite:///" + os.path.join(BaseDir, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = True
