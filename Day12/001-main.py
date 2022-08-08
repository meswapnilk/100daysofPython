################### Scope ####################

enemies = 1 # Global Scope

def increase_enemies():
  enemies = 2  #Local Scope
  print(f"enemies inside function: {enemies}")

def increase_global_enemies():
    global enemies # Avoid this
    enemies = 5  #Using Global Scope

def incr_enemies(): # Recommended 
    return enemies + 1

increase_enemies()
increase_global_enemies()
enemies = incr_enemies()
print(f"enemies outside function: {enemies}")




# Local Scope