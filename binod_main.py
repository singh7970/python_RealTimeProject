def isBinod(filename):
    with open(filename, "r") as f:
        filecontent = f.read()
        if "binod" in filecontent.lower():
            return True
    return False
import os
dir_content = os.listdir()
binod_count = 0
for item in dir_content:
    if item.endswith('.txt'):
        flag = isBinod(item)
        if flag:
            print(f"Binod found in {item}")
            binod_count += 1
        else:
            print(f"Binod not found in {item}")
print(f"Total BINOD found: {binod_count}")





