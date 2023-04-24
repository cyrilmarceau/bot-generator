import os
import sys

class BotLocation:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        print('BotLocation: x = {}, y = {}'.format(self.x, self.y))
        

    def get_location(self):
        return {'x': self.x, 'y': self.y}

# INSTANCIATION
bot = BotLocation(10, 20)

# GET LOCATION
bot.get_location()