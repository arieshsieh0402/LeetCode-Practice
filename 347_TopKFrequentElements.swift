// Counter
func topKFrequent(_ nums: [Int], _ k: Int) -> [Int] {
    var counter = [Int: Int]()
    var result = [Int]()

    // 計算每個 n 的數量
    for n in nums {
        counter[n, default: 0] += 1
    }

    // 排序字典，回傳由大到小的 array
    var sortedCounterArr = counter.sorted { $0.value > $1.value }

    // 取前 k 的 tuple 的 key
    for i in 0..<k {
        result.append(sortedCounterArr[i].0)
    }

    return result
}