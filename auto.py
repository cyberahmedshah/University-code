import os

# os.makedirs("Projects", exist_ok=True)

# with open("Projects/char.txt", "w") as f:
#     pass 


os.makedirs("Masterclasses", exist_ok=True)


for i in range (1, 101):
    with open (f"Masterclasses/Day{i}", "w") as f:
        f.write(f"Welcome to the Day {i} of the masterclass")

 