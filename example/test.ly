#& # First example lython file
#& ## This function is meant to print hello

def hello():
    print 'Hello'

#& ## It is good to know that you can enter text within the Python code and it will still run.

def world():
#& Exactly like this
    print 'World'


#& ## Goals
#& The goal is to have a markdown file and a python file that runs in the end.

if __name__ == '__main__':
    hello()
    world()
