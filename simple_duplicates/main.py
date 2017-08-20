import sys
import pickle
import argparse
import os


def parse_files(ds, args):
    for fn in sys.stdin:
        print (fn)


def parse_directory(ds, args):
    print ("Not implemented")


if (__name__ == '__main__'):

    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--type", help="Parsing files (f) or directories (d)", type=str, required=True)
    parser.add_argument("-d", "--dest", help="Destination for the object type", type=str)

    args = parser.parse_args()

    print("Type: ", args.type)
    print("Dest: ", args.dest)

    # Read the data structure (if it exists)
    if (args.dest is not None):
        if os.path.exists(args.dest):
            print ("Loading data structure")

            with open(args.dest) as infile:
                ds = pickle.load(infile)
        else:
            print ("Creating data structure")
            ds = {}
            with open(args.dest, "w") as outfile:
                pickle.dump(ds, outfile, -1)

    if (args.type == "d"):
        parse_directory(ds, args)
    if (args.type == "f"):
        parse_files(ds, args)
