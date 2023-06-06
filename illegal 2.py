from flask import Flask
from faker import Faker
#import os
#import system
#import pyttxt3
#from itertools import cycle
#import random
#import sys

#import pygame
#from pygame.locals import *

ap =dir( Flask)
print (ap)
app = Flask(__name__)
f = Faker()
print (help(f))

@app.route("/")
def hello_world():
    return "Hello, World!"
    
print (help("modules"))
print ('\n',help('keywords'))
def add_url_rule():
    return 'past url '    
app.run(debug = True)