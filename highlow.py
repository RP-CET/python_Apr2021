import random

low = 1
high = 20
secret = random.randint(1, 20)

tries = 1
while tries < 7:
    hint = "Enter a number between " + str(low) + " and " + str(high) + " : "
    user_guess = int(input(hint))
    if user_guess > secret:
        high = user_guess
        print ("Too High")
    elif user_guess < secret:
        low = user_guess
        print("Too Low")
    else:
        print ("You have guessed correctly!")
        print ("You've got it at the %dth try" % (tries))
    
    tries = tries + 1
    
if tries == 7:
    print ("You didn't get it in 6 tries. The secret number is " + str(secret))
    
    
