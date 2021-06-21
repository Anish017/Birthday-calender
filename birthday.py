bdays = {'Anish': '2002-04-04', } # dictionary to store name as key and DOB as value


#print(type(bdays))       (#just to clearify if the dictonary syntax is correct or not.)
def show_menu():
    print("\n***** THIS IS YOUR BITHDAY CALENDER *****")
    print(" OKAY! WHAT YOU WANT ME TO DO")
    print("-----------------------------------------")
    print("\t1. View Birthday")
    print("\t2. Add Birthday")
    print("\t3. Update Birthday")
    print("\t4. Remove Birthday")
    print("\t5. View all Birthday")
    print("\t6. EXIT")

#___________________________________________________________________________________________________________

def display():
    print("*****BIRTHDAYS LISTS*****")
    print("-------------------------")
    for key, value in bdays.items():
        print("{} : {}" .format(key,value))

#___________________________________________________________________________________________________________
while True:    #while loop is used coz we need this to loop again and again soo..
    show_menu()

    choise = input()    # for users to input 

    if choise == '1':

        name = input("Enter the name of the peson you want:  ")
        if name in bdays.keys():
            print("{} : {} " .format(name , bdays[name]))

        else:
            print("Sorry!! No details found..")


 #_______________________________________________________________________________________________________________       
        
    elif choise == '2':
        name = input("Enter the name of the person You want to add:  ")
        if name in bdays.keys():
            print("Name already exists.")
        else:
            birth_date = input("Enter the birthday for {}: " .format(name))
            bdays[name] = birth_date           
#_____________________________________________________________________________________________________________________
    elif choise == '3':
        name = input("Enter the name of the person You want to Update:  ")
        if name in bdays.keys():
            birth_date = input("Enter the birthday for {}: 2" .format(name))
            bdays[name] = birth_date
        else:
            print("Name Doesn't exists to update:")             
#_____________________________________________________________________________________________________________________
    elif choise == '4':
        name = input("Enter the name of the person You want to 'DELETE':  ")
        if name in bdays.keysa():
            del bdays[name]
            print("*** Sucessfully Deleted ***")
        else:
            print("Name Does't EXists to 'DELETE'") 
#_____________________________________________________________________________________________________________________
    elif choise == '5':
        display()       
#_____________________________________________________________________________________________________________________
    elif choise == '6':
        print("Thanks! See YOU Again")
        break
  
    else:
        print("Look At the menu and enter number accordingly")





   