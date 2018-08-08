import os
def rename_files():
    # get file name from a folder
    file_list = os.listdir("/Users/wgarcia/Workspace/Udacity-Xi/Small games/Prank")
    #print("old name: " + str(file_list))
    saved_path = os.getcwd()
    print("Current working directory is " + saved_path)
    os.chdir("/Users/wgarcia/Downloads/prank")
    
    # for each file, rename filename
    for file_name in file_list:
        os.rename(file_name, file_name.strip("0123456789")) 
        print(file_name)
    os.chdir(saved_path)

rename_files()