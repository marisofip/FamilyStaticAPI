
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = []

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        pass

    def delete_member(self, id):
        # fill this method and update the return
        pass

    def get_member(self, id):
        # fill this method and update the return
        pass

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
from random import randint

class FamilyStructure:
    
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = []
        self._members.append({
            "id": self._generateId(),
            "name": "John",
            "age": 33,
            "lucky_numbers": [7, 13, 22]
        })
        self._members.append({
            "id": self._generateId(),
            "name": "Jane",
            "age": 35,
            "lucky_numbers": [10, 14, 3]
        })
        self._members.append({
            "id": self._generateId(),
            "name": "Jimmy",
            "age": 5,
            "lucky_numbers": [1]
        })

    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member: dict):
        try:
            first_name = member["first_name"]
            id = member["id"]
            age = member["age"]
            lucky_numbers = member["lucky_numbers"]
        except KeyError as e:
            raise ValueError(f"Missing {e}")
        new_member = {
            "id": id,
            "first_name": first_name,
            "age": age,
            "lucky_numbers": lucky_numbers
        }
        self._members.append(new_member)
        return new_member

    def delete_member(self, id):
        for i, member in enumerate(self._members):
            if member["id"] == id:
                deleted_member = self._members[i]
                del self._members[i]
                return deleted_member
        return None

    def update_member(self, name, id, age, lucky_numbers):
        for i, member in enumerate(self._members):
            if member["id"] == id:
                member["name"] = name
                member["age"] = age
                member["lucky_numbers"] = lucky_numbers

                break

    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return member
        return None

    def get_all_members(self):
        return self._members