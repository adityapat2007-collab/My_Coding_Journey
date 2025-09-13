from collections import Counter
class Solution:
    def mostFrequentElement(self, nums):
        nums_array = nums.split(" ")
        l=len(nums_array)
        for i in range(l):
            nums_array[i]=int(nums_array[i]) #array ready

        freq=Counter(nums_array)
        print(f"Most frequent element: {freq.most_common(1)[0][0]}")


n = input('Enter elements separated by space: ')
obj = Solution()
obj.mostFrequentElement(n)

