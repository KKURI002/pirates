from game import event
import random
from game.combat import Combat
from game.combat import Monster
from game.display import announce
import game.config as config
import game.superclasses as superclasses

class Skeleton(Monster):
    def __init__(self, name):
        attacks = {}
        attacks["punch"] = ["punches", random.randrange(35,46), (8,18)]
        attacks["kick"] = ["kicks", random.randrange(35,46), (8,18)]
        super().__init__(name, random.randrange(7,20), attacks, 70 + random.randrange(-20,61))

class KillerSkeletons (event.Event):
    
    def __init__ (self):
        self.name = " monkey attack"

    def process (self, world):
        result = {}
        result["message"] = "the skeletons are defeated!"
        monsters = []
        n_appearing = random.randrange(3,8)
        n = 1
        while n <= n_appearing:
            monsters.append(Skeleton("Killer Skeletons "+str(n)))
            n += 1
        announce ("The crew is attacked by a group of killer skeletons!")
        Combat(monsters).combat()
        if random.randrange(2) == 0:
            result["newevents"] = [ self ]
        else:
            result["newevents"] = [ ]
        config.the_player.ship.food += n_appearing*3

        return result