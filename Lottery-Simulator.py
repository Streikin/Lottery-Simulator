#Please view the readme file to understand how everything works easily
import random
from statistics import mean

# fast lottery: 3 / 70 / 20 / True
# realistic lottery: 5 / 70 / 1 
balls_amount = 3                    
max_number_amount = 70              
lotteries_amount = 20               
print_intermediate_results = True   
# --------------------
if balls_amount >= 4 or max_number_amount >= 49:
    print("Lottery started, this can take a while.")
    print("...")

count = 0
tries = 0
absolute_tries = []

#lottery logic
def lottery(numbers, biggest):
    global count
    count = 0

    drawn = random.sample(range(1, biggest - 1), numbers)
    numbers = random.sample(range(1, biggest - 1), numbers)
    for draw in drawn:
        for number in numbers:
            if number == draw:
              count += 1
    drawn.sort()
    numbers.sort()
    return count

#get multible lotteries results
for i in range(lotteries_amount):
    tries = 0
    count = 0
    while count != balls_amount:
        lottery(balls_amount, max_number_amount)
        tries += 1
    absolute_tries.append(tries)

    if print_intermediate_results or lotteries_amount == 1:
        print("")
        print(f"Lottery {i+1}/{lotteries_amount}:")
        print(f"Tries: {tries}")

print("")
print(f"This lottery had {balls_amount} balls with each having a span of 1-{max_number_amount}.")

#get avg tries
avg_tries = mean(absolute_tries)
if len(absolute_tries) > 1:
    print(f"avg tries: {avg_tries}")
