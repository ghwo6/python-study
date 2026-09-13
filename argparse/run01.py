# run01.py
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-d","--decimal",dest="decimal",action="store")
parser.add_argument("-f","--fast",dest="fast",action="store_true")

args = parser.parse_args()

print(args.decimal)
print(args.fast)