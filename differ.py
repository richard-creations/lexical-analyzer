def differ():
    onlyfiles = [y for x in walk("./samples")
                 for y in glob(path.join(x[0], '*.frag'))]
    for file in onlyfiles:
        filename, file_extension = path.splitext(file)
        name = filename.split("/")
        output = name[len(name) - 1]
        cmd = "diff < ./samples/"+output+".frag  ./result/"+output+".out > ./diffs/"+output+".diff"
        subprocess.Popen(cmd, shell=True)

differ()
