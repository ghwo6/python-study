import argparse

parser = argparse.ArgumentParser(description="Process some intergers.")
parser.add_argument("integers",metavar="N",type=int,nargs="+",help="an integer for the accumulator")
parser.add_argument("--sum",dest="accumulate",action="store_const",const=sum,default=max,help="sum the integers (default : find the max)")

args = parser.parse_args()
parser.parse_args(['--sum',7,'-1','42'])
print(args.accumulate(args.integers))

# args = parser.parse_args(['--sum', '7', '-1', '42'])
# print(args)
# print(args.accumulate(args.integers))