def prob_at_least_one_six(trials=10000):
    success = 0
    for _ in range(trials):
        has_six = False
        for _ in range(10):  # roll 10 times
            if random.randint(1,6) == 6:
                has_six = True
                break
        if has_six:
            success += 1
    return success / trials

p = prob_at_least_one_six()
print("Probability of at least one '6' in 10 rolls:", p)
