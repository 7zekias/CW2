def tickets():
    tickets = {
        "London": 10.15,
        "Manchester": 22.50,
        "Birmingham": 21.40 
    }

def name():
    return input("Welcome to the ticketing system. Please enter your name")

def location():
    return input(f"Hello, {name}. Please enter the location you would like to visit")

def main():
    name()
    location()

main()