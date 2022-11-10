def return_10():
    return 10

# def add(a, b):
    result = a + b
    return result

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
    
def multiply(a, b):
    return a*b

def divide(a, b):
    return a/b

def length_of_string(string):
    return len(string)

def join_string(string_a, string_b):
    return string_a + string_b

def add_string_as_number(a, b):
    return int(a) + int(b)

def number_to_full_month_name(number):
    months = {1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December",
        }
    return months[number]

def number_to_short_month_name(number):
    months = {1: "Jan",
        2: "Feb",
        3: "Mar",
        4: "Apr",
        5: "May",
        6: "Jun",
        7: "Jul",
        8: "Aug",
        9: "Sept",
        10: "Oct",
        11: "Nov",
        12: "Dec",
        }
    return months[number]

def volume_of_cube(b):
    return b**3

def reverse_string(example):
    return example[::-1]
    
def fahrenheit_to_celsius(fahrenheit):
    return ((fahrenheit - 32) * 5/9)

def manipulate(num):
    num += 10
    print(num)
