import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_LINE = 6

num_quick_picks = int(input("How many quick picks? "))
for random_num in range(num_quick_picks):
    quick_pick = sorted(random.sample(range(MIN_NUMBER, MAX_NUMBER + 1), NUMBERS_PER_LINE))
    print(" ".join(f"{num:2}" for num in quick_pick))
