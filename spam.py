import re

def isSpam(msg):
    return re.search("http:", msg)
