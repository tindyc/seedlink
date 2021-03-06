import os
from datetime import date, datetime
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


date = date.today()


# Renders home page
@app.route("/")
@app.route("/index")
def index():
    if request.method == "GET":
        products = mongo.db.donation.find().limit(4).sort("date_created", 1)

    return render_template("index.html", products=products)


# Renders marketplace page
@app.route("/marketplace", methods=["GET"])
def marketplace():
    if request.method == "GET":
        products = mongo.db.donation.find()

    return render_template("marketplace.html", products=products)


# Register user in the db
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Check if user already in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists!")
            return redirect(url_for("register"))

        # check if email already in db
        existing_email = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})

        if existing_email:
            flash("Email address already registered!")
            return redirect(url_for("register"))

        # add user details to db
        register = {
            "firstname": request.form.get("firstname").lower(),
            "lastname": request.form.get("lastname").lower(),
            "username": request.form.get("username").lower(),
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "date_created": date.strftime("%d %b %Y"),
        }
        mongo.db.users.insert_one(register)

        # put the user into a session cookie
        session["user"] = request.form.get("username").lower()
        flash("Sign Up Successful!")
        return redirect(url_for("my_profile", username=session["user"]))

    return render_template("register.html")


# Log existing user into site
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Check if user already in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        # ensure password matches
        if existing_user:
            if check_password_hash(existing_user["password"],
                                   request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                return redirect(url_for("my_profile",
                                username=session["user"]))
            else:
                # invalid password
                flash("Incorrect Username/Password!")
                return redirect(url_for("login"))
        else:
            # username doesn't exist/is incorrect
            flash("Incorrect Usernname/Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# Logs user out of their account
@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# Add profile form
@app.route("/add_profile", methods=["GET", "POST"])
def add_profile():
    if request.method == "POST":
        # default values if fields are left blank
        default_img = ("profile_image.png")
        profile = {
            "fullname": request.form.get("fullname"),
            "birthday": request.form.get("birthday"),
            "image": request.form.get("image") or default_img,
            "created_by": session["user"],
            "date_created": date.strftime("%d %b %Y")
        }
        mongo.db.profiles.insert_one(profile)
        flash("Your Profile Has Been Added")
        return redirect(url_for("my_profile", username=session["user"]))

    profiles = mongo.db.profiles.find().sort("fullname", 1)
    return render_template("add_profile.html", profiles=profiles)


# Update profile form
@app.route("/update_profile/<profile_id>", methods=["GET", "POST"])
def update_profile(profile_id):
    if request.method == "POST":
        # default values if fields are left blank
        default_img = ("profile_image.png")
        update = {
            "fullname": request.form.get("fullname"),
            "birthday": request.form.get("birthday"),
            "image": request.form.get("image") or default_img,
            "created_by": session["user"],
            "date_created": date.strftime("%d %b %Y")
        }
        mongo.db.profiles.update({"_id": ObjectId(profile_id)}, update)
        flash("Your Profile Has Been Updated")
        return redirect(url_for("my_profile", username=session["user"]))

    profile = mongo.db.profiles.find_one({"_id": ObjectId(profile_id)})
    profiles = mongo.db.profiles.find().sort("fullname", 1)
    return render_template("update_profile.html", profile=profile,
                           profiles=profiles)


# Display personal profile page
@app.route("/my_profile/<username>", methods=["GET", "POST"])
def my_profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    if session["user"]:
        my_profile = list(mongo.db.profiles.find(
            {"created_by": session["user"]}))
        user = mongo.db.users.find_one({"username": session["user"]})
        return render_template("profile.html", username=username,
                               user=user, profiles=my_profile)
    return redirect(url_for('login'))


# Add Donation form
@app.route("/add_donation", methods=["GET", "POST"])
def add_donation():
    if request.method == "POST":
        donation = {
            "product_category": request.form.get("product_category"),
            "product_name": request.form.get("product_name"),
            "quantity": request.form.get("quantity"),
            "expiry_date": request.form.get("expiry_date"),
            "created_by": session["user"],
            "date_created": date.strftime("%d %b %Y"),
        }
        mongo.db.donation.insert_one(donation)
        flash("Your donation has been added to the marketplace!")
        return redirect(url_for("marketplace"))

    donation = mongo.db.donation.find().sort("product_category", 1)
    return render_template("add_donation.html", donation=donation)

# Add Order_Seeds form


@app.route("/order_seeds", methods=["GET", "POST"])
def order_seeds():
    if request.method == "POST":
        order_seeds = {
            "username": session["user"],
            "fullname": request.form.get("fullname"),
            "address": request.form.get("address"),
            "quantity": request.form.get("quantity"),
            "date_ordered": date.strftime("%d %b %Y"),
        }
        mongo.db.order_seeds.insert_one(order_seeds)
        flash("Your Seeds Have Been Ordered!")
        return redirect(url_for("marketplace"))

    order_seeds = mongo.db.order_seeds.find().sort("seed_name", 1)
    return render_template("order_seeds.html", order_seeds=order_seeds)

# 404 error page
@app.errorhandler(404)
def page_not_found(e):
    """
    Renders a custom 404 error page with a button
    that takes the user back to the home page.
    """
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
