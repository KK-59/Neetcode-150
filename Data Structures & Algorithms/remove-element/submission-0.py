class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter = 0
        pointer = len(nums) - 1
        i = 0
        while i < len(nums):
            print(i)
            print("point:", pointer) 
            if nums[i] == val:
                print("switch")
                nums[i] = "_"
                temp = nums[i]
                nums[i] = nums[pointer]
                nums[pointer] = temp
                pointer -= 1
                i -= 1
            elif nums[i] == "_":
                break
            else:
                print("here: ", nums[i])
                counter += 1
            i += 1
        print(nums)
        return counter