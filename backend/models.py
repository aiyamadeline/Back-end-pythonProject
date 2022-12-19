from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from . import db


class members(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String)

    def __init__(self, username, password):
        self.username = username
        self.password = password



