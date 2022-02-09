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
        self._members = [{
            'id' : 1,
            'first_name' : 'John',
            'last_name' : self.last_name,
            'age' : '33 Years old',
            'lucky_numbers' : [7,13,22],
        },
        {
            'id' : 2,
            'first_name' : 'Jane',
            'last_name' : self.last_name,
            'age' : '35 Years old',
            'lucky_numbers' : [10,14,3],
        },
        {
            'id' : 3,
            'first_name' : 'Jimmy',
            'last_name' : self.last_name,
            'age' : '5 Years old',
            'lucky_numbers' : [1],
        },
        {
            'id' : 4,
            'first_name' : 'Raul',
            'last_name' : self.last_name,
            'age' : '9 Years old',
            'lucky_numbers' : [9,10,11,12],
        },
        {
            'id' : 5,
            'first_name' : 'Marcelo',
            'last_name' : self.last_name,
            'age' : '1 Years old',
            'lucky_numbers' : [13,14,15,16],
        },
        {
            'id' : 6,
            'first_name' : 'Loreto',
            'last_name' : self.last_name,
            'age' : '19 Years old',
            'lucky_numbers' : [3,4,5,6],
        },
        {
            'id' : 7,
            'first_name' : 'Isabel',
            'last_name' : self.last_name,
            'age' : '5 Years old',
            'lucky_numbers' : [3,4,5,6],
        }]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        if member['id'] is None: member["id"]=self._generateId() 
        member["last_name"] = self.last_name
        self._members.append(member)
        return member

    def delete_member(self, id):
        for position in range(len(self._members)):
            if self._members[position]["id"] == id:
                self._members.pop(position)
                return self._members

    def get_member(self, id):
        filtered_member = list(filter(lambda member: member["id"] == id, self._members))
        return filtered_member[0]

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members