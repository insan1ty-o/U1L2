import matplotlib.pyplot as plt
import numpy as np

def plot(data1, data2, data3):
  for dataset in [data1, data2, data3]:
    plt.plot(dataset)
    plt.title('Breeding rats to 50,000lbs')
    plt.xlabel('Generations')
    plt.ylabel('Weight')
    plt.legend(["MAX", "MIN", "AVG"])
    plt.show()
    plt.savefig('rat_graph.png')

#file addition----------------------
with open("largest_rat.txt", "r") as openFile:
  MAX = openFile.read()
  MAX = MAX.split(", ")
with open("smallest_rat.txt", "r") as openFile:
  MIN = openFile.read()
  MIN = MIN.split(", ")
with open("average_generation.txt", "r") as openFile:
  AVG = openFile.read()
  AVG = AVG.split(" ")

for i in AVG:
  if i == '':
    AVG.remove(i)

MAX.remove(MAX[-1])
MIN.remove(MIN[-1])
AVG.remove(AVG[-1])

for i in range(len(MAX)):
  MAX[i] = int(MAX[i])
for i in range(len(MIN)):
  MIN[i] = int(MIN[i])
for i in range(len(AVG)):
  AVG[i] = int(AVG[i])
#-----------------------------------

graph = plot(MAX, MIN, AVG)
plt.show()
