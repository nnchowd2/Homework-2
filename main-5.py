#ID 1591144

import csv

input_file = input()
freq = {}

with open(input_file, 'r') as s:
    readfile = csv.reader(s)
    for row in readfile:
        for word in row:
            if word in freq:
                freq[word] += 1
            else:
                freq[word] = 1

for key in list(freq.keys()):
    print("{} {}".format(key, freq[key]))



