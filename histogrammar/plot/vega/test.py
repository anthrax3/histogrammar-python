#basic script that uses Bin primitive to fill data in histogram primitive and exports the result in json

import histogrammar as hg
import json
# generate a stream of uniform random numbers
import random
# The data of interest (value) is buried within some unweildy object (DataPoint)
data = [random.random() for i in range(2000)]

# add some "bad" values into the dataset
data.extend([float('nan'), float('inf'), float("-inf"), 100, -100])
h = hg.Bin(num=20, low=0, high=1, quantity=lambda x: x, value=hg.Count())
for d in data:
    h.fill(d)

# histogrammar has kept track of these
print ("NaN counter:       ", histogram.nanflow)
print ("overflow counter:  ", histogram.overflow)
print ("underflow counter: ", histogram.underflow)




test_file=open("test.json",'w')

#stores data in json format
testdata = json.dumps(h.toJson(),indent=4)

print(testdata)

test_file.close()

