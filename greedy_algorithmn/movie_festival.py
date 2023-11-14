import sys
import unittest
from io import StringIO

"""
https://cses.fi/problemset/task/1629/
Topic: Greedy sort
Movie Festival

In a movie festival n movies will be shown. You know the starting and ending time of each movie. What is the maximum number of movies you can watch entirely?
Input
Line 1: n (int): the number of movies
Remaining  n lines that describe the movies
    Each line has two integers a and b: the starting and ending times of a movie

Output
Print one integer: the maximum number of movies
"""


def main():

    # Format input
    n = int(sys.stdin.readline())  # number of movie inputs
    movies = []

    for _ in range(n):
        movie = [int(num) for num in sys.stdin.readline().split()]  # movie: [start, end]
        movies.append(movie)

    # Sort movies list by end time
    movies.sort(key=lambda movie: movie[1])

    # Count possible movie viewings
    movie_count = 1

    curr_movie_end = movies[0][1]
    for movie in movies[1:]:
        movie_start, movie_end = movie[0], movie[1]

        # Check if viewing is possible
        if curr_movie_end <= movie_start:
            movie_count += 1
            curr_movie_end = movie_end

    print(movie_count)


class TestCode(unittest.TestCase):

    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()

    def tearDown(self):
        sys.stdin = sys.__stdin__
        sys.stdout = self.held

    def test_main(self):
        test_input = '3\n3 5\n4 9\n5 8\n'
        expected_output = '2\n'

        sys.stdin = StringIO(test_input)
        main()
        actual = sys.stdout.getvalue()

        self.assertEqual(actual, expected_output)
