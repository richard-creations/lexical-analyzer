from os import listdir, path, walk
from os.path import isfile, join, splitext
from glob import glob
import subprocess

def go():
    onlyfiles = [y for x in walk("./samples")
                 for y in glob(path.join(x[0], '*.out'))]
    for file in onlyfiles:
        filename, file_extension = path.splitext(file)
        name = filename.split("/")
        output = name[len(name) - 1]
        cmd = "dcc < ./samples/"+output+".out > ./result/"+output+".out"
        subprocess.Popen(cmd, shell=True)
