import argparse

parser = argparse.ArgumentParser()

parser.add_argument(dest="dst",action="store")
parser.add_argument("--qp",dest="qp",action="store")
parser.add_argument("--configure",dest="configure",action="store")
args = parser.parse_args()

print(f"args.dst = {args.dst}")
print(f"args.qp = {args.qp}")
print(f"args.configure = {args.configure}")