import os
from datetime import datetime
                     
                  
def change_name(path):
    directory = os.path.expanduser(path)
    for root, dirs, files in os.walk(directory):
        for name in files:
            if name.endswith(".txt"):
                id_file = str(id(name))
                modified_name = datetime.fromtimestamp(os.path.getctime(name)).strftime(f"(t)%H-%M-%S(id){id_file[8:]}(d)%d-%m-%Y.txt")
                os.rename(name, modified_name)
                print(name, "- renamed to -", modified_name)

print("Hello,",os.getlogin(),"\n\nThis script will allow you to rename your files to actual data of creation.\n\
Each file will be classified with (t) - time, (id) - file id and (d) - creation date.\n")
path = input("\nEnter your path name here: ")
print("")
change_name(path)
print("\nIt's all done, friend\nHave a nice day!")




    




            
              
 

    
