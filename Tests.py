from Functions import *

def test_add_transaction():
    apList = initApartments()
    history = []
    try:
        add_transaction(apList, ["20", "water", "100"], history)
        assert False
    except ValueError:
        assert True

    try:
        add_transaction(apList, ["9.5", "water", "100"], history)
        assert False
    except ValueError:
        assert True
    
    try:
        add_transaction(apList, ["5", "watr", "33"], history)
    except ValueError:
        assert True

def test_remove_transaction():
    apList = initApartments()
    history = []
    try:
        remove_transaction(apList, ["0"], history)
        assert False
    except ValueError:
        assert True

    try:
        remove_transaction(apList, ["11"], history)
        assert False
    except ValueError:
        assert True

    try:
        remove_transaction(apList, ["7.5"], history)
        assert False
    except ValueError:
        assert True
    
    try:
        remove_transaction(apList, ["5", "two", "7"], history)
        assert False
    except ValueError:
        assert True

    try:
        remove_transaction(apList, ["7", "to", "5"], history)
        assert False
    except ValueError:
        assert True

    try:
        remove_transaction(apList, ["5.5", "to", "8"], history)
        assert False
    except ValueError:
        assert True
    
    try:
        remove_transaction(apList, ["5", "to", "8.5"], history)
        assert False
    except ValueError:
        assert True
    
    try:
        remove_transaction(apList, ["0", "to", "6"], history)
        assert False
    except ValueError:
        assert True
    
    try:
        remove_transaction(apList, ["5", "to", "11"], history)
        assert False
    except ValueError:
        assert True

    try:
        remove_transaction(apList, ["heting"], history)
        assert False
    except ValueError:
        assert True

def test_replace_data():
    apList = initApartments()
    history = []
    try:
        replace_data(apList, ["5", "gas", "wth", "100"], history)
        assert False
    except ValueError:
        assert True

    try:
        replace_data(apList, ["5", "heting", "with", "90"], history)
        assert False
    except ValueError:
        assert True

    try:
        replace_data(apList, ["3.5", "gas", "with", "50"], history)
        assert False
    except ValueError:
        assert True

    try:
        replace_data(apList, ["12", "gas", "with", "100"], history)
        assert False
    except ValueError:
        assert True

    try:
        replace_data(apList, ["0", "gas", "with", "40"], history)
        assert False
    except ValueError:
        assert True

    try:
        replace_data(apList, ["6", "gas", "with", "150.5"], history)
        assert False
    except ValueError:
        assert True

def test_list_apartments():
    apList = initApartments()

    try:
        list_apartments(apList, ["0"])
        assert False
    except ValueError:
        assert True

    try:
        list_apartments(apList, ["12"])
        assert False
    except ValueError:
        assert True

    try:
        list_apartments(apList, ["7.5"])
        assert False
    except ValueError:
        assert True

    try:
        list_apartments(apList, ["$", "56"])
        assert False
    except ValueError:
        assert True

    try:
        list_apartments(apList, [">", "34.5"])
        assert False
    except ValueError:
        assert True

def test_compute_sum():
    apList = initApartments()

    try:
        compute_sum(apList, ["heat"])
        assert False
    except ValueError:
        assert True

    try:
        compute_sum(apList, [])
        assert False
    except ValueError:
        assert True
    
    try:
        compute_sum(apList, ["heating", "10"])
        assert False
    except ValueError:
        assert True

def test_compute_max():
    apList = initApartments()

    try:
        compute_max(apList, [])
        assert False
    except ValueError:
        assert True

    try:
        compute_max(apList, ["7.5"])
        assert False
    except ValueError:
        assert True

    try: 
        compute_max(apList, ["0"])
        assert False
    except ValueError:
        assert True

    try:
        compute_max(apList, ["12"])
        assert False
    except ValueError:
        assert True

def test_sort_expenses():
    apList = initApartments()
    try:
        sort_expenses(apList, ["apart"])
        assert False
    except ValueError:
        assert True
    
    try:
        sort_expenses(apList, [])
        assert False
    except ValueError:
        assert True

    try:
        sort_expenses(apList, ["typ"])
        assert False
    except ValueError:
        assert True

def test_filter_expenses():
    apList = initApartments()
    history = []
    try:
        filter_expenses(apList, [], history)
        assert False
    except ValueError:
        assert True

    try:
        filter_expenses(apList, ["ga"], history)
        assert False
    except ValueError:
        assert True

    try:
        filter_expenses(apList, ["20.2"], history)
        assert False
    except ValueError:
        assert True

    try:
        filter_expenses(apList, ["20", "15"], history)
        assert False
    except ValueError:
        assert True

def perform_tests():
    test_add_transaction()
    test_remove_transaction()
    test_replace_data()
    test_list_apartments()
    test_compute_sum()
    test_compute_max()
    test_sort_expenses()
    test_filter_expenses()