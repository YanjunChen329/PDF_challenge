"""
1A Bucket Challenge
"""

import unittest
import sys
import json


def bucket_challenge_recursion(bucket_sizes, target):
    """
    A recursive solution to the problem: Given an array of bucket sizes and a target
    value, determine whether we could use an integer amount of arbitrary buckets to
    reach the target value. Return 1 if we can and 0 if we can not.
    :param bucket_sizes: an array of bucket sizes
    :param target: the target value
    :return: 1 if we can reach the target value and 0 if we can not
    """
    # Base Case 1: return 0 if target is smaller than 0
    if target < 0:
        return 0
    # Base Case 2: return 1(True) if target is just 0
    elif target == 0:
        return 1
    else:
        # Iterate over all possible solutions and see whether they work
        for size in bucket_sizes:
            if bucket_challenge(bucket_sizes, target - size) > 0:
                return 1  # return 1 if there is a solution
        return 0  # return 0 if there is none


def bucket_challenge(bucket_sizes, target):
    """
    A much more feasible solution to the problem: Given an array of bucket sizes and
    a target value, determine whether we could use an integer amount of arbitrary buckets
    to reach the target value. Return 1 if we can and 0 if we can not.
    :param bucket_sizes: an array of bucket sizes
    :param target: the target value
    :return: 1 if we can reach the target value and 0 if we can not
    """
    value_array = [target]  # This array stores the values that need to be checked

    # Sanity check
    if target < 0:
        return "target value needs to be positive"
    if min(bucket_sizes) < 0:
        return "bucket sizes need to be positive"

    # Iterate over the value array until we find a 0 (a solution) or we find no solutions
    while value_array:
        value = value_array.pop()
        # Iterate over all possible buckets and check if any of them works
        for size in bucket_sizes:
            new_val = value - size
            if new_val < 0:
                continue
            elif new_val == 0:
                return 1
            else:
                value_array.append(new_val)
    return 0


# ------------------------------- Test -------------------------------------


class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(bucket_challenge([5, 7], 13), 0)
        self.assertEqual(bucket_challenge([8, 3], 9), 1)
        self.assertEqual(bucket_challenge([5, 7], 33), 1)
        self.assertEqual(bucket_challenge([3, 14, 18], 19), 0)
        self.assertEqual(bucket_challenge([3, 11, 21], 492), 1)
        self.assertEqual(bucket_challenge([2, 3, 5, 7], 3523), 1)
        self.assertEqual(bucket_challenge([3, 5, 7], 3513423), 1)
        self.assertEqual(bucket_challenge([19, 21, 32], 21332423), 1)
        self.assertEqual(bucket_challenge([134, 23, 57], 563758235), 1)


def run():
    if len(sys.argv) != 3:
        print "Need 2 arguments!"
        return None
    else:
        try:
            buckets = list(json.loads(sys.argv[1]))
            target = int(sys.argv[2])
        except TypeError:
            print "Illegal inputs"
            return None
        print bucket_challenge(buckets, target)


# Run
if __name__ == '__main__':
    run()
    # unittest.main()  # Test

