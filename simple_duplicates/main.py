import sys
import pickle
import argparse
import os
import csv


def export_csv(ds, filename):

    writer = csv.writer(open(filename, 'wb'))

    for key, value in ds.iteritems():
        ln = [key]
        for ik, iv in value.iteritems():
            ln.append(ik)
            ln.append(iv)
            # ln.extend([v for v in iv])

        writer.writerow(ln)


def save_obj(ds, args):
    with open(args.dest, "w") as outfile:
        pickle.dump(ds, outfile, -1)


def load_obj(args):
    ds = {}
    with open(args.show) as infile:
        ds = pickle.load(infile)
    return ds


def parse_files(ds, args):
    for fn in sys.stdin:
        info = fn.strip().split(" ")
        print (info[0], info[1], info[2])

        # Check name + size
        name = info[1]+info[2]

        # Creating if not existing
        if name not in ds.keys():
            ds[name] = {}
            ds[name]["dup"] = 0
        else:
            ds[name]["dup"] += 1

            # Since it is a dup, we should add a new name
            name = name+"_"+str(ds[name]["dup"])
            ds[name] = {}

        ds[name]["type"] = "f"
        ds[name]["size"] = info[2]
        ds[name]["parent"] = info[0]
    save_obj(ds, args)


def parse_directory(ds, args):
    print ("Not implemented")


if (__name__ == '__main__'):

    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--type", help="Parsing files (f) or directories (d)", type=str, required=True)
    parser.add_argument("-d", "--dest", help="Destination for the object type", type=str)
    parser.add_argument("-c", "--csv", help="Destination for the csv file", type=str)
    parser.add_argument("-s", "--show", help="Simply display the data structure", type=str)

    args = parser.parse_args()

    print("Type: ", args.type)
    print("Dest: ", args.dest)
    print("CSV: ", args.csv)

    if (args.show is not None and os.path.exists(args.show)):
        print ("Opening", args.show)
        print (load_obj(args))

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

    if (args.csv is not None):
        export_csv(ds, args.csv)
