import os
from flask import Flask, flash, render_template, redirect, request, session, url_for
from forms import RegisterForm, LoginForm, AddTip
from flask_pymongo import PyMongo
import datetime
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="| Travel | Work | Experience | Life Style")


@app.route("/trip")
def trip():
    return render_template("trip.html", title="| Trip")


@app.route("/work")
def work():
    return render_template("work.html", title="| Work")


@app.route("/life")
def life():
    return render_template("life.html", title="| Life")


@app.route("/tips", methods=["GET", "POST"])
def tips():
    tips = list(mongo.db.tips.find())
    return render_template("tips.html", title="| Tips", tips=tips)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    tips = list(mongo.db.tips.find({"$text": {"$search": query}}))
    return render_template("search.html",  tips=tips)


@app.route("/registration", methods=["GET", "POST"])
def registration():
    form = RegisterForm()
    if form.validate_on_submit():
        register_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        user = {
            "username": request.form.get("username").lower(),
            "email": request.form.get("email"),
            "image": request.form.get("image"),
            "password": generate_password_hash(request.form.get("password")),
            "date_created": datetime.datetime.utcnow()
            }
        mongo.db.users.insert_one(user)
        session["user"] = request.form.get("username").lower()
        flash("Welcome to your new profile!", "reg-success")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("registration.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        
        if existing_user:
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                return redirect(url_for("profile", username=session["user"]))
            else:
                 flash("Incorrect Username and/or Password", "reg-danger")
                 return redirect(url_for("login"))
        
        else:
            flash("Incorrect Username and/or Password", "reg-danger")
            return redirect(url_for("login"))
    return render_template("login.html", title="| Login", form=form)


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    user = mongo.db.users.find_one({"username": session["user"]})
    if session["user"]:
        return render_template("profile.html", username=user["username"], 
                                email=user["email"], date_created=user["date_created"])
    return render_template("profile.html", title="| Profile", username=username)


@app.route("/logout")
def logout():
    flash("You have been logged out!", "log-info")
    session.pop("user")
    return redirect(url_for("home"))


@app.route("/add_tip", methods=["GET", "POST"])
def add_tip():
    form = AddTip()
    if form.validate_on_submit():
        tip = {
            "tip_category": request.form.get("tip_category"),
            "tip_title": request.form.get("tip_title"),
            "tip_description": request.form.get("tip_description"),
            "date_added": datetime.datetime.utcnow(),
            "created_by": session["user"]
        }
        mongo.db.tips.insert_one(tip)
        flash("Tip successfully added!", "reg-success")
        return redirect(url_for("tips"))

    categories = mongo.db.categories.find().sort("tip_category", 1)
    return render_template("add_tip.html", title="| Add Tip", form=form, categories=categories)


@app.route("/update_tip/<tip_id>", methods=["GET", "POST"])
def update_tip(tip_id):
    if request.method == "POST":
        update = {
            "tip_category": request.form.get("tip_category"),
            "tip_title": request.form.get("tip_title"),
            "tip_description": request.form.get("tip_description"),
            "date_added": datetime.datetime.utcnow(),
            "created_by": session["user"]
        }
        mongo.db.tips.update({"_id": ObjectId(tip_id)}, update)
        flash("Tip successfully updated", "reg-success")
        return redirect(url_for("tips"))

    tip = mongo.db.tips.find_one({"_id": ObjectId(tip_id)})
    categories = mongo.db.categories.find().sort("tip_category", 1)
    return render_template("update_tip.html", tip=tip, categories=categories)


@app.route("/delete_tip/<tip_id>")
def delete_tip(tip_id):
    mongo.db.tips.remove({"_id": ObjectId(tip_id)})
    flash("Tip successfully deleted, add the new one!", "tip-deleted")
    return redirect(url_for("add_tip"))


@app.route("/delete_user")
def delete_user():
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    mongo.db.users.remove({"username":username})
    flash("Your profile is deleted!", "profile-deleted")
    session.pop("user")
    return redirect("registration")
    return render_template("registration.html", title="| Home")


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html', error=error), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html', error=error), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)