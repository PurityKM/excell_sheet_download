# one

def beer_menu():
    print("**** Jamal and Daughters Pub ****")
    
    print("1) Tusker               200/=")
    print("2) Pilsner              280/=")
    print("3) Smirnoff Ice         320/=")
    print("4) White Cap            180/=")
    
def calc_cost(choice, quantity):
    prices = [200, 280, 320, 180]
    
    if choice < 1 or choice > 4:
        print("Invalid choice. Please choose 1,2,3,4.")
    
    price_per_bottle = prices[choice - 1]
    total_cost = quantity * price_per_bottle 
    
    print(f"{quantity} bottles will cost you Kshs. {total_cost}/=") 
        
    
beer_menu()
choice = int(input("Enter your choice: "))
quantity = int(input(f"How many bottles do you want? "))

calc_cost(choice, quantity)

# two

def calc_result(num1, num2, operator):

    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    elif operator == '%':
        if num2 != 0:
            return num1 % num2
        else:
            return "Error: Modulo by zero is not allowed."
        
    else:
        return "Error: Invalid operator. Please use (+, -, *, /, or %):"

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter operator (+, -, *, /, or %): ")

result = calc_result(num1, num2, operator)

print(f"Result: {result}")

# three

def tax_and_net(gross_pay):
    
    if gross_pay >= 40000:
        tax_rate = 0.30
    elif gross_pay >=30000:
        tax_rate = 0.25
    elif gross_pay >= 20000:
        tax_rate = 0.15
    elif gross_pay >= 10000:
        tax_rate = 0.1
    else:
        tax_rate = 0
        
        
    tax_amount = gross_pay * tax_rate
    net_pay = gross_pay - tax_amount
    
    return tax_amount, net_pay

gross_pay = float(input("Enter your gross pay: "))
    
tax_amount, net_pay = tax_and_net(gross_pay)
    
print(f"Tax amount: {tax_amount}")
print(f"Net pay: {net_pay}")
        
        
# four

def compute_numbers(first, second):
    
    if first > second:
        result = first - second
    elif second > first:
        result = first / second
    else:
        result = first + second
        
    return result

    
first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))

result = compute_numbers(first, second)
print(f"Result: {result}")


# five

value = float(input("Enter your value: ")) 
   
if value < 0:
    print("NEGATIVE")
elif value > 0:
    print("POSITIVE")
else:
    print("ZERO")
    
      
# six

def divider(big_num, small_num):
    
    if small_num == 0:
        print("Error: Division by zero is not allowed.")
    elif big_num >= small_num:
        res = big_num / small_num
    else:
        res = small_num / big_num
        
    return res    
    
big_num = float(input("Enter the biggest number: "))
small_num = float(input("Enter the smallest number: "))

res = divider(big_num, small_num)

print(f"Result: {res}")

        