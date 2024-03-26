#Question 1
def convert_f(temperature):#Task 2
    try:
        celsius = (temperature-32)*(5/9)
        return round(celsius, 2)
    except ValueError:
        return "Input is not a number."

while True:
    continue_user= input("Do you want to convert the temperature from Fahrenheit to Celsius?(yes/no) ")
    if continue_user.lower() != 'yes':
        break
    try: #Task 1
        user_input = int(input("What is the current temperature in Fahrenheit? "))
    except ValueError:
        print("Please enter a number.")
    else:#Task 3
        print(f"The temperature in celsius is: {convert_f(user_input)}")
    finally:
        print("Thank you for using the weather forecast application!")