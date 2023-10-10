import os
if __name__ == "__main__":
    reset = "\033[0m"
    cyan = "\033[36m"
    red = "\033[91m"
    print(cyan)
    print("""     ___                                  _     ____
    |_ _|_ __  _ __   ___   ___ ___ _ __ | |_  | __ )  ___  _   _
     | || '_ \| '_ \ / _ \ / __/ _ \ '_ \| __| |  _ \ / _ \| | | |
     | || | | | | | | (_) | (_|  __/ | | | |_  | |_) | (_) | |_| |
    |___|_| |_|_| |_|\___/ \___\___|_| |_|\__| |____/ \___/ \__, |
                                     Nothing is Impossible  |___/""")
    print(reset)
    directory = input("Enter the Directory Path [:E:/] :")
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
    print(red,"File renaming complete.")

