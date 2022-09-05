# your code goes here

def sortArrayByParity(nums):
        i  = 0
        j = len(nums)-1
        while(j>=i):
            if(nums[i]%2!=0 and nums[j]%2==0):
                nums[i],nums[j] = nums[j], nums[i]
            if nums[i]%2==0:
                i+=1
            if nums[j]%2!=0:
                j-=1
        return nums
        
nums = list(map(int,input().split()))
print(sortArrayByParity(nums))
