import glob
import os
import Prof_to_csv

path = os.path.dirname(os.path.abspath(__file__))
os.chdir(path)


files = glob.glob(path + "/*.prof")

for filename in files:
    filename = filename.replace(path, "")
    Prof_to_csv.Function(filename.replace("\\", ""))