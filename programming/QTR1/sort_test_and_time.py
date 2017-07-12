"""
Test the sorting algorithm and see how long it takes.
"""
import random
import time

random_items = [random.randint(-50, 100) for c in range(32)]

print('Before : {}'.format(random_items))
start_time = time.clock()
# Insert function here using random_items as argument.
end_time = time.clock()
elapsed_time = end_time - start_time
print('After : {}'.format(random_items))
print("The elapsed time for the function is : {}".format(elapsed_time))
