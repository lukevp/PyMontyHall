

import random

class MontyHallState(object):
    def __init__(self):
        self.doors = [False, False, True]
        random.shuffle(self.doors)
        self.chosen = -1
        
    def choose(self, door):
        self.chosen = door
    
    def is_winner(self):
        if (self.chosen < 0 or self.chosen > 2):
            raise Exception
        else:
            return self.doors[self.chosen]
    def switch(self):
        # choose a reveal door and then switch to the last remaining door.
        reveal = random.choice([i for i in range(3) if (i != choice and not self.doors[i])])
        switch = 0
        while switch == choice or switch == reveal: switch += 1
        self.chosen = switch
        
        
switchwins = 0
switchlosses = 0
staywins = 0
staylosses = 0

for i in range(1000):
    state = MontyHallState()
    choice = random.randrange(0,3)
    print "Doors: ", state.doors
    state.choose(choice)
    print "Chosen door: ", state.chosen + 1
    if state.is_winner(): 
        print "Staying won."
        staywins += 1
    else: 
        print "Staying lost."
        staylosses += 1
    state.switch()
    print "Switched door: ", state.chosen + 1
    if state.is_winner():
        print "Switching won."
        switchwins += 1
    else: 
        print "Switching lost."
        switchlosses += 1
    print "----------"
    
print "Staying with first chosen door resulted in ", staywins, " wins and ", staylosses, " losses."
print "Switching to the other door after reveal resulted in ", switchwins, " wins and ", switchlosses, " losses."