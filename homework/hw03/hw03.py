(a, b) = (2.1, 2.9)
assert (round( a), round( b)) == ( 2,  3), "test 01.a failed"
assert (round(-a), round(-b)) == (-2, -3), "test 01.b failed"
assert (int  ( a), int  ( b)) == ( 2,  2), "test 02.a failed"
assert (int  (-a), int  (-b)) == (-2, -2), "test 02.b failed"
assert (list(range(12, 16)) == [12, 13, 14, 15]), "test 03.a failed"
assert (list(range(0, 10, 2)) == [0, 2, 4, 6, 8]), "test 03.b failed"
assert (list(range(5, -1, -1)) == [5, 4, 3, 2, 1, 0]), "test 03.c failed"
import random
assert 1 <= random.randint(1, 10) <= 10, "test 04.a failed"
assert random.randint(1, 2) in [1, 2], "test 04.a failed"
