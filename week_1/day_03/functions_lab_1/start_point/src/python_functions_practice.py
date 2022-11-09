def return_10():
    return 10

def add(a, b):
    result = a + b
    return result

def subtract(a, b):
    result = a - b
    return result

def multiply(a, b):
    result = a*b
    return result

def divide(a, b):
    result = a/b
    return result

def length_of_string(string):
    string_length=len(string)
    return string_length

def join_string(string_a, string_b):
    joined_string = string_a + string_b
    return joined_string

def add_string_as_number(a, b):
    result= int(a) + int(b)
    return result

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
    month_string = months[number]
    return month_string

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
    month_string = months[number]
    return month_string

def volume_of_cube(b):
    result= b**3
    return result

def reverse_string(example):
    result = example[::-1]
    return result
    
def fahrenheit_to_celsius(fahrenheit):
    celsius = ((fahrenheit - 32) * 5/9)
    return celsius


