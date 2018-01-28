def bucket_challenge(bucket_sizes, target):
    """
    Given an array of bucket sizes and a target value, determine whether we could
    use an integer amount of arbitrary buckets to reach the target value. Return 1
    if we can and 0 if we can not.
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
        result = []
        # Iterate over all possible solutions and see whether they work
        for size in bucket_sizes:
            result.append(bucket_challenge(bucket_sizes, target - size))
        return int(sum(result) > 0)  # Return 1 if there exists more than 0 solutions


print bucket_challenge([5, 7], 33)
