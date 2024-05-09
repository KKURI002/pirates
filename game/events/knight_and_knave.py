'''Player and Crew meet the spirit of a knight and a knave'''
from game import event
from game.player import Player
from game.context import Context
import game.config as config
import random

class KnightAndKnave (Context, event.Event):
    def __init__ (self):
        super().__init__()
        self.the_left = "knight"
        self.the_right = "knave"
        self.knight_and_knave = 1
        #self.verbs['chase'] = self
        #self.verbs['feed'] = self
        #self.verbs['help'] = self
        self.verbs["guess"] = self
        self.verbs["leave"] = self
        self.verbs["the knight is on the left"] = self
        self.verbs["the knave is on the left"] = self
        self.verbs["the knave is on the right"] = self
        self.verbs["the knight is on the right"] = self
        self.result = {}
        self.go = False

    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "guess"):
            self.go = False
            self.result["message"] = "who is the knight and who is the knave?\nif you guess right you may pass, if you guess wrong we will attack"
            if (verb == "the knight is on the left") or (verb == "the knave is on the right"):
                if(verb == "the knight is on the left"):
                    self.result["message"] = "you guessed the knight correct"
                if(verb == "the knave is on the right"):
                    self.result["message"] = "you guessed the knave correct"
            elif (verb == "the knight is on the right") or (verb == "the knave is on the left"):
                if(verb == "the knight is on the right"):
                    self.result["mesage"] = "you guessed wrong"
                    #
                if (verb == "the knave is on the left"):
                    self.result["message"] = "you guessed wrong"
                    #
        elif (verb == "leave"):
            self.go = True
            self.result["message"] = "you turn around and go back to the beach"

            ''''r = random.randint(1,10)
            if (r < 5):
                self.result["message"] = "the seagulls fly off."
                if (self.seagulls > 1):
                    self.seagulls = self.seagulls - 1
            else:
                c = random.choice(config.the_player.get_pirates())
                if (c.isLucky() == True):
                    self.result["message"] = "luckly, the seagulls fly off."
                else:
                    self.result["message"] = c.get_name() + " is attacked by the seagulls."
                    if (c.inflict_damage (self.seagulls, "Pecked to death by seagulls")):
                        self.result["message"] = ".. " + c.get_name() + " is pecked to death by the seagulls!"

        elif (verb == "feed"):
            self.seagulls = self.seagulls + 1
            self.result["newevents"].append (KnightAndKnave())
            self.result["message"] = "the seagulls are happy"
            self.go = True
        elif (verb == "help"):
            print ("the seagulls will pester you until you feed them or chase them off")
            self.go = False
        else:
            print ("it seems the only options here are to feed or chase")
            self.go = False'''



    def process (self, world):

        self.go = False
        self.result = {}
        self.result["newevents"] = [ self ]
        self.result["message"] = "default message"

        while (self.go == False):
            print (str (self.knight_and_knave) + " you see two people, what do you want to do?")
            Player.get_interaction ([self])

        return self.result