import datetime
import random
def hello():
    print 'Hello'
def world():
    print 'World'
def time():
    print datetime.datetime.now()
def my_random():
    print int(random.random() * 100)
if __name__ == '__main__':
    hello()
    world()
    time()
