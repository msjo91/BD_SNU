def sums_to(nums, k):
    """
    Take a list of integers and return True if the sum of all the elements in the list is equal to k.
    Return False otherwise.
    """
    if len(nums) == 0:
        if k == 0:
            return True
        else:
            return False
    return sums_to(nums[1:], k - nums[0])
