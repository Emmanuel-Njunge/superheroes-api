### app.py
from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import db, Hero, Power, HeroPower

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///superheroes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
Migrate(app, db)

@app.route('/')
def home():
    return jsonify({'message': 'Welcome to the Superheroes API!'}), 200


@app.route("/heroes", methods=["GET"])
def get_heroes():
    heroes = [hero.to_dict(rules=("-hero_powers.hero",)) for hero in Hero.query.all()]
    return jsonify(heroes), 200

@app.route("/heroes/<int:id>", methods=["GET"])
def get_hero_by_id(id):
    hero = Hero.query.get(id)
    if hero:
        return jsonify(hero.to_dict()), 200
    return jsonify({"error": "Hero not found"}), 404

@app.route("/powers", methods=["GET"])
def get_powers():
    powers = [power.to_dict() for power in Power.query.all()]
    return jsonify(powers), 200

@app.route("/powers/<int:id>", methods=["GET"])
def get_power_by_id(id):
    power = Power.query.get(id)
    if power:
        return jsonify(power.to_dict()), 200
    return jsonify({"error": "Power not found"}), 404

@app.route("/powers/<int:id>", methods=["PATCH"])
def update_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404

    data = request.get_json()
    description = data.get("description")

    if not description or len(description) < 20:
        return jsonify({"errors": ["validation errors"]}), 400

    power.description = description
    db.session.commit()
    return jsonify(power.to_dict()), 200

@app.route("/hero_powers", methods=["POST"])
def create_hero_power():
    data = request.get_json()
    strength = data.get("strength")
    power_id = data.get("power_id")
    hero_id = data.get("hero_id")

    if strength not in ["Strong", "Weak", "Average"]:
        return jsonify({"errors": ["validation errors"]}), 400

    hero = Hero.query.get(hero_id)
    power = Power.query.get(power_id)

    if not hero or not power:
        return jsonify({"errors": ["Hero or Power not found"]}), 400

    hero_power = HeroPower(strength=strength, hero=hero, power=power)
    db.session.add(hero_power)
    db.session.commit()

    return jsonify(hero.to_dict()), 201

if __name__ == '__main__':
    app.run(port=5555, debug=True)