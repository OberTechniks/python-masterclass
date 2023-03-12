answer = 5
guess = int(input("Please guess a number between 1 and 10"))
if guess < answer: 
    print("Sorry, the correct answer is greater than that")
elif guess > answer: 
    print("Sorry, the correct answer is less than that")
else:
    print("Correct!")

# at the end, print farewell message
print("This was fun. Please try again soon!")

print(2+2, 2, "What does this look like?")