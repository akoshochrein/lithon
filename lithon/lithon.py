
import os
import random
import re
import sys

from ordereddict import OrderedDict

markdown_lines = OrderedDict()
python_lines = OrderedDict()

VARIABLE_RE = re.compile(r'^{{(.+)}}$')
VARIABLE_EXPAND_RE = re.compile(r'^{{(.+)}} \+\=$')
RANDOM_SIZE = 1000000


def main():
    args = sys.argv
    if len(args) < 2:
        return 1
    else:
        filename = args[1]
        process_file(filename)
        write_python_file(filename)
        write_markdown_file(filename)


def process_file(filename):
    with open(filename, 'r') as f:
        python_section = False
        for line in f.readlines():
            match_var = VARIABLE_RE.match(line)
            match_exp_var = VARIABLE_EXPAND_RE.match(line)

            # add a random seed to the lines so they will not collide on hashing
            key = hash(line + str(int(random.random()*RANDOM_SIZE)))

            if match_var:
                # register the variable in the python lines
                key = match_var.group(1)
                python_lines[key] = ''
            elif match_exp_var:
                # Expand is caught, we shall read the input until a new markdown is started
                variable_insert = True
                variable = match_exp_var.group(1)
            elif not line[:2] == '#&' and not line == '\n':

                # Python part
                if variable_insert:
                    python_lines[variable] += line
                else:
                    python_lines[key] = line

                # Markdown part
                if not python_section:
                    section_start_key = hash(str(key) + 'pybegin')
                    markdown_lines[section_start_key] = '```Python\n'
                    python_section = True

                markdown_lines[key] = line
            else:
                variable_insert = False
                if python_section:
                    section_end_key = hash(str(key) + 'pyend')
                    markdown_lines[section_end_key] = '```\n'
                    python_section = False
                markdown_lines[key] = line[3:]

        if python_section:
            markdown_lines[key] = '```\n'


def write_python_file(filename):

    def generate_python_filename(filename):
        return os.path.splitext(filename)[0] + '.py'

    with open(generate_python_filename(filename), 'w') as f:
        for line in python_lines.keys():
            f.write(python_lines[line])

    print 'python file generated'


def write_markdown_file(filename):

    def generate_markdown_filename(filename):
        return os.path.splitext(filename)[0] + '.md'

    with open(generate_markdown_filename(filename), 'w') as f:
        for line in markdown_lines.keys():
            f.write(markdown_lines[line])

    print 'markdown file generated'


if __name__ == '__main__':
    main()
