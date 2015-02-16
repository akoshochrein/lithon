#& # First example lython file

#& Import sections are always in the begining of your file.

{{ imports }}

#& ## This function is meant to print hello

def hello():
    print 'Hello'

#& ## It is good to know that you can enter text within the Python code and it will still run.

def world():
#& Exactly like this
    print 'World'

#& I need a function that can display time for me. I will need some imports for this.

{{ imports }} +=
import datetime

#& Now I can define the function

def time():
    print datetime.datetime.now()

#& If I need another thing imported, it is not too hard.

{{ imports }} +=
import random

#& Using it should work as well

def my_random():
    print int(random.random() * 100)

#& ## Goals
#& The goal is to have a markdown file and a python file that runs in the end.

if __name__ == '__main__':
    hello()
    world()
    time()
