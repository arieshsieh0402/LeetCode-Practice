// 217_contains_duplicate

// Brute force

/*
    這題最直觀的方式是使用兩層迴圈，外層迴圈遍歷陣列中的每個元素，內層迴圈檢查該元素是否在剩餘的元素中出現過。
    如果找到了相同的元素，就返回 true；如果遍歷完所有元素都沒有找到重複的，則返回 false。
*/

// Brute force

func containsDuplicate(_ nums: [Int]) -> Bool {
    let n = nums.count
    for i in 0..<(n - 1) {
        for j in (i + 1)..<n { 
            if nums[i] == nums[j] {
                return true
            }
        }
    }
    return false
}

// 使用 enumerated() 或 dropFirst()

/*
    外層迴圈使用 enumerated() 來獲取當前元素的索引和值，內層迴圈使用 dropFirst() 方法來跳過已經檢查過的元素。
    這樣可以使程式碼更簡潔易讀。
    而因為 Array 符合 RandomAccessCollection（隨機存取集合）協議，故不論 drop 多少個，時間複雜度都是 O(1)。
    此處也不會消耗額外的記憶體空間，因為 dropFirst() 並不會創建新的陣列。
*/

func containsDuplicate2(_ nums: [Int]) -> Bool {
    for (i, num1) in nums.enumerated() {
        for num2 in nums.dropFirst(i + 1) {
            if num1 == num2 {
                return true
            }
        }
    }
    return false
}

// Hash Table

/*
    使用 Hash Table 來記錄已經出現過的元素。
    遍歷陣列中的每個元素，檢查該元素是否已經存在於 Hash Table 中。
    如果存在，則表示有重複元素，返回 true；如果不存在，則將該元素加入 Hash Table。
    最後如果遍歷完所有元素都沒有找到重複的，則返回 false。
*/

func containsDuplicateHashTable(_ nums: [Int]) -> Bool {
    // Hash table

    var numsDict = [Int: Int]() 

    for num in nums {
        if numsDict[num] != nil {
            return true
        }
        numsDict[num] = 1
    }
    return false
}