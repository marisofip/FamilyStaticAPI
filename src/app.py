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

@app.route('/members', methods=['GET'])
def handle_get_all_members():
    members = jackson_family.get_all_members()
    if members:
        return jsonify(members), 200
    else:
        return jsonify({"error": "No members found"}), 404

@app.route('/member/<int:id>', methods=['GET'])
def handle_get_member(id):
    member = jackson_family.get_member(id)

    if member:
        response_member = {
            "first_name": member.get("first_name", ''),
            "id": member.get("id", ''),
            "age": member.get("age", ''),
            "lucky_numbers": member.get("lucky_numbers", [])
        }
        return jsonify(response_member), 200
    else:
        return jsonify({"error": "Member not found"}), 404

@app.route('/member', methods=['POST'])
def handle_add_member():
    member = request.get_json()

    if member:
        return jsonify(jackson_family.add_member(member)), 200    
    else:
        return jsonify({"error": "Could not add member"}), 404

@app.route('/member/<int:id>', methods=['PUT'])
def handle_update_member(id):
    member = request.get_json()
    updated_member = jackson_family.update_member(id, member)

    if member:    
        return jsonify(updated_member), 200
    else:
        return jsonify({"error": "Could not update member"}), 404

@app.route('/member/<int:id>', methods=['DELETE'])
def handle_delete_member(id):
    deleted_member = jackson_family.delete_member(id)
    if deleted_member:
        return jsonify({"done": True, "deleted_member": deleted_member}), 200
    else:
        return jsonify({"error": "Member not found"}), 404


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
