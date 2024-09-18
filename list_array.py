"""Array Based List"""

#Imports
from copy import deepcopy

class List:
    #Initialised List
    def __init__(self):
        self._values= []

    #Returns value at nth term
    def __getitem__(self, i):
        value= deepcopy(self._values[i])
        return value

    def __len__(self):
        length= len(self._values)
        return length

    def __setitem__(self, i, value):
        self._values[i]= deepcopy(value)

    def __contains__(self, key):

        valid= False
        i= 0
        while i < len(self._values) :
            if self._values[i] == key:
                valid= True
                i+=1
        return valid

    def _linear_search(self, key):
        i = 0
        while i < len(self._values) and self._values[i] != key:
            i+=1
        else:
            i= -1
        return i

    def append(self, value):
        self._values.append(deepcopy(value))
        return None

    def count(self, key):
        number = 0
        i = 0
        n = len(self._values)

        while i < n:
            x = deepcopy(self._values[i])
            if x == key:
                number += 1
            i += 1
        return number







