def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """

    highest_index = len(nums)
    result = ()
    dict_of_indexs = {}
    for index in range(len(nums)):
        dict_of_indexs[nums[index]] = index
    
    for num in dict_of_indexs.keys():
        target_num = goal - num
        
        if dict_of_indexs.get(target_num, -1) != -1:
            num1_index = dict_of_indexs[num]
            num2_index = dict_of_indexs[target_num]
            test_high_index = max(num1_index, num2_index)

            if test_high_index < highest_index:
                result = (num, target_num)
                highest_index = test_high_index

    return result





# sum_pairs([5, 1, 4, 8, 3, 2], 7)