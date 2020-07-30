import argparse
from itertools import permutations

parser = argparse.ArgumentParser()
parser.add_argument("-r", "--requestpath", help="Provide request endpoint here", type=str, required=True)
args = parser.parse_args()
request_path = str(args.requestpath)

if '?' in request_path:
    ignore = request_path.index('?')
    request_ignore = request_path[:ignore].strip()
    version = request_ignore.split("/")
    probable_path = request_ignore.split("/")
else:
    request_path = request_path.strip()
    version = request_path.split("/")
    probable_path = request_path.split("/")

if probable_path[0].startswith("v"):
    probable_path.pop(0)

for i in range(len(probable_path), -1, -1):
    for path in permutations(probable_path, i):
        if version[0].startswith("v") and len(path) >= 1:
            print(version[0] + '/' + '/'.join(path))
        else:
            print('/'.join(path))
