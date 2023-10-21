import random

def generate_task_code(n=5):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return random.randint(range_start, range_end)