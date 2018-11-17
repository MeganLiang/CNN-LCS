import numpy as np
import math as math
import pandas as pd

# data = np.loadtxt('mappings/mapping_forks.txt', delimiter=',', skiprows=1, usecols=range(1,16))
# names = np.loadtxt('mappings/mapping_forks.txt', delimiter=',', skiprows=1, usecols=0, dtype='str')
# print(names)



text_file = open("mapping_mnist.txt", "r")
lines = text_file.readlines()
print(lines)

new_data = []
for j in range(len(lines)):
    data = (lines[j]).split(',')[1:]
    data = list(map(int, data))
    mag_theta = [0, 0]
    # [0, 1,  2, 3,  4,   5, 6, 7, 8, 9, 10,11,12,13,14]
    print(data)  # [3, 56, 6, 69, 128, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    print(len(data))
    for i in range(5, 20, 5):
        x1, y1 = data[i - 4], data[i - 3]
        x2, y2 = data[i + 1], data[i + 2]
        mag = math.hypot((x1 - x2), (y1 - y2))
        if x1 - x2 != 0:
            angle = math.atan((y1 - y2) / (x1 - x2))
        else:
            angle = 0
        # print(mag, angle)
        mag_theta.append(mag)
        mag_theta.append(angle)

    # print(mag_theta)
    mag_theta = np.asarray(mag_theta)
    name = (lines[j]).split(',')[0].split('_')[2]
    print(name)
    new_item = np.concatenate((data, mag_theta, name), axis=None)
    new_data.append(new_item)
print(type(new_data))

#
# new_data = [item for sublist in new_data for item in sublist]
# new_data = list(map(lambda x: x.strip(), new_data))
new_data = np.asarray(new_data)

np.savetxt("mapped2_mnist.arff", new_data, fmt='%s')
# print(len(new_data))
# print(str(new_data[1]))
# with open('mapped2_mnist.arff', 'w') as f:
#     for item in new_data:
#         f.write("%s\n" % item)
