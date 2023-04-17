def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """

    # hashmap count first
    count = {}
    for n in nums:
        count[n] = 1 + count.get(n, 0)

    # create second freq list, put count into freq
    freq = [[] for i in range(len(nums)+1)]
    for num, c in count.items():
        freq[c].append(num)

    print(freq)
    # go through the freq and get the largest K to output
    res = []
    for i in range(len(freq)-1, -1, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res

    # return output


print(topKFrequent([1, 1, 1, 2, 2, 3, 4], 2))
