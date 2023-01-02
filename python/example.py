import os
d = '/Users/xxxxx/Documents'
filename = 'example-Documents.txt'
subdirs = [os.path.join(d, o) for o in os.listdir(d) if os.path.isdir(os.path.join(d,o))]


# print(subdirs)

f = open(filename, "w")
for dirs in subdirs:
    f.write(dirs)
    f.write("\n")
f.close()

#open and read the file after the appending:
f = open(filename, "r")
print(f.read())