from game import event
from game.player import Player
from game.context import Context
import game.config as config
import random

class Shark (Context, event.Event):
    '''Encounter with a shark. Uses the parser to decide what to do about it.'''
    def __init__ (self):
        super().__init__()
        self.name = "shark visitor"
        self.shark = 1
        self.verbs['kill'] = self
        self.verbs['feed'] = self
        self.verbs['follow'] = self
        self.result = {}
        self.go = False

    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "kill"):
            self.go = True
            r = random.randint(1,10)
            if (r < 5):
                self.result["message"] = "the shark is killed."
                if (self.shark > 1):
                    self.shark = self.shark - 1
            else:
                c = random.choice(config.the_player.get_pirates())
                if (c.isLucky() == True):
                    self.result["message"] = "luckily, the shark swims off."
                else:
                    self.result["message"] = c.get_name() + " is attacked by the shark."
                    if (c.inflict_damage (self.shark, "Bitten to death by the shark")):
                        self.result["message"] = ".. " + c.get_name() + " is bitten to death by the shark!"

        elif (verb == "feed"):
            self.shark = self.shark + 1
            self.result["newevents"].append (Shark())
            self.result["message"] = "the sharks are happy"
            self.go = True
        elif (verb == "follow"):
            print ("the shark leads you too a school of fish")
            self.go = True
            if (verb == 'feed'):
                self.result["message"] = 'the shark is happy and leaves you alone'
            elif (verb == 'kill'):
                self.go = True
                r = random.randint(1,10)
                if (r < 5):
                    self.result["message"] = "the shark is killed."
                    if (self.shark > 1):
                        self.shark = self.shark - 1
                else:
                    c = random.choice(config.the_player.get_pirates())
                    if (c.isLucky() == True):
                        self.result["message"] = "luckily, the shark swims off."
                    else:
                        self.result["message"] = c.get_name() + " is attacked by the shark."
                        if (c.inflict_damage (self.shark, "Bitten to death by the shark")):
                            self.result["message"] = ".. " + c.get_name() + " is bitten to death by the shark!"
                self.result["message"] = 'the fish are gone'
        else:
            print ("it seems the only options here are to kill, feed, or follow.")
            self.go = False



    def process (self, world):

        self.go = False
        self.result = {}
        self.result["newevents"] = [ self ]
        self.result["message"] = "default message"

        while (self.go == False):
            print (str (self.shark) + " a shark has appeared what do you want to do?")
            Player.get_interaction ([self])

        return self.result
