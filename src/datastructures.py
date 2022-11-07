
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint
from flask_sqlalchemy import SQLAlchemy

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [{ #array
           "id": self._generateId(),
           "first_name": "John",
           "last_name": last_name
       }]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return

        if "id" not in member: 
            member["id"] = self._generateId()

        return self._members.append(member)

    def delete_member(self, id):

        for item in range(0, len(self._members)):
            if item == id:
               member.remove(item) 

        return "success"
    
    def update_member(self, id, member):
   
       for i in range(0, len(self._members)):
            if member["id"] == id:
                return self._members.append(member)


    def get_member(self, id):
     
     for member in self._members: 
        if member["id"] == id:
            return member
        return "member not found"

    def get_all_members(self):
        return self._members 