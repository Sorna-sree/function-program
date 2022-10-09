
# Calculate the cost of train tickets. Single one way ticket from Madurai to Chennai (or vice versa) is Rs1000.  
# Adding a return ticket will cost Rs750 extra. 
# Family of 4 or more gets 20% off. Senior rate is 50% off. 

one_way_cost = 1000
return_cost = 750

def cal(count,cost) :
    SeniorPassenger_count = senior_count(count)
    temp_cost = count * cost

    if count >= 4 : 
        discount_amount = dis_cal(20,temp_cost)
        temp_cost = temp_cost - discount_amount

    senior_discount = dis_cal(50,cost)
    total_senior_discount = SeniorPassenger_count * senior_discount
    total_cost = temp_cost - total_senior_discount

    return total_cost

def senior_count(counts) :
    senior_passenger_count = 0
    for i in range(counts) :
        age = int(input(f"Enter age of person {i+1} : "))
        if age >= 60 :
            senior_passenger_count = senior_passenger_count + 1
    
    return senior_passenger_count

def dis_cal(discount_per, amt) :
    dis_amt = (discount_per * amt) / 100
    return dis_amt

print("Welcome to Python Railay Ticket Booking")
count = int(input("Enter Total Number of Passengers : "))

total_oneway_cost = cal(count,one_way_cost)

print(f"Total Amount as Oneway trip for {count} Passengers is : Rs.{total_oneway_cost}")

return_ans = input("Do you want to Book Return Ticket? 1. YES    2. NO      ")
if return_ans == "YES" or return_ans == "yes" or return_ans == "Yes" :
    return_ans2 = input("Do you want to Book Return Ticket for all the passengers ? 1. YES    2. NO     ")
    total_return_cost = 0
    if return_ans2 == "YES" or return_ans2 == "yes" or return_ans2 == "Yes" :
        total_return_cost = cal(count,return_cost)
    else :
        return_count = int(input("Enter number of Return Tickets :"))
        total_return_cost = cal(return_count,return_cost)

total_cost = total_oneway_cost + total_return_cost
print(f"The Total Ticket Amount for {count} Passengers is : Rs.{total_cost}")