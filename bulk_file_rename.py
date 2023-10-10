import os

import condition as condition

directory = input("Enter the Directory Path [:E:/Tomato/] :")
i=1
for filename in os.listdir(directory):
    if filename:
        base_name, extension = os.path.splitext(filename)
        new_name = str(i)+"" + extension
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_name)

        os.rename(old_path, new_path)
        print(old_path,"------> ",new_path)
        i+=1
print("File renaming complete.")

