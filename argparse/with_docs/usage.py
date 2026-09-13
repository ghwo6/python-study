# 이해 못함

import argparse

# ghwo61351@c6r3s6 python-study % /usr/local/bin/python3.12 /Users/ghwo61351/tasks_ghwo6/python-study/argparse/
# with_docs/description.py
# usage: PROG [-h] [--foo [FOO]] bar [bar ...]
# PROG: error: the following arguments are required: bar

# usage를 사용하면 

# ghwo61351@c6r3s6 python-study % /usr/local/bin/python3.12 /Users/ghwo61351/tasks_ghwo6/python-study/argparse/
# with_docs/description.py
# usage: PROG [options]
# PROG: error: the following arguments are required: bar

# 이렇게 나옴

# parser = argparse.ArgumentParser(prog='PROG')
parser = argparse.ArgumentParser(prog='PROG', usage='%(prog)s [options]')
parser.add_argument('--foo', nargs='?', help='foo help')
parser.add_argument('bar', nargs='+', help='bar help')

parser.parse_args()


