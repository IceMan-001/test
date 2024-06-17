import random
from collections import deque
from benchmark import benchmark
from memory_profiler import profile

elements = list(range(10**7))
random.shuffle(elements)

list_elements = list(elements)
deque_elements = deque(elements)

print("search")


@benchmark(repeat=100)
def list_search(data):
    element = random.choice(data)
    return data.index(element)


@benchmark(repeat=100)
def deque_search(data):
    element = random.choice(data)
    return data.index(element)


for _ in range(10):
    list_search(list_elements)
    deque_search(deque_elements)



# tasks = deque(range(1, 51), maxlen=10)
# tasks.append(51)
# # tasks.rotate(5)
# # tasks.reverse()
# print(tasks)
