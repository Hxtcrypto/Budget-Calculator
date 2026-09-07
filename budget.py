import math
print("-------Welcome to the Budget Calculator-------")

print("Enter your budget for the month:")
budget= int(input())
print("Choose what you are:")
print("1. Student")
print("2. Working Professional")
print("3. Retired")
choice = int(input("Enter your choice (1-3): "))
if choice == 1:
    print("You are a Student.")
    books_expense = int(input("Enter amount spent on books: "))
    food_expense = int(input("Enter amount spent on food: "))
    print("Living in hostel or at home")
    int(input("Enter 1 for hostel and 2 for home: "))

    if choice == 1:
        print("You are living in a hostel.")
        hostel_expense = int(input("Enter amount spent on hostel: "))
        average_expense = (books_expense + food_expense + hostel_expense) / 3
        print("Average:{average_expense}")
    else:
        print("You are living at home.")
        home_expense = int(input("Enter amount spent according to home: "))


        average_expense = (books_expense + food_expense + home_expense) / 3
    print("Average monthly expense calculated for a student is {monthly_calculator()}".format(monthly_calculator=monthly_calculator()))
elif choice == 2:
    print("You are a Working Professional.")
    rent_expense = int(input("Enter amount spent on rent: "))
    food_expense = int(input("Enter amount spent on food: "))   
    lesuire_expense = int(input("Enter amount spent on leisure: "))
    total_expense = rent_expense + food_expense + lesuire_expense
    average_expense = total_expense / 3
    print("Average monthly expense calculated for a working professional is {}.".format(total_expense))
elif choice == 3:
    print("You are Retired.")
    medical_expense = int(input("Enter amount spent on medical: "))
    travel_expense = int(input("Enter amount spent on travel: "))
    total_expense = medical_expense + travel_expense
    average_expense = total_expense / 2
    print("Average monthly expense calculated for a retired person is {}.".format(budget * 0.3))
else:
    print("Invalid choice. Please select a valid option.")

def monthly_calculator():
    print("Calculating your budget...")
    monthly_expense = budget * 0.5
    print("Your monthly expense is: {}".format(monthly_expense))

print("Enter your amount you want to spend for the month:")
amount_to_spend = int(input())
if amount_to_spend > budget:
    print("Budget exceeded ")
    print("New budget is: {}".format(budget - amount_to_spend))

else:
    print("Congratuilations! You saved  your budget.")

    for i in range(1, 12):
        print("Month {}: You have saved {}".format(i, budget - amount_to_spend))
        print("every month you have saved {}".format(budget - amount_to_spend))
        print("Every month budget is {}".format(budget))

        for j in range(1,31):
            day=int(input("Your daily spending for day {}: ".format(j)))
            budget -= day
            if budget < 0:
                print("You have exceeded your budget for the month.")
                break
            elif budget == 0:
                print("You have reached your budget limit for the month.")
                break
            elif budget > 0:
                print("You have {} left in your budget for the month.".format(budget))
            else:
                print("You have saved your budget for the month.")
                
