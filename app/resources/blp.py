from flask import Blueprint, jsonify, request
from app.models.persons import Persons
from app import db

blp = Blueprint('api', __name__)

@blp.route('/humans', methods=['GET', 'POST'])
def people_api():
    if request.method == 'GET':
        persons = Persons.query.all()
        result = [{'id': person.id, 'name': person.name, 'age': person.age} for person in persons]
        return jsonify(result)
    elif request.method == 'POST':
        data = request.json
        new_person = Persons(name=data['name'], age=data['age'])
        db.session.add(new_person)
        db.session.commit()
        return jsonify({'id': new_person.id, 'name': new_person.name, 'age': new_person.age}), 201

@blp.route('/humans/<int:person_id>', methods=['GET', 'PUT', 'DELETE'])
def person_api(person_id):
    person = Persons.query.get(person_id)
    if not person:
        return jsonify({"message": "person not found"}), 404
    
    if request.method == 'GET':
        return jsonify({'id': person.id, 'name': person.name, 'age': person.age})
    elif request.method == 'PUT':
        data = request.json
        person.name = data['name']
        person.age = data['age']
        db.session.commit()
        return jsonify({'id': person.id, 'name': person.name, 'age': person.age})
    elif request.method == 'DELETE':
        db.session.delete(person)
        db.session.commit()
        return jsonify({"message": "Person deleted successfully"}), 200
