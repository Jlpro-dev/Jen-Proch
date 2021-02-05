# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 15:03:44 2020

@author: jenpr
"""

from introduction import intro
from slowprint import slowdown
"""importing equipment module and inventory to enable a review of the inventory"""
import inventory
import equipment_general
from inventory import printList

"""start the game with introduction"""
print(intro())
"""print inventory list"""
printList()
slowdown("Now we will look at two locations where there have been rumors of trouble.")
input("\n\nPress the enter key to continue")
"""import planets to enable review of planet options"""
import planets
from planets import pickPlanets
"""in future choice of planet will determine next steps. at the moment, you must choose wilderness""" 
pickPlanets()
slowdown("Now to equip you for your mission. You can refer back to the Inventory for your options.")
"""import armory to allow players to choose equipment for missions"""
import armory
from armory import fillBackpack
fillBackpack()
slowdown("Well, now that you are equipped and have your destination ready, we will journey to your first destination.  I wish you luck, Agent.")
"""importing modules for level 1: Planet Wilderness"""
import wilderness
from wilderness import wildIntro
from wilderness import seehowmany
from wilderness import visitForest
from wilderness import wateringHole
from wilderness import marketplace
from wilderness import forest
from ship_class import welcomeback
from tictactoe import tictactoe
"""Start level 1 with introduction and choices"""
wildIntro()
"""interact with villagers in marketplace"""
seehowmany()
"""interact with villagers at Watering Hole"""
wateringHole()
"""travel to new destination in on Planet Wilderness and explore forest"""
visitForest()
"""player must beat minigame to move forward"""
tictactoe()
slowdown("Now that you've decoded the clue, you should head back to your ship as quickly as possible!")
welcomeback()








   
