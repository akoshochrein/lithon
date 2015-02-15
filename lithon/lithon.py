
import os
import sys


markdown_lines = []
python_lines = []


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
            if not line[:2] == '#&' and not line == '\n':
                # Python part
                python_lines.append(line)

                # Markdown part
                if not python_section:
                    markdown_lines.append('```Python\n')
                    python_section = True
                markdown_lines.append(line)
            else:
                if python_section:
                    markdown_lines.append('```\n')
                    python_section = False
                markdown_lines.append(line[3:])

        if python_section:
            markdown_lines.append('```\n')


def write_python_file(filename):

    def generate_python_filename(filename):
        return os.path.splitext(filename)[0] + '.py'

    with open(generate_python_filename(filename), 'w') as f:
        for line in python_lines:
            f.write(line)

    print 'python file generated'


def write_markdown_file(filename):

    def generate_markdown_filename(filename):
        return os.path.splitext(filename)[0] + '.md'

    with open(generate_markdown_filename(filename), 'w') as f:
        for line in markdown_lines:
            f.write(line)

    print 'markdown file generated'


if __name__ == '__main__':
    main()
