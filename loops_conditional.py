#Ask User for age and print if they can vote
age= int(input("Enter your age:"))
if age < 18:
    print("You can't vote:")
else:
    print("You can vote:")

#Loop through numbers 1-10 and print even numbers
for i in range(11):
    if i%2==0:
        print(i)

#List of employees and printing those with salaries over 60,00
employee_salary=[64310,58988,94426,44900,105000]
for i  in range(len(employee_salary)):
    if employee_salary[i] > 60000:
        print(employee_salary[i])

#Using nested loops to print a 3x3 grid of *
for x  in range(1):
    print("***")
    for y in range(2):
        print("***")

#Loop through list to find target item
shoppinglist=["Milk","Eggs","Bread","Apple","Butter"]
print(shoppinglist)
target_item="Bread"
for i  in range(len(shoppinglist)):
    if shoppinglist[i] == target_item:
        print(target_item+" is the target item")
        break
