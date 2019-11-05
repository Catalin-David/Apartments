from Functions import *
from os import *

def readCommand():
    '''
    Function reads the user's command
    output: a tuple, the command and its parameters
    '''
    cmd = input(">Give command: ")
    print("")
    idx = cmd.find(" ")
    if idx == -1:
        return (cmd, [])
    command = cmd[:idx]
    params = cmd[idx+1:]
    params = params.split(" ")
    for i in range (len(params)):
        params[i] = params[i].strip()

    return (command, params)

def add_transcation_ui(apartmentList, params, history):
    ''' 
    Function tells the user the result of the add_trasaction operation with the current parameters
    params: apartmentList - the list of apartments
            params - parameters of a new transaction 
            history - database of all previous apartmentLists
    output: a message that informs the user whether the transaction was added successfully or not
    '''
    try:
        add_transaction(apartmentList, params, history)
        print("Operation performed successfully")
    except ValueError as ve:
        print(ve)

def remove_transaction_ui(apartmentList, params, history):
    '''
    Function tells the user the result of the remove_trasaction operation with the current parameters
    params: apartmentList - list of expenses for all apartments
            params - params for a operation of type remove
            history - database of all previous apartmentLists
    output: a message that informs the user whether the trasaction was removed successfully or not
    '''
    try:
        remove_transaction(apartmentList, params, history)
        print("Operation performed successfully")
    except ValueError as ve:
        print(ve)
    
def replace_data_ui(apartmentList, params, history):
    '''
    Function tells the user the result of the replace_data operation with the current parameters
    params: apartmentList - list of expenses for all apartments
            params - params for a operation of type replace_data
            history - database of all previous apartmentLists
    output: a message that informs the user whether the data was replaced successfully or not
    '''
    try:
        replace_data(apartmentList, params, history)
        print("Operation performed successfully")
    except ValueError as ve:
        print(ve)

def print_apartment(apartment, index):
    '''
    Function prints all expenses of a given apartment
    params : apartment - the apartment for which we print expenses
    '''
    string = "Apartment " + str(index) + "; "
    #print("Apartment", get_apartment_type(apartment, "index"))
    for ut in apartment.keys():
        if ut != "index":
            string = string + str(get_apartment_type(apartment, ut)) + " " + ut + "; "
            #print(ut, get_apartment_type(apartment, ut), "RON") 

    print(string)
    #print("Apartment", get_apartment_type(apartment, "index"), ";", "total:", get_apartment_type(apartment, "total"), ";", 
    #"water", get_apartment_type(apartment, "water"), ";", "electricity", get_apartment_type(apartment, "electricity"), ";", 
    #"heating", get_apartment_type(apartment, "heating"), ";", "gas", get_apartment_type(apartment, "gas"), ";")

def printList(apartmentList):
    '''
    The funtion prints the expenses of all apartments
    params: apartmentList - the list of expenses for all apartments
    '''
    for i in range (1, len(apartmentList)):
        print_apartment(apartmentList[i], i)
    print("")

def print_lower(apartmentList, amount):
    '''
    Function prints apartments for which the total expenses are lower than a certain amount
    params: apartmentList - the list of expenses for all apartments
            amount - the amount to which we need to compare
    '''
    for i in range(1, len(apartmentList)):
        if get_apartment_type(apartmentList[i], "total") < amount:
            print_apartment(apartmentList[i], i)

def print_equal(apartmentList, amount):
    '''
    Function prints apartments for which the total expenses are equal to certain amount
    params: apartmentList - the list of expenses for all apartments
            amount - the amount to which we need to compare
    '''
    for i in range(1, len(apartmentList)):
        if get_apartment_type(apartmentList[i], "total") == amount:
            print_apartment(apartmentList[i], i)

def print_higher(apartmentList, amount):
    '''
    Function prints apartments for which the total expenses are higher than a certain amount
    params: apartmentList - the list of expenses for all apartments
            amount - the amount to which we need to compare
    '''
    for i in range(1, len(apartmentList)):
        if get_apartment_type(apartmentList[i], "total") > amount:
            print_apartment(apartmentList[i], i)

def list_apartments_ui(apartmentList, params):
    '''
    Function receives parameters for an operation of type list
    params: apartmentList - the list of expenses for all apartments
            params - the parameters for an operation of type list
    '''
    try:
        ans = list_apartments(apartmentList, params)
        if ans == 0:
            printList(apartmentList)
        elif ans == 1:
            print_apartment(apartmentList[int(params[0])], int(params[0]))
        elif ans == 2:
            print_lower(apartmentList, int(params[1]))
        elif ans == 3:
            print_equal(apartmentList, int(params[1]))
        elif ans == 4:
            print_higher(apartmentList, int(params[1]))
    except ValueError as ve:
        print(ve)

def compute_sum_ui(apartmentList, params):
    '''
    Function tells the user the result of the compute_sum operation with the current parameters
    params: apartmentList - list of expenses for all apartments
            params - params for a operation of type compute_sum
    output: a message that informs the user whether the sum was computed successfully or not
    '''
    try:
        suma = compute_sum(apartmentList, params)
        print("The total amount for type " + params[0] + " is " + str(suma) + "RON")
    except ValueError as ve:
        print(ve)

def compute_max_ui(apartmentList, params):
    '''
    Function tells the user the result of the compute_max operation with the current parameters
    params: apartmentList - list of expenses for all apartments
            params - params for a operation of type compute_max
    output: a message that informs the user whether the max was computed successfully or not
    '''
    try:
        result = compute_max(apartmentList, params)
        suma = result[0]
        tip = result[1]
        print("The maximum expense for apartment " + params[0] + " is of type " + tip + " and it amounts to " + str(suma) + "RON")
    except ValueError as ve:
        print(ve)

def sort_expenses_ui(apartmentList, params):
    '''
    Function tells the user the result of the sort_expenses operation with the current parameters
    params: apartmentList - list of expenses for all apartments
            params - params for a operation of type sort_expenses
    output: a message that informs the user whether the expenses were sorted successfully or not
    '''
    try:
        sortedLists = sort_expenses(apartmentList, params)
        if len(sortedLists) == 1:
            print("Apartments are sorted ascending by total expenses")
            for lista in sortedLists:
                for s in lista:
                    print("Apartment " + str(s) + " : " + str(get_apartment_type(apartmentList[s], "total")) + "RON")
        else:
            whichList = 1
            tip = ""
            for lista in sortedLists:
                if whichList == 1:
                    tip = "electricity"
                elif whichList == 2:
                    tip = "water"
                elif whichList == 3:
                    tip = "heating"
                else:
                    tip = "gas"
                whichList += 1
                print("Apartments are sorted ascending by " + tip + " expenses")
                for s in lista:
                     print("Apartment " + str(s) + " : " + str(get_apartment_type(apartmentList[s], tip)) + "RON")
                print("")

    except ValueError as ve:
        print(ve)

def filter_expenses_ui(apartmentList, params, history):
    '''
    Function tells the user the result of the filter-expenses operation with the current parameters
    params: apartmentList - list of expenses for all apartments
            params - params for a operation of type filter-expenses
            history - database of all previous apartmentLists
    output: a message that informs the user whether the expenses were filtered successfully or not
    '''
    try:
        filter_expenses(apartmentList, params, history)
        print("Operation performed sucessfully")
    except ValueError as ve:
        print(ve)

def undo_command_ui(apartmentList, history):
    '''
    Function tells the user the result of the undo_command operation with the current parameters
    params: apartmentList - list of expenses for all apartments
            history - database of all previous apartmentLists
    output: a message that informs the user whether the data was replaced successfully or not
    '''
    try:
        undo_command(apartmentList, history)
        print("Operation performed successfully")
    except ValueError as ve:
        print(ve)

def start():
    '''
    Function navigates the user through the program
    '''
    apartmentList = initApartments()
    history = []
    while True:
        printList(apartmentList)
        cmdTuple = readCommand()
        command = cmdTuple[0]
        params = cmdTuple[1]
        if command == "add":
            add_transcation_ui(apartmentList, params, history)
        elif command == "remove":
            remove_transaction_ui(apartmentList, params, history)
        elif command == "replace":
            replace_data_ui(apartmentList, params, history)
        elif command == "list":
            list_apartments_ui(apartmentList, params)
        elif command == "sum":
            compute_sum_ui(apartmentList, params)
        elif command == "max":
            compute_max_ui(apartmentList, params)
        elif command == "sort":
            sort_expenses_ui(apartmentList, params)
        elif command == "filter":
            filter_expenses_ui(apartmentList, params, history)
        elif command == "undo":
            undo_command_ui(apartmentList, history)
        elif command == "exit":
            break
        else:
            print("Invalid command")
        print("")
        system("pause")
        system("cls")