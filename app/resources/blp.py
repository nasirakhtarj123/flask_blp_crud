from flask import Blueprint, jsonify, request
from flask.views import MethodView
from app.models.persons import Persons
from app import db

blp = Blueprint('api', __name__)

@blp.route('/humans')
class PeopleAPI(MethodView):
    def get(self):
        persons = Persons.query.all()
        result = [{'id': person.id, 'name': person.name, 'age': person.age} for person in persons]
        return jsonify(result)

    def post(self):
        data = request.json
        new_person = Persons(name=data['name'], age=data['age'])
        db.session.add(new_person)
        db.session.commit()
        return jsonify({'id': new_person.id, 'name': new_person.name, 'age': new_person.age}), 201

@blp.route('/humans/<int:person_id>')
class PersonAPI(MethodView):
    def get(self, person_id):
        person = Persons.query.get(person_id)
        if person:
            return jsonify({'id': person.id, 'name': person.name, 'age': person.age})
        return jsonify({"message": "person not found"}), 404

    def put(self, person_id):
        person = Persons.query.get(person_id)
        if person:
            data = request.json
            person.name = data['name']
            person.age = data['age']
            db.session.commit()
            return jsonify({'id': person.id, 'name': person.name, 'age': person.age})
        return jsonify({"message": "person not found"}), 404

    def delete(self, person_id):
        person = Persons.query.get(person_id)
        if person:
            db.session.delete(person)
            db.session.commit()
            return jsonify({"message": "Person deleted successfully"}), 200
        return jsonify({"message": "person not found"}), 404
