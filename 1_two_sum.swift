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
