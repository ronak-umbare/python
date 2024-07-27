import os

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
        
def edit(filename):
    try:
        with open(filename, 'a') as f:
            content = input("Enter what do u wanna add : ")
            f.write(content + "\n") 
            print('Content added to {filename}')
    except FileNotFoundError:
        print("File not found")
    except Exception as E:
        print("An error occured")
        
def main():
    while True:
        print("FILE MANAGER \n")
        print("Press 1: to create \n")
        print("Press 2: to view \n")
        print("Press 3: to Delete \n")
        print("Press 4: to Read \n")
        print("Press 5: to Edit \n")
        print("Press 6: to Exit \n")
        
        choice = input("Enter UR choice : ")
         
        if choice == "1":
            filename = input("Enter filename to create: ")
            create_file(filename)
            
        elif choice == "2":
            view_files()
        
        elif choice == "3":
            filename = input("Enter filename u wanna delete: ")
            delete()
            
        elif choice == "4":
            filename = input("Enter the file name u wanna read: ")
            read(filename)
        
        elif choice == "5":
            filename = ("Enter the file name which you wanna edit: ")
            edit(filename)
            
        elif choice == "6":
            print("Closing...")
            break
            
        else:
            print("Invalid choice")
            
if __name__ == "__main__":
    main()
        
        
        
        