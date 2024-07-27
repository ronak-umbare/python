import os

# # if(not os.path.exists("Data")):
# #     os.mkdir("Data")

# for i in range(0,100):
#     os.rename(f"Data/SampleFile_{i+1}",f"Data/SampleFolder_{i+1}")
    
    
def create_file(filename):
    try:
        with open(filename, 'x') as f:
            print("File name {filename}: Created successfully!..")
    except FileExistsError:
        print("File already exist")
    except Exception as E:
        print("An Error occured")
        
def view_files():
    files = os.listdir()
    if not files:
        print("No files in directory")
        for file in files:
            print(file)

def delete(filename):
    try:
        os.remove(filename)
        print("{filename} has been deleted successfully")
    except FileNotFoundError:
        print("file not found")
    except Exception as E:
        print("An error occured")
        
def read(filename):
    try:
        with open(filename , "r") as f:
            content = f.read()
            print("{filename} contains = ")
            print(content)
    except FileNotFoundError:
        print("File not found")
    except Exception as E:
        print("An error occured")
        

    
            
            