// https://leetcode.com/problems/valid-anagram/description/

// Sorted Array Comparison
// 最直觀的方法是將兩個字串排序後進行比較。如果排序後的字串相同，則回傳 true，否則回傳 false。


func isAnagram(_ s: String, _ t: String) -> Bool {    
    var sArr = Array(s)
    var tArr = Array(t)

    return sArr.sorted(by: >) == tArr.sorted(by: >)
}

// Time Complexity: O(nlogn + mlogm)，其中 n 和 m 分別是字串 s 和 t 的長度。
// Space Complexity: O(n + m)，需要額外的空間來存儲排序後的字串陣列。

// Hash Table Counting
// 使用 Hash Table 來計數每個字母出現的次數。遍歷字串 s，對每個字母進行計數；然後遍歷字串 t，對每個字母進行減計數。
// 如果減去後的計數為 0，則將該 key 從 Hash Table 中移除。最後檢查 Hash Table 是否為空，如果是空的，則回傳 true，否則回傳 false。

func isAnagram(_ s: String, _ t: String) -> Bool {
    guard s.count == t.count else {
        return false
    }

    var counter = [Character: Int]()

    for c in s {
        if let count = counter[c] {
            counter[c] = count + 1
        } else {
            counter[c] = 1
        }
    }

    // 語法糖版本
    // for c in s {
    //     counter[c, default: 0] += 1
    // }

    for c in t {
        if let count = counter[c], count > 0 {
            counter[c] = count - 1
        } else {
            return false
        }
    }
    return true
}

// Time Complexity: O(n)
// Space Complexity: O(n)
// 因為只有長度相同的時候才會初始化 dict，此時 m, n 長度相同, 取一個為代表即可。