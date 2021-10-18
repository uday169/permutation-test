# check possible permutation for string and numbers

def stringPermutation(string, i=0):
    if i == len(string):
        print("".join(string))

    for j in range(i, len(string)):
        words = [c for c in string]
        # swapping elements in this way, we achieve all different combinations of characters.
        words[i], words[j] = words[j], words[i]
        stringPermutation(words, i + 1)


def permutation(nums):
    # Remove space from list
    nums = ' '.join(nums).split()
    # checking given list is numbers or string
    mynewlist = [s for s in nums if s.isdigit()]
    if len(mynewlist) == 0:
        result = []
        result.append(stringPermutation(nums))
        return result
    else:
        # If nums is empty then there are no permutations will available
        if len(nums) == 0:
            return []
        # If there is only one element in nums then, one permutation is possible
        if len(nums) == 1:
            return [nums]
        res = [] # empty list that will store current permutation
        #  Iterating the nums to calculate the permutation
        for n in range(len(nums)):
            rem = nums[n]
            # Extract num[n] or rem from the list.  remList is remaining list
            remList = nums[:n] + nums[n + 1:]
            # Generating all permutations where rem is first element
            for per in permutation(remList):
                res.append([rem] + per)
        return res

data = list('123 ') #input ABC, AB C , 123
# printing the each permutation
for p in permutation(data):
    print(p)