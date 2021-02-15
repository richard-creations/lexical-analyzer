from os import listdir, path, walk
from os.path import isfile, join, splitext
from glob import glob
import subprocess


def run():
    onlyfiles = [y for x in walk("./samples")
                 for y in glob(path.join(x[0], '*.frag'))]
    for file in onlyfiles:
        filename, file_extension = path.splitext(file)
        name = filename.split("/")
        output = name[len(name) - 1]
        cmd = f"dcc < samples/{output}.frag > /solutions/"+output+".out"
        subprocess.run(cmd, shell=True)
        #proc = subprocess.run(cmd, shell=True)



run()
