# Calculate the cost flight tickets. Single one way ticket from Madurai to Chennai (or vice versa) is Rs 3500 for
# weekday morning and afternoon flights. Rs 3000 for weekday evening flights. Rs 5000 for weekends. Senior discout is 10%.
# Tickets bought at least two weeks ahead of time is 20% off.
# Print the number of weekend tickets sold in a given day.

from datetime import datetime , date

senior_count = 0 
weekend_count = 0

def choice(): # this function is used for display the offer 
    print("---------------------------Our Offers------------------------\n")
    print("Senior Ticket per head 10% off")
    print("Book your tickets 2 weeks before and get 20% off\n")
    print("If you are Travelling During...\n")
    print("1. WEEKDAYS MORNING TRAVEL OR WEEKDAYS AFTERNOON TRAVEL -> INR 3,500\n")
    print("2. WEEKDAYS EVENING TRAVEL -> INR 3,000\n")
    print("3. WEEKEND DAYS TRAVEL -> INR 5,000\n")
    user_choice = int(input("Enter your choice (1 to 3) : ")) #input for user choice
    return user_choice

print("\nWelcome to Python Flight Ticket Booking\n")
today_date = str(date.today())
print("Today date : ",today_date)

travel_date = input("Enter the Travel Date (year-month-day) : ") #input for travel date
today_date = datetime.strptime(today_date, "%Y-%m-%d") #convert to the today date in time
travel_date = datetime.strptime(travel_date, "%Y-%m-%d")
total_persons = int(input("Enter Total count of Passengers :  ")) #tptal person count

for index in range(0,total_persons): #calculate the senior count
    age = int(input(f"Enter age of person {index+1} : "))
    if(age >= 60):
        senior_count += 1

user_choice = choice() # call for choice function
 
if(user_choice == 1): #calculate the discount for WEEKDAYS MORNING TRAVEL OR WEEKDAYS AFTERNOON TRAVEL
    cost = (total_persons - senior_count) * 3500
    senior_cost = (3500 - (10 * 3500)/100) * senior_count
    cost += senior_cost
elif(user_choice == 2): #calculate the discount for WEEKDAYS EVENING TRAVEL -> INR 3,000
    cost = (total_persons - senior_count) * 3000
    senior_cost = (3000 - (10 * 3000)/100) * senior_count
    cost += senior_cost
elif(user_choice == 3): #calculate the discount for WEEKEND DAYS TRAVEL
    cost = (total_persons - senior_count) * 5000
    senior_cost = (5000 - (10 * 5000)/100) * senior_count
    cost += senior_cost
    weekend_count +=1 # count the weekend count
else:
    print("Invalid Input !")

date_limit = (travel_date - today_date) #calculate the  the day of two weeks ahead
date_limit = int((f'{date_limit.days}'))


if(date_limit >= 14): #Tickets bought at least two weeks ahead of time is 20% off.
    cost = (cost - (20 * cost) /100)

print("Total Ticket Amount : " ,cost)  #print the cost of the ticket
print("Weekend Tickets sold in this day : " ,weekend_count) 