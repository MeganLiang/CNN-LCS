import numpy as np

text_file = open("filtered/donut_filtered.txt", "r")
lines = text_file.readlines()

new_arr = []
processed = []

keep = []
for i in range(len(lines)):
    same = []

    line = lines[i].split(',')
    filter = line[0].split('/')[0]
    name = line[0].split('/')[1]

    for j in range(i, len(lines)):

        line1 = lines[j].split(',')
        filter1 = line1[0].split('/')[0]
        name1 = line1[0].split('/')[1]

        if name not in processed:
            if name == name1:
                same.append(line1)
    processed.append(name)
    if len(same) != 0:

        keep_threshold = 1000
        index_keep = -1
        for x in range(len(same)):
            least_classes = same[x][1:]

            least_classes = list(map(int, least_classes))
            print(least_classes)
            cl = least_classes.count(0)

            # if there are lots of 0 and 3
            if cl < keep_threshold:
                keep_threshold = cl

                index_keep = x
        # new_arr.append(same)
        if index_keep != -1:
            # print(index_keep)
            keep.append(same[index_keep])


with open('fork_filtered.txt', 'w') as f:
    for item in keep:
        f.write("%s\n" % item)