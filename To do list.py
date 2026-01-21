# Make a to do list. User can add, remove and view task. Store the list in a file between sessions.
import csv
def add_row(file_name):
    with open(file_name,'r') as f:
        r = csv.reader(f)
        read = list(r)
        Sno=[]
        for row in read:
            Sno.append(row[0])
        
    with open(file_name,'a',newline="") as file:
        write = csv.writer(file)
        n=int(input("Enter Serial Number :"))
        task = input(f"Enter Task for Sno {n} :")
        write.writerow([n,task])

def add_rows(file_name) :
    with open(file_name,'r') as f:
        r = csv.reader(f)
        read = list(r)
        Sno=[]
        for row in read:
            Sno.append(row[0])
            
    with open(file_name,'a',newline="") as file:
        write = csv.writer(file)
        stop = 1
        while (stop!=0):
            n=int(input("Enter Serial Number :"))
            task = input(f"Enter Task for Sno {n} :")
            write.writerow([n,task])
            stop = int(input("Enter 1 to continue or 0 to stop :"))

def view_task(file_name):
    with open(file_name,'r') as file:
        r = csv.reader(file)
        read  = list(r)
        print("Sno   Task")
        for row in read:
            for item in row:
                print(f"{item}.    ",end="")
            print()
            
def remove_row(file_name):
    with open (file_name,'r') as file:
        r=csv.reader(file)
        read=list(r)
        sno=int(input("Enter Sno to remove :"))
        new_list = []
        for row in read:
            if(int(row[0])!=sno):
                new_list.append(row)
    with open(file_name,'w',newline="") as f:
        write= csv.writer(f)
        for row in new_list:
            write.writerow(row)
            
        
file_name = "ToDoList/ToDoList.csv"
while True:
    print("1. Add")
    print("2. Remove")
    print("3. View ")
    print("4. Exit")    
    choice = int(input("Enter choice :"))
    print()
    if(choice==1):
        print("1. Add only one row.")
        print("2. Add multiple row.")
        c=int(input("Enter choice :"))
        if(c==1):
            add_row(file_name)
            print()
        else:
            add_rows(file_name)
            print()
    elif(choice == 2):
        remove_row(file_name)
    elif(choice == 3):
        view_task(file_name)
        print()
    elif(choice == 4):
        print("Thank you.")
        break
    else:
        print("Invalid choice.")