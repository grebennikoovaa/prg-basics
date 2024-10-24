import time

num_to_word = {5: 'five', 4: 'four', 3: 'three', 2: 'two', 1: 'one'}
countdown = int(input("Enter the number of seconds to count down: "))

while countdown > 0:
    if countdown in num_to_word:  
        print(num_to_word[countdown])
    else:
        print(countdown) 
    countdown -= 1
    time.sleep(1)  # Wait for 1 second

print("Time's up!")
