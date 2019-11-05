def create_apartment(idx = -1, water = -1, heating= -1, electricity = -1, gas = -1):
    '''
    Function creates and returns a new apartment
    '''
    return {"index":int(idx), "total":int(water)+int(heating)+int(electricity)+int(gas), "water":int(water), "heating":int(heating), 
    "electricity":int(electricity), "gas":int(gas)}

def create_list(apartmentList):
    '''
    Function creates a copy of the current apartmentList and returns it
    params: apartmentList - list of all apartments expenses
    '''
    newList = []
    for x in apartmentList:
        newList.append(x.copy())
    return newList

def initApartments():
    '''
    Function initiates 10 apartments
    '''
    apartmentList = []
    apartmentList.append(create_apartment(0, 0, 0, 0, 0))
    apartmentList.append(create_apartment(1, 10, 5, 2, 4))
    apartmentList.append(create_apartment(2, 7, 8, 9, 10))
    apartmentList.append(create_apartment(3, 5, 5, 10, 20))
    apartmentList.append(create_apartment(4, 4, 2, 1, 0))
    apartmentList.append(create_apartment(5, 8, 8, 8, 8))
    apartmentList.append(create_apartment(6, 7, 9, 10, 11))
    apartmentList.append(create_apartment(7, 11, 13, 20, 19))
    apartmentList.append(create_apartment(8, 3, 2, 15, 1))
    apartmentList.append(create_apartment(9, 6, 6, 6, 0))
    apartmentList.append(create_apartment(10, 9, 9, 9, 6))
    return apartmentList    


def get_apartment_type(apartment, tip):
    '''
    Function returns the expenses for one type of the apartment
    params: apartment - the apartment for which we need the expense
            tip - the type of expense we need to return ( e.g. water, electricity, etc.)
    output: returns the expenses for type 'tip' of apartment 'apartment'
    '''
    return apartment[tip]

def set_apartment_type(apartment, tip, amount):
    '''
    Function sets the expenses for one type of the apartment to a new value
    params: apartment - the apartment whose expense will be changed
            tip - type of expense that will be changed
            amount - the new amount of the given type for the given apartment
    '''
    apartment[tip] = amount

def add_transaction(apartmentList, params, history):
    '''
    Function checks the parameters and performs the operation (if they are ok) or raises a ValueError
    params: apartmentList - the list of apartments
            params - the list of parameters
    '''
    if len(params) < 3:
        raise ValueError("There are not enough parameters")
    
    if len(params) > 3:
        raise ValueError("There are too many parameters")
    
    try:
        index = int(params[0])
    except:
        raise ValueError("Index of apartment should be an integer")

    if index < 1 or index > 10:
        raise ValueError("Index of apartment should be between 1 and 10")

    try:
        suma = int(params[2])
    except:
        raise ValueError("The transaction amount should be an integer")

    tip = params[1]
    if tip not in ["water", "electricity", "gas", "heating"]:
        raise ValueError("No utility found with such name, please check for spelling errors")

    history.append(create_list(apartmentList))
    set_apartment_type(apartmentList[index], tip, get_apartment_type(apartmentList[index], tip)+suma)
    set_apartment_type(apartmentList[index], "total", get_apartment_type(apartmentList[index], "total")+suma)

def remove_allAps(apartmentList, tip):
    '''
    Function removes expenses from all apartments for a certain type
    params: apartmentList - the list of apartments
            tip - the type for which all expenses will be removed
    '''
    for i in range (1, len(apartmentList)):
        set_apartment_type(apartmentList[i], "total", get_apartment_type(apartmentList[i], "total") - get_apartment_type(apartmentList[i], tip))
        set_apartment_type(apartmentList[i], tip, 0)

def remove_forAp(apartmentList, st, dr):
    '''
    Function removes all expenses for apartments in range [st, dr)
    params: apartmentList - list of expenses for all apartments
            st - left hand side of the interval
            dr - right hand side of the interval
    '''
    if st > dr:
        raise ValueError("Left-hand side of the interval should be lower than the right-hand side")
    if st < 1 or st > 10:
        raise ValueError("Left-hand side of the interval is out of range")
    if dr < 1 or dr > 10:
        raise ValueError("Right-hand side of the interval is out of range")

    for i in range (st, dr+1):
        set_apartment_type(apartmentList[i], "total", 0)
        set_apartment_type(apartmentList[i], "water", 0)
        set_apartment_type(apartmentList[i], "electricity", 0)
        set_apartment_type(apartmentList[i], "heating", 0)
        set_apartment_type(apartmentList[i], "gas", 0)

def remove_transaction(apartmentList, params, history):
    '''
    Function checks the parameters and performs the operation (if they are ok) or raises a ValueError
    params: apartmentList - the list of apartments
            params - the list of parameters
    '''
    if len(params) == 1:
        if params[0] in ["water", "electricity", "gas", "heating"]:
            history.append(create_list(apartmentList))
            remove_allAps(apartmentList, params[0])
        else:
            try:
                params[0] = int(params[0])
            except:
                raise ValueError("Bad transaction parameters")
            history.append(create_list(apartmentList))
            remove_forAp(apartmentList, params[0], params[0])
    elif len(params) == 3:
        try:
            st = int(params[0])
        except:
            raise ValueError("Left-hand side of the interval should be an integer")
        try:
            dr = int(params[2])
        except:
            raise ValueError("RIght-hand side of the interval should be an integer")

        if params[1] != "to":
            raise ValueError("Invalid command")
        history.append(create_list(apartmentList))
        remove_forAp(apartmentList, st, dr)

    else:
        raise ValueError("Number of parameters is not right")

def replace_data(apartmentList, params, history):
    '''
    Function replaces data for one type of expense of an apartment
    params: apartmentList - list of expenses for all apartments
            params - the params for the replace operation
    '''
    if len(params) != 4:
        raise ValueError("Number of parameters is not right")
    try:
        index = int(params[0])
    except:
        raise ValueError("Index of apartment should be an integer")

    try:
        amount = int(params[3])
    except:
        raise ValueError("The amount in the transaction should be an integer")
    
    tip = params[1]
    if tip not in ["water", "gas", "electricity", "heating"]:
        raise ValueError("The utility is not recognized, try checking for spelling errors")

    if index < 1 or index > 10:
        raise ValueError("Index of apartment should be between 1 and 10")

    if params[2] != "with":
        raise ValueError("Command is not recognized")

    history.append(create_list(apartmentList))
    set_apartment_type(apartmentList[index], "total", get_apartment_type(apartmentList[index], "total") - get_apartment_type(apartmentList[index], tip) + amount)
    set_apartment_type(apartmentList[index], tip, amount)

def list_apartments(apartmentList, params):
    '''
    Function lists expenses for apartments in different ways, depending on the input
    params: apartmentList - list of expenses for all apartments
            params - the params for the list operation
    output: return a code for the print function
    '''
    if len(params) == 0:
        return 0
    elif len(params) == 1:
        try:
            params[0] = int(params[0])
        except:
            raise ValueError("Index of apartment should be an integer")
        if params[0] < 1 or params[0] > 10:
            raise ValueError("Index of apartment should be between 1 and 10")
        return 1
    elif len(params) == 2:
        try:
            params[1]= int(params[1])
        except:
            raise ValueError("The amount to which we compare should be an integer")
        if params[0] == '<':
            return 2
        elif params[0] == '=':
            return 3
        elif params[0] == '>':
            return 4
        else:
            raise ValueError("Sign is not ok")
    else:
        raise ValueError("Number of parameters is not ok")

def compute_sum(apartmentList, params):
    '''
    Function computes sum of all apartments for one utlity
    params: apartmentList - list of all apartments expenses
            params - parameters needed to carry out the operation
    '''
    if len(params) != 1:
        raise ValueError("Number of parameters is not right")
    if params[0] not in ["water", "electricity", "heating", "gas"]:
        raise ValueError("The utility is not recognized, please check for spelling errors")
    suma = 0
    for i in range (1, 11):
        suma = suma + get_apartment_type(apartmentList[i], params[0])
    return suma

def compute_max(apartmentList, params):
    '''
    Function computes the maximum expense for one apartment
    params: apartmentList - list of all apartments expenses
            params - parameters needed to carry out the operation
    '''
    if len(params) != 1:
        raise ValueError("Number of parameters not right")
    try:
        index = int(params[0])
    except:
        raise ValueError("Index of apartment should be an integer")

    if index<1 or index>10:
        raise ValueError("Index of apartment should be between 1 and 10")
    
    s1 = get_apartment_type(apartmentList[index], "heating") 
    t1 = "heating"
    s2 = get_apartment_type(apartmentList[index], "gas")
    t2 = "gas"
    s3 = get_apartment_type(apartmentList[index], "electricity")
    t3 = "electricity"
    s4 = get_apartment_type(apartmentList[index], "water")
    t4 = "water"
    if s2>s1:
        s1 = s2
        t1 = t2
    
    if s4>s3:
        s3 = s4
        t3 = t4

    if s3 > s1:
        s1 = s3
        t1 = t3

    return [s1, t1]

def sort_by_type(apartmentList, tip):
    '''
    Function sorts apartments based on the expenses for one utlity
    params: apartmentList - list of all apartments expenses
            tip - the utlity based on which we sort    
    '''
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    for i in range(0, 10):
        for j in range(i+1, 10):
            x = lista[i]
            y = lista[j]
            if get_apartment_type(apartmentList[x], tip) > get_apartment_type(apartmentList[y], tip):
                lista[i], lista[j] = lista[j], lista[i]
    return lista

def sort_expenses(apartmentList, params):
    '''
    Function sorts expenses of all apartments
    params: apartmentList - list of all apartments expenses
            params - parameters needed to carry out the operation
    '''
    if len(params) != 1:
        raise ValueError("Number of parameters is not right")
    if params[0] == "apartment":
        lista = []
        lista.append(sort_by_type(apartmentList, "total"))
        return lista
    elif params[0] == "type":
        lista = []
        lista.append(sort_by_type(apartmentList, "electricity"))
        lista.append(sort_by_type(apartmentList, "water"))
        lista.append(sort_by_type(apartmentList, "heating"))
        lista.append(sort_by_type(apartmentList, "gas"))
        return lista
    else:
        raise ValueError("Second parameter not recognized, please check spelling errors")

def filter_by_type(apartmentList, tip):
    '''
    Function filters the database of apartments based on a utlity
    params: apartmentList - list of all apartments expenses
            tip - the utility based on which we sort
    '''
    newList = []
    for ap in apartmentList:
        newDict = {}
        newDict["index"] = get_apartment_type(ap, "index")
        if tip in ap.keys():
            newDict[tip] = get_apartment_type(ap, tip)
        newList.append(newDict)
    apartmentList.clear()
    apartmentList.extend(newList)

def filter_by_amount(apartmentList, amount):
    '''
    Function filters expenses lower than amount
    params: apartmentList - list of all apartments expenses
            amount - the amount compared to which we filter
    '''
    newList = []
    for ap in apartmentList:
        newDict = {"index":get_apartment_type(ap, "index")}
        for ut in ap.keys():
            if get_apartment_type(ap, ut) < amount:
                newDict[ut] = get_apartment_type(ap, ut)
        #if get_apartment_type(ap, "water")<amount:
         #   newDict["water"] = get_apartment_type(ap, "water")
        #if get_apartment_type(ap, "heating")<amount:
         #   newDict["heating"] = get_apartment_type(ap, "heating")
        #if get_apartment_type(ap, "electricity")<amount:
         #   newDict["electricity"] = get_apartment_type(ap, "electricity")
        #if get_apartment_type(ap, "gas")<amount:
         #   newDict["gas"] = get_apartment_type(ap, "gas")
        newList.append(newDict)
    apartmentList.clear()
    apartmentList.extend(newList)

def filter_expenses(apartmentList, params, history):
    '''
    Function filters expenses based on the given parameters
    params: apartmentList - list of all apartments expenses
            params - parameters needed to carry out the operation
            history - database of all previous apartmentLists
    '''
    if len(params) != 1:
        raise ValueError("Number of parameters is not right")
    if params[0] in ["water", "electricity", "heating", "gas"]:
        history.append(create_list(apartmentList))
        filter_by_type(apartmentList, params[0])
    else:
        try:
            params[0] = int(params[0])
        except:
            raise ValueError("Second parameter is neither a utility nor an amount")
        history.append(create_list(apartmentList))
        filter_by_amount(apartmentList, params[0])
    

def undo_command(apartmentList, history):
    '''
    Function undos the last operation which modified the apartmentList
    params: apartmentList - list of all apartments expenses
            history - database of all previous apartmentLists
    '''
    if len(history) == 0:
        raise ValueError("No more undos")
    apartmentList.clear()
    apartmentList.extend(history.pop())