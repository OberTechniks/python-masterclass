answer = 5
guess = int(input("Please guess a number between 1 and 10"))
if guess < answer: 
    print("Sorry, the correct answer is greater than that")
elif guess > answer: 
    print("Sorry, the correct answer is less than that")
else:
    print("Correct!")
