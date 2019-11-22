import numpy as np


def generate_random_segment():
    x = np.float16(np.random.randint(-100.00, 100.00, 100))
    index = (list(enumerate(x)))
    return x, index


print(generate_random_segment())
