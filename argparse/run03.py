import argparse

parser = argparse.ArgumentParser()

parser.add_argument(dest="dst",action="store")
parser.add_argument("--qp",dest="qp",action="store",default=1.3)
parser.add_argument("--configure",dest="configure",action="store",default=3)
args = parser.parse_args()

print(f"args.dst = {args.dst}",f"type(args.dst) = {type(args.dst)}")
print(f"args.qp = {args.qp}",f"type(args.qp) ={type(args.qp)}")
print(f"args.configure = {args.configure}",f"type(args.qp) ={type(args.configure)}")