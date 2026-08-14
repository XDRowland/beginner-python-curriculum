nums = [1, 2, 3]
print(nums)

biggest_item = max(nums)
smallest_item = min(nums)

print("The bigest item:", biggest_item)
print("The smallest item:", smallest_item)

print("Our algorithom")

biggest = nums[0]
for i in range(len(nums)):
    if nums[i] > biggest:
        biggest = nums[i]
        
print("The biggest item:", biggest)