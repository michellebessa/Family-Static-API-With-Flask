from random import randint
from flask_sqlalchemy import SQLAlchemy

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = []

    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):

        if "id" not in member: 
            member["id"] = self._generateId()

        return self._members.append(member)

    def delete_member(self, id):

        for item in range(len(self._members)):
            print(item)

            if self_.members[item]["id"] == id:
                self_.members.pop(item)

    
    def update_member(self, id, member):
   
       for item in self._members:
            if item["id"] == id:
                print(item)
                item = member
                return self._members


    def get_member(self, id):
     
     for member in self._members: 
        if member["id"] == id:
            return member

    def get_all_members(self):
        return self._members 