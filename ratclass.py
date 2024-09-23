class Rat():
  def __init__(self, sex, weight):
    self.sex = sex
    self.weight = weight
    self.litters = 0

  def __str__(self):
    return str(f"{self.sex}:{self.weight}") # FIX

# ACTIONS----------
  def getWeight(self):
    return self.weight
  
  def getSex(self):
    return self.sex

  def canBreed(self):
    if self.litters == 5:
      return False
    else:
      return True
#--------------------

# TOOLS--------------
  def __repr__(self):
    return f"{self.sex}:{self.weight}"
    
  def __lt__(self, otherobj):
    return self.weight <  otherobj.weight
  def __gt__(self, otherobj):
    return self.weight > otherobj.weight
  def __le__(self, otherobj):
    return self.weight <= otherobj.weight
  def __ge__(self, otherobj):
    return self.weight >= otherobj.weight
  def __eq__(self, otherobj):
    return self.weight == otherobj.weight
