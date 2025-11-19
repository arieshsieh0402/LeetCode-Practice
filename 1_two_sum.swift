func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
  for i in 0..<nums.count {
    var complement = target - nums[i]
    for j in i + 1..<nums.count {
      if nums[j] == complement {
        return [i, j]
      }
    }
  }
  return []
}

// Example usage:
let nums = [2, 7, 11, 15]
let target = 9
let result = twoSum(nums, target)
print(result)  // Output: [0, 1]