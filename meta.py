import argparse
from datetime import datetime
import json
import os

parser = argparse.ArgumentParser()
parser.add_argument("action")
parser.add_argument("day")
args = parser.parse_args()

now = datetime.now()
output = json.dumps({'timestamp': now.timestamp(), 'date': now.isoformat()})

currday = args.day.zfill(1)
dirpath = os.path.relpath(currday)

if not os.path.exists(dirpath):
	os.mkdir(dirpath, 0o755)

filePath = os.path.join(dirpath, '{0}.{1}'.format(currday, args.action))
try:
	with open(filePath, 'x') as f:
		f.write(output)

		print("Wrote {0}".format(filePath))
		print("Now you'll want to:")
		print("\tgit add {0}".format(currday))
		print('\tgit commit -m "{0} day {1}"'.format(args.action, currday))
		print('\tgit push')

except (FileExistsError) as e:
	print("Whoops, that file exists! No cheating!")
