import random

def bag_simulation(trials=10000):
    balls = ["R"]*5 + ["G"]*7 + ["B"]*8
    prev_blue = 0
    red_given_blue = 0
    
    for _ in range(trials):
        prev = random.choice(balls)
        curr = random.choice(balls)
        
        if prev == "B":
            prev_blue += 1
            if curr == "R":
                red_given_blue += 1
    
    return red_given_blue/prev_blue if prev_blue else 0

p_red_given_blue = bag_simulation(100000)
print("P(Red | Previous Blue):", p_red_given_blue)
