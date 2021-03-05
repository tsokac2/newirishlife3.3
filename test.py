import app as app_module
import unittest
import os
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask import session
import datetime
if os.path.exists("env.py"):
    import env


app = app_module.app

app.config["TESTING"] = True
app.config["WTF_CSRF_ENABLED"] = False
app.config['MONGO_URI'] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)
app_module.mongo = mongo


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        with app.app_context():
            mongo.db.users.delete_many({})
            mongo.db.tips.delete_many({})


class AppTests(AppTestCase):
    def test_home(self):
        """Test Home page load response"""
        res = self.client.get("/")
        data = res.data.decode("utf-8")
        assert res.status == "200 OK"
        assert "Gandalf" in data

    def test_trip(self):
        """Test Trip page load response"""
        res = self.client.get("/trip")
        data = res.data.decode("utf-8")
        assert res.status == "200 OK"
        assert "Trip" in data

    def test_work(self):
        """Test Work page load response"""
        res = self.client.get("/work")
        data = res.data.decode("utf-8")
        assert res.status == "200 OK"
        assert "Work" in data

    def test_life(self):
        """Test Life page load response"""
        res = self.client.get("/life")
        data = res.data.decode("utf-8")
        assert res.status == "200 OK"
        assert "Life" in data

    def test_tips(self):
        """Test Tips page load response"""
        res = self.client.get("/tips")
        data = res.data.decode("utf-8")
        assert res.status == "200 OK"
        assert "Bits and pieces" in data

    def test_signup(self):
        """Test Signup page load response"""
        res = self.client.get("/registration")
        data = res.data.decode("utf-8")
        assert res.status == "200 OK"
        assert "Create Account" in data

    def test_login(self):
        """Test Login page load response"""
        res = self.client.get("/login")
        data = res.data.decode("utf-8")
        assert res.status == "200 OK"
        assert "Already a member!" in data

    def test_login_func(self):
        """Test Login functionality"""
        res = self.client.post("/login", data=dict(
            username="tom",
            password="password"
            ))
        data = res.data.decode("utf-8")
        assert 'tom' in data
