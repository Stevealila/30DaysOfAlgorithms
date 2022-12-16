def containsDuplicates (arr):

    hm = {}

    for n in arr:
        if n in hm: return True
        hm[n] = n 

    return False



nums = [1,2,3,1]
print(containsDuplicates(nums)) #true
nums = [1,2,3,4]
# containsDuplicates(nums)
print(containsDuplicates(nums)) #false
nums = [1,1,1,3,3,4,3,2,4,2]
print(containsDuplicates(nums)) #true