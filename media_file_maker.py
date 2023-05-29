import os
arr = os.listdir('images/')
print("[")
for x in arr:
    print(f"'images/{x}'", end=',')
print("]")