"""
Problem 1.Multiples of 3 and 5
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
"""
from time_check import timer


@timer
def find_multiples_sum(num):
	return sum([i for i in range(num) if i % 3 == 0 or i % 5 == 0])


if __name__ == "__main__":
	find_multiples_sum(1000)
