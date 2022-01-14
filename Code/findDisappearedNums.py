def findDisappearedNums(nums):
    """
    (nums List[int] -> disappearedNums List[int])
    Given an array nums of n integers where nums[i] is in the range [1,n],
    return an array of all the integers in the range [1,n]
    that do not appear in nums.
    """
    disappearedNums = []
    n = len(nums)
    
    for i in range(1,n+1):
        if i not in nums:
            disappearedNums.append(i)

    print(str(disappearedNums) + "\n")

findDisappearedNums([1, 2, 3, 5, 8, 9, 3, 1])
# [4, 6, 7]
findDisappearedNums([4, 3, 2, 7, 8, 2, 3, 1])
# [5, 6]
findDisappearedNums([1, 9, 8, 5])
# [2, 3, 4]
findDisappearedNums([1, 1])
# [2]
