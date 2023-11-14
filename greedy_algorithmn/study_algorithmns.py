import sys
import unittest
from io import StringIO
"""
https://codeforces.com/gym/102951/problem/B
Topic: Greedy sort
B. Studying Algorithms

Steph wants to improve her knowledge of algorithms over winter break.
She has a total of X (1 ≤ X ≤ 104) minutes to dedicate to learning algorithms.
There are N (1 ≤ N ≤ 100) algorithms, and each one of them requires a𝑖 (1 ≤ a𝑖 ≤ 100)
minutes to learn. Find the maximum number of algorithms she can learn.

Input
Line 1: Two space-separated integers N and X (Number of algos and Studying time)
Line 2: N space-separated integers 𝑎1,𝑎2,…𝑎𝑁 (Time takes to study each individual algo)

Output
A single integer, the number of algorithms Steph can study given her time.
"""


def main():

    # Format input
    input1 = [int(number) for number in sys.stdin.readline().split()]
    n, x = input1[0], input1[1]
    algorithm_times = [int(number) for number in sys.stdin.readline().split()]

    # Sort list of algorithm times
    algorithm_times.sort()

    # Count how many
    timeSum = 0
    algoCount = 0

    for time in algorithm_times:

        if (timeSum + time) > x:
            break

        else:
            timeSum += time
            algoCount += 1

    print(algoCount)


class TestCode(unittest.TestCase):

    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()

    def tearDown(self):
        sys.stdin = sys.__stdin__
        sys.stdout = self.held

    def test_main(self):
        test_input = '6 15\n4 3 8 4 7 3\n'
        expected_output = '4\n'

        sys.stdin = StringIO(test_input)
        main()
        actual = sys.stdout.getvalue()

        self.assertEqual(actual, expected_output)
