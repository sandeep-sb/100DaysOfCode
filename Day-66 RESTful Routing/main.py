from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

API_KEY = "TopSecretKey"

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


#  Converting database to dict before serializing it to JSON
def to_dict(self):
    return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random")
def get_random_cafe():
    cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(cafes)
    # return jsonify(cafe={
    #     'name': random_cafe.name,
    #     'id': random_cafe.id,
    #     'map_url': random_cafe.map_url,
    #     'img_url': random_cafe.img_url,
    #     'location': random_cafe.location,
    #     'seats': random_cafe.seats,
    #     'coffee_price': random_cafe.coffee_price,
    #     'amenities': {
    #         'has_toilet': random_cafe.has_toilet,
    #         'has_wifi': random_cafe.has_wifi,
    #         'has_sockets': random_cafe.has_sockets,
    #         'can_take_calls': random_cafe.can_take_calls,
    #     }
    #
    # })

    # Simply convert the random_cafe data record to a dictionary of key-value pairs.
    return jsonify(cafe=to_dict(random_cafe))


# Find all the cafes in the database
@app.route("/all")
def get_all_cafes():
    cafes = db.session.query(Cafe).all()
    return jsonify(cafes=[to_dict(cafe) for cafe in cafes])


# Search for a cafe by its location
@app.route("/search")
def search():
    query_location = request.args.get("loc")
    cafes = Cafe.query.filter_by(location=query_location).all()
    if cafes:
        return jsonify(cafe=[to_dict(cafe) for cafe in cafes])
    else:
        return jsonify(error={
            "Not found": "Sorry, we don't have a cafe at that location."
        })


# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        seats=request.form.get("seats"),
        has_toilet=bool(request.form.get("has_toilet")),
        has_wifi=bool(request.form.get("has_wifi")),
        has_sockets=bool(request.form.get("has_sockets")),
        can_take_calls=bool(request.form.get("can_take_calls")),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe = Cafe.query.get(cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(cafe={"success": "Successfully updated the price."})
    else:
        # Sent 404 to make sure that updating the price is not successful.
        return jsonify(cafe={"Not Found": "Sorry a cafe with that ID was not found in the database."}), 404


# HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def cafe_closed(cafe_id):
    cafe = Cafe.query.get(cafe_id)
    if cafe:
        api_key = request.args.get("api_key")
        # checks for API key
        if not api_key or api_key != API_KEY:
            return jsonify({"error": "Sorry, that's not allowed. Make sure you have the correct api key."}), 403
        db.session.delete(cafe)
        db.session.commit()
        return jsonify(cafe={"Success": "Successfully deleted the cafe"})
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that ID was not found in the database."}), 404


if __name__ == '__main__':
    app.run(debug=True)
