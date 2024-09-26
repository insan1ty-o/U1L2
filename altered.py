# Matthew Fahnestock
# U1 L1
# Breeding rats  to an average weight
from random import triangular, randint, choice, shuffle, uniform, random
from ratclass import Rat
GOAL = 50000                # Target average weight (grams)
NUM_RATS = 20               # Max adult rats in the lab
INITIAL_MIN_WT = 200        # The smallest rat (grams)
INITIAL_MAX_WT = 600        # The chonkiest rat (grams)
INITIAL_MODE_WT = 300       # The most common weight (grams)
MUTATE_ODDS = 0.01          # Liklihood of a mutation
MUTATE_MIN = 0.5            # Scalar mutation - least beneficial
MUTATE_MAX = 1.2            # Scalar mutation - most beneficial
LITTER_SIZE = 8             # Pups per litter (1 mating pair)
GENERATIONS_PER_YEAR = 10   # How many generations are created each year
GENERATION_LIMIT = 500     # Generational cutoff - stop breeded no matter what

def calculate_weight(sex, mother, father):
  '''Generate the weight of a single rat'''
  min = mother.getWeight()
  max = father.getWeight()
  if sex == "M":
    wt = int(triangular(min, max, min))
  else:
    wt = int(triangular(min, max, max))

  return wt

def mutate(pups):
  """Check for mutability, modify weight of affected pups"""
  #MOTHER---
  for rat in pups[0]:
    if random() <= MUTATE_ODDS:
      rat.weight *= uniform(MUTATE_MIN, MUTATE_MAX)
      rat.weight = int(rat.weight)

  #FATHER---
  for rat in pups[1]:
    if random() <= MUTATE_ODDS:
      rat.weight *= uniform(MUTATE_MIN, MUTATE_MAX)
      rat.weight = int(rat.weight)

  return pups  

def initial_population():
  '''Create the initial set of rats based on constants'''
  rats = [[],[]]
  mother = Rat("M", INITIAL_MIN_WT)
  father = Rat("F", INITIAL_MAX_WT)
  for r in range(NUM_RATS):
    if r < 10:
      sex = "M"
      ind = 0
    else:
      sex = "F"
      ind = 1
  
    wt = calculate_weight(sex, mother, father)
    R = Rat(sex, wt)
    rats[ind].append(R)
  return rats

def breed(rats):
  """Create mating pairs, create LITTER_SIZE children per pair"""
  children = [[],[]]
  shuffle(rats[0])
  shuffle(rats[1])
  for r in range(NUM_RATS//2):
    mother = rats[0][r]
    father = rats[1][r]
    mother.litters += 1
    father.litters += 1
    gender = choice(['M','F'])
    
    wt = calculate_weight(gender, mother, father)
    child = Rat(gender, wt)
    
    for i in range(LITTER_SIZE):
      if child.sex == "M" and len(children[0]) + len(children[1]) != 80 or len(children[0]) < 10:
        children[0].append(child)
      elif child.sex == "F" and len(children[0]) + len(children[1]) != 80 or children[1] < 10:
        children[1].append(child)
  return children  

def select(rats, pups):
  '''Choose the largest viable rats for the next round of breeding'''
  min = 0
  max = 0
  largest = 0
  smallest = 0
  temprats = [[],[]]

  for pup in pups[0]:
    rats[0].append(pup)

  for pup in pups[1]:
    rats[1].append(pup)
  
  rats[0].sort(reverse=True)
  rats[1].sort(reverse=True)

  #LARGEST----
  for L_mother in rats[0]:
    if L_mother.weight > largest:
      largest = L_mother.weight

  for L_father in rats[1]:
    if L_father.weight > largest:
      largest = L_father.weight
  #SMALLEST----
  for Sm_mother in rats[0]:
    for rat in range(len(rats[0])):
      if Sm_mother.weight < rats[0][rat].weight:
        smallest = Sm_mother.weight

  for Sm_father in rats[1]:
    for rat in range(len(rats[1])):
      if Sm_father.weight < rats[1][rat].weight:
        smallest = Sm_father.weight

  # MOTHER ------
  for r in rats[0]:
    if r.canBreed() == True and len(temprats[0]) != 10:
        temprats[0].append(r)
    if not r.canBreed():
      print("")
  #FATHER ----
  for r in rats[1]:
    if r.canBreed() == True and len(temprats[1]) != 10:
        temprats[1].append(r)
    if not r.canBreed():
      print("")

  return temprats, largest, smallest

def calculate_mean(rats):
  total = 0
  numRats = NUM_RATS
  for num in rats[0]:
    total += num.weight
  for num in rats[1]:
    total += num.weight

  return total // numRats

def fitness(rats):
  """Determine if the target average matches the current population's average"""
  mean = calculate_mean(rats)
  return mean >= GOAL, mean

def main():
  goalmet = False
  population = initial_population()
  generation = 0
  smallest_generation = []
  largest_generation = []
  largest_rat = 0
  averages = ""
  while goalmet == False:
    children = breed(population)
    pups = mutate(children)
    population, gen_largest, gen_smallest = select(population, pups)
    fulfillment, mean = fitness(population)
    

    generation += 1
    averages += str(int(mean)) + "  "
    if gen_largest > largest_rat:
      largest_rat = gen_largest
    smallest_generation.append(gen_smallest)
    largest_generation.append(gen_largest)
    if fulfillment == True:
      goalmet = True
    elif generation == GENERATION_LIMIT:
      goalmet = True 
  
  smallest_generation.sort()
  largest_generation.sort()

  #file creation ----
  with open("largest_rat.txt", "w") as openFile:
    for i in largest_generation:
      openFile.write(str(i) + ", ")

  with open("smallest_rat.txt", "w") as openFile:
    for i in smallest_generation:
      openFile.write(str(i) + ", ")

  with open("average_generation.txt", "w") as openFile:
    openFile.write(averages)
  #------------

  print("RESULTS".center(40, "~"))
  print(f"Total Population Mean: {int(mean)}\n")
  print(f"Generations: {generation}")
  print(f"Experiment Duration: ~{int(generation//GENERATIONS_PER_YEAR)} year(s)")
  print(f"\nLargest Rat: {(largest_rat)}\n")
  print(f"Weight Averages:\n{averages}")
  print("--------------------------------------------\n")
if __name__ == "__main__":
  main()