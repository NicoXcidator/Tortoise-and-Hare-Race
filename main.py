import random as rand
import time

tortoise = 0
hare = 0

for i in range(20):
  print(f"Step number {i + 1}")
  tortoise += 1
  hare += rand.randint(-1,3)
  print(f"Hare: {hare} ; Tortoise: {tortoise}")
  time.sleep(0.25)

if hare == tortoise:
  print("It's a TIE!")
elif tortoise > hare:
  print("Tortoise is victorious!")
else:
  print("Hare is victorious!")