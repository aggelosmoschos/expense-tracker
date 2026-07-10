from expense_input import calculate_total, calculate_average_expense, calculate_category_totals, find_highest_expense, find_lowest_expense
def test_calculate_total_empty():
    assert calculate_total([]) == 0 

def test_calculate_total_one():
    assert calculate_total([{"amount": 10}]) == 10

def test_calculate_total_multiple():
    assert calculate_total([{"amount": 10}, {"amount": 20}]) == 30

def test_calculate_average_empty():
    assert calculate_average_expense([]) == 0 

def test_calculate_average_one(): 
    assert calculate_average_expense([{"amount": 10}]) == 10 

def test_calculate_average_multiple(): 
    assert calculate_average_expense([{"amount": 20}, {"amount": 10}]) == 15

def test_calculate_category_empty(): 
    assert calculate_category_totals([]) == {}

def test_calculate_category_one():
    assert calculate_category_totals([{"category": "food", "amount": 10}]) == {"food": 10}

def test_calculate_category_multiple():
    assert calculate_category_totals([{"category": "food", "amount":10}, {"category": "entertainment", "amount": 20}, {"category": "transport", "amount": 0}, {"category": "rent", "amount": 150}, {"category": "food", "amount": 25}]) == {"food": 35, "entertainment": 20, "transport": 0, "rent": 150,}

def test_find_highest_empty():
    assert find_highest_expense([]) is None 

def test_find_highest_one(): 
    assert find_highest_expense([{"category": "food", "amount": 10}]) == {"category": "food", "amount": 10}

def test_find_highest_multiple():
    assert find_highest_expense([{"category": "food", "amount":10}, {"category": "entertainment", "amount": 20}, {"category": "transport", "amount": 3}, {"category": "rent", "amount": 150}, {"category": "food", "amount": 25}]) == {"category": "rent", "amount": 150}

def test_find_lowest_empty():
    assert find_lowest_expense([]) is None 

def test_find_lowest_one():
    assert find_lowest_expense([{"category": "food", "amount": 10}]) == {"category": "food", "amount": 10} 

def test_find_lowest_multiple():
    assert find_lowest_expense([{"category": "food", "amount":10}, {"category": "entertainment", "amount": 20}, {"category": "transport", "amount": 3}, {"category": "rent", "amount": 150}, {"category": "food", "amount": 25}]) == {"category": "transport", "amount": 3}
