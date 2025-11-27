# enigma/plugboard.py

import re

class Plugboard:
    def __init__(self, connections):
        self.wiring = self.decodePlugboard(connections)
    
    def getWiring(self):
        return self.wiring
    
    def decodePlugboard(self, connections):
        if connections is None or connections == "":
            return self.identityPlugboard()

        pairings = re.split("[^a-zA-Z]", connections)
        mapping = self.identityPlugboard()
        pluggedChars = []

        if len(pairings) >= 13:
            print("Too Many Plugboard Wires!!!")
            return self.identityPlugboard()

        for pair in pairings:
            if len(pair) != 2:
                return self.identityPlugboard()
            
            c1 = ord(str(pair[0]).upper()) - 65
            c2 = ord(str(pair[1]).upper()) - 65

            if c1 in pluggedChars or c2 in pluggedChars:
                return self.identityPlugboard()
            
            pluggedChars.append(c1)
            pluggedChars.append(c2)

            mapping[c1] = c2
            mapping[c2] = c1
        
        return mapping
    
    def identityPlugboard(self):
        mapping = []
        for i in range(26):
            mapping.append(i)
        return mapping

    def getUnpluggedChars(self, connections):
        unpluggedChars = []
        for i in range(26):
            unpluggedChars.append(i)

        if "" in connections:
            return unpluggedChars
        
        pairings = re.split("[^a-zA-Z]", connections)

        for pair in pairings:
            c1 = ord(str(pair[0]).upper()) - 65
            c2 = ord(str(pair[1]).upper()) - 65
        
            unpluggedChars.remove(c1)
            unpluggedChars.remove(c2)
        
        return unpluggedChars
    
    def forward(self, c):
        return chr((self.wiring[ord(c.upper()) - 65]) + 65)


def createPlugboard(connections):    
    return Plugboard(connections)
