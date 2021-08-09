import os
from flask import (
    Flask, flash, render_template,
    redirect, request, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)

"""
route for home page
"""


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", page_title="Home")


"""route to all plants in database
"""


@app.route('/all_plants')
def all_plants():
    plants = mongo.db.plants.find()

    return render_template(
        'all_plants.html', plants=plants)


"""route to display plant"""


@app.route('/display_plant/<plant_id>')
def display_plant(plant_id):
    plant = mongo.db.plants.find_one_or_404(
        {"_id":ObjectId(plant_id)})
    return render_template('display_plant.html', plant=plant)


"""Route to add plant page"""


@app.route("/add_plant", methods=["GET", "POST"])
def add_plant():
    if request.method == "POST":
        plant = {
            "category_name": request.form.get("category_name"),
            "plant_name": request.form.get("plant_name"),
            "plant_img": request.form.get("plant_img"),
            "plant_description": request.form.get("plant_description"),
            "plant_place": request.form.get("plant_place"),
            "plant_tips": request.form.get("plant_tips"),
            "plant_more_info": request.form.get("plant_more_info"),
            "plant_notes": request.form.get("plant_notes")
        }

        mongo.db.plants.insert_one(plant)
        flash("Plant Successfully Added.")
        return redirect(url_for("index"))
    categories = mongo.db.categories.find().sort("category_name", 1)
    places = mongo.db.places.find().sort("plant_places", 1)
    return render_template(
        "add_plant.html", categories=categories, places=places)


""" This route is for edit plant
old data will be updated by new
"""


@app.route("/edit_plant/<plant_id>", methods=["GET", "POST"])
def edit_plant(plant_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "plant_name": request.form.get("plant_name"),
            "plant_img": request.form.get("plant_img"),
            "plant_description": request.form.get("plant_description"),
            "plant_place": request.form.get("plant_place"),
            "plant_tips": request.form.get("plant_tips"),
            "plant_more_info": request.form.get("plant_more_info"),
            "plant_notes": request.form.get("plant_notes")
        }

        mongo.db.plants.update({"_id": ObjectId(plant_id)}, submit)
        flash("Plant Successfully Updated.")

    plant = mongo.db.plants.find_one({"_id": ObjectId(plant_id)})

    categories = mongo.db.categories.find().sort("category_name", 1)
    places = mongo.db.places.find().sort("plant_places", 1)
    return render_template(
        "edit_plant.html", categories=categories, plant=plant, places=places)


"""
This is route to delete a single plant from database
"""


@app.route("/delete_plant/<plant_id>")
def delete_plant(plant_id):
    mongo.db.plant.remove({"_id": ObjectId(plant_id)})
    flash("Plant Successfully Removed.")
    return redirect(url_for("index"))


"""error page 404"""


@app.errorhandler(404)
def page_not_found(error):

    return render_template("404.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
