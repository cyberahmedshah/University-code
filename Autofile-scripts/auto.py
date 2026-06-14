import os
import shutil


os.makedirs("Projects", exist_ok=True)

with open("Projects/char.txt", "w") as f:
     pass 


shutil.rmtree("Masterclasses")


for i in range (1, 101):
     with open (f"Masterclasses/Day{i}", "w") as f:
         f.write(f"Welcome to the Day {i} of the masterclass")

 