from math import ceil
import random
from time import sleep

def generate_even_numbers(max):
    for i in range(0, max+1, 2):
        yield i



def read_file_lines(file_path):
    with open(file_path, "r") as file:
        for line in file:
            yield line.strip()


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        next_value = a+b
        a = b
        b = next_value


def batch_generator(batch_list, batch_size):
    start = 0
    for _ in range(0, len(batch_list), batch_size):
        yield batch_list[start: start+batch_size]
        start += batch_size


def is_prime(n):
	for i in range(2, int(n ** 0.5) + 1):
		if n % i == 0:
			return False
	return True


def prime_numbers():
    prime = 0
    while True:
        if is_prime(prime):
            yield prime 
        prime += 1


def sensor_data_stream(min_value, max_value, interval):
    while True:
        yield random.randint(min_value, max_value)
        sleep(interval)
 

def process_logs(file_path, keyword):
    with open(file_path, "r") as logFile:
        for log in logFile:
            if keyword in log:
                yield log

