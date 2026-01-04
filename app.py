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
        return jsonify({"message": "Meal successfully inserted!", "id": meal.id})
    
    return jsonify({"message": "Invalid data"}), 400

@app.route("/meal/<int:id_meal>", methods=['PUT'])
def update_meal(id_meal):
    data=request.json
    meal = Meal.query.get(id_meal)

    if meal:
        meal.name=data.get("name")
        meal.description=data.get("description")
        meal.time=data.get("time")
        meal.indicator=data.get("indicator")
        db.session.commit()
        return jsonify({"message": "Meal successfully updated!"})
    
    return jsonify({"message": "Meal not found"}), 404

@app.route("/meal/<int:id_meal>", methods=['DELETE'])
def delete_meal(id_meal):
    meal = Meal.query.get(id_meal)

    if meal:
        db.session.delete(meal)
        db.session.commit()
        return jsonify({"message": "Meal successfully deleted!"})
    
    return jsonify({"message": "Meal not found"}), 404    

@app.route("/meal", methods=['GET'])
def read_meal_list():
    meals = Meal.query.all()
    
    if meals:
        meals_list = []

        for meal in meals:
            meal_data = {
                "id": meal.id,
                "name": meal.name,
                "description": meal.description,
                "time": meal.time,
                "indicator": meal.indicator
            }
            meals_list.append(meal_data)

        return jsonify({"meals": meals_list, "total meals": len(meals_list)})
    
    return jsonify({"message": "The meal list is empty"})

@app.route("/meal/<int:id_meal>", methods=['GET'])
def read_meal(id_meal):
    meal = Meal.query.get(id_meal)

    if meal:
        return jsonify(meal.to_dict())

    return jsonify({"message": "Meal not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)