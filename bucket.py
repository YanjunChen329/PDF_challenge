def bucket_challenge(bucket_sizes, target):
    if target < 0:
        return 0
    elif target == 0:
        return 1
    else:
        result = []
        for size in bucket_sizes:
            result.append(bucket_challenge(bucket_sizes, target - size))
        return sum(result) > 0


print bucket_challenge([5, 7], 33)
