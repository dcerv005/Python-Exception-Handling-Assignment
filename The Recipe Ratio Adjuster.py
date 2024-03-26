#Question 2


def adjustment(a, b):
    try:
        adjustment_factor = a/b
        return f"The adjustment factor is: {adjustment_factor}"
    except ZeroDivisionError:
        return "You cannot divide by 0. Please pick a recipe that can give out more than 0 servings."
    

try: #Task 1
    original_recipe = int(input("How many serving does the recipe serve? "))
    serving_size = int(input("How many servings do you wish to make? "))
    print(adjustment(serving_size, original_recipe))
except ValueError:
    print("Please enter a number. Thank you.")
finally:#Task 3
    print("The outcome doesnt matter, have fun with the process if cooking!")

