import random

# (a) Tossing a coin 10,000 times
def coin_toss_simulation(n=10000):
    heads, tails = 0, 0
    for _ in range(n):
        toss = random.choice(["H", "T"])
        if toss == "H":
            heads += 1
        else:
            tails += 1
    return heads/n, tails/n

ph, pt = coin_toss_simulation()
print("Probability of Heads:", ph)
print("Probability of Tails:", pt)


# (b) Rolling two dice and probability of getting sum = 7
def dice_sum_simulation(n=10000):
    success = 0
    for _ in range(n):
        die1, die2 = random.randint(1,6), random.randint(1,6)
        if die1 + die2 == 7:
            success += 1
    return success / n

p_sum7 = dice_sum_simulation()
print("Probability of sum = 7:", p_sum7)
