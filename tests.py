import pytest
import requests

BASE_URL = 'http://127.0.0.1:5000'
meals = []

def test_insert_meal():
    new_test_meal_data = {
        "name": "Meal test",
        "description": "Test meal description",
        "time": "DD/MM/YYYY HH:MM",
        "indicator": "Yes" 
    }
    response = requests.post(f"{BASE_URL}/meal", json=new_test_meal_data)
    assert response.status_code == 200
    response_json = response.json()
    assert "message" in response_json
    assert "id" in response_json
    meals.append(response_json['id'])

def test_read_meals_list():
    response = requests.get(f"{BASE_URL}/meal")
    assert response.status_code == 200
    response_json = response.json()
    assert "meals" in response_json
    assert "total meals" in response_json

def test_read_meal():
    if meals:
        meal_id = meals[0]
        response = requests.get(f"{BASE_URL}/meal/{meal_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert meal_id == response_json['id']

def test_update_meal():
    if meals:
        meal_id = meals[0]
        payload = {
        "name": "New meal test",
        "description": "Test meal description updated",
        "time": "DD/MM/YYYY HH:MM",
        "indicator": "Yes" 
        }
        response = requests.put(f"{BASE_URL}/meal/{meal_id}", json=payload)
        assert response.status_code == 200
        response_json = response.json()
        assert "message" in response_json

        #New requisition to test if the name was changed
        response = requests.get(f"{BASE_URL}/meal/{meal_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert response_json['name'] == payload ['name']
        assert response_json['description'] == payload ['description']
        assert response_json['time'] == payload ['time']
        assert response_json['indicator'] == payload ['indicator']

def test_delete_meal():
    if meals:
        meal_id = meals[0]
        response = requests.delete(f"{BASE_URL}/meal/{meal_id}")
        assert response.status_code == 200

        response = requests.delete(f"{BASE_URL}/meal/{meal_id}")
        assert response.status_code == 404