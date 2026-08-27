#Discount Calculator
def calculate_discount(price,discount_percent):
    amount=price-(price*discount_percent/100)
    return amount
discounted_price=calculate_discount(10,2)
print(discounted_price)
#Arthmetric Calculator
def numbi(numberlist):
    summy=sum(numberlist)
    average=summy/len(numberlist)
    max_numbi=max(numberlist)
    min_numbi=min(numberlist)
    return summy,average,max_numbi,min_numbi
sumsum, avg, max_num,min_num=numbi([1,2,3,4])
print(sumsum)#10
print(avg)#2.5
print(max_num)#4
print(min_num)#1
#Employees and their Department
def companyxyz(employees):
    departments=[]
    for emp in employees:
        departments.append(emp)
    return departments
employees =[{"name":"Janardan Seth", "department":"Accounting"},{"name":"Andrew Simmons", "department":"Engineer"},{"name":"David Johnson", "department":"HR"}]
employed=companyxyz(employees)
print(employed)
#Reading a list of products and returning under a certain price#
def cars_list(cars,max_price):
    garage = []
    for car in cars:
        if car["price"] < max_price:
            garage.append(car)
    return garage
cars = [{"car model":"Ford Mustang","price":33000},{"car model":"Jeep Wrangler","price":36035},{"car model":"Dodge Charger","price":50000},{"car model":"Jeep Gladiator","price":40000}]
available = cars_list(cars, 45000)
print(available)
#Write a function that processes a list of sales data and returns total revenue#
def calculate_revenue(sales):
    total = 0
    for sale in sales:
        total += sale["amount"]
    return total
sales = [{"product":"Laptop","amount":1200},{"product":"Phone","amount":800},{"product":"Headphones","amount":150},{"product":"Monitor","amount":300}]
revenue = calculate_revenue(sales)
print(revenue)

