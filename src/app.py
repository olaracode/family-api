"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def handle_all_members():
    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = {
            "hello": "GET all members response :)",
            "family": members
        }

    return jsonify(response_body), 200


@app.route('/members/<int:id>', methods=['GET', 'POST', 'DELETE'])
def handle_member(id=None):
    if request.method == 'GET':
    # this is how you can use the Family datastructure by calling its methods
        if id == None:
            family = jackson_family.get_all_members()
            return jsonify(family), 200
        if id:
            member = jackson_family.get_member(id)
            return jsonify(member), 200

    if request.method == 'POST':
        first_name = request.json.get("first_name")
        last_name = "Jackson"
        age = request.json.get("age")
        lucky_numbers = request.json.get("lucky_numbers")
        id = request.json.get("id")
        
        if not first_name:
            return jsonify({"msg": "first_name is required"}), 400
        if not age:
            return jsonify({"msg": "age is required"}), 400
        if not lucky_numbers:
            return jsonify({"msg": "lucky_numbers is required"}), 400
        
        member={
            "first_name": first_name,
            "age": age,
            "lucky_numbers": lucky_numbers,
            "id": id
        }
        jackson_family.add_member(member)
        return jsonify({"msg":"Member created successfully"}), 200


    if request.method == 'DELETE':
        member = jackson_family.get_member(id)
        if not member:
            return jsonify({"msg": "Member not found"}), 404
        else:
            jackson_family.delete_member(id)
            return jsonify({"done": True}), 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)