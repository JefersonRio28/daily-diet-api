from flask import Flask, request, jsonify
from database import db
from models.meal import Meal

app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)

@app.route("/meal", methods=['POST'])
def insert_meal():
    data=request.json
    meal_name=data.get("name")
    meal_description=data.get("description")
    meal_time=data.get("time")
    meal_indicator=data.get("indicator")

    if meal_name and meal_description and meal_time and meal_indicator is not None:
        meal = Meal(name=meal_name, description=meal_description, time=meal_time, indicator=meal_indicator)
        db.session.add(meal)
        db.session.commit()
        return jsonify({"message": "Meal successfully inserted!"})
    
    return jsonify({"message": "Invalid data"}), 400

if __name__ == '__main__':
    app.run(debug=True)