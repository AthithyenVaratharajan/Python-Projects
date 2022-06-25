nums1 = [1,2]
nums2 = [3,4,5,6]




m, n = len(nums1), len(nums2)
sum_idx = m + n
sum = nums1 + nums2
sum.sort()
if sum_idx % 2 != 0:
    middle_idx = sum_idx // 2 
    print(sum[middle_idx])
else:
    middle = (sum[(sum_idx // 2)-1]+sum[sum_idx // 2])/2
    print (float(middle))
