print("Guess the Number between 1 and 100:")
while True:
    number=int(input("Enter a number:"))
    if number == 51:
        print("Congratulations you found it!")
        break
    elif number > 51:
        print("Way too high")
    elif number < 51:
        print("Way too low")
    else:
        print("Please enter a number")
        
        
