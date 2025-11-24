// 49. Group Anagrams
// https://leetcode.com/problems/group-anagrams/description/

// Sort
func groupAnagramsSort(_ strs: [String]) -> [[String]] {
    var groups: [[String]] = []
    var used = Array(repeating: false, count: strs.count)
    let n = strs.count

    for i in 0..<n {
        if used[i] {
            continue
        }
        used[i] = true
        var group = [strs[i]]
        for j in i + 1..<n {
            if !used[j] && strs[i].sorted(by: <) == strs[j].sorted(by: <) {
                group.append(strs[j])
                used[j] = true
            }
        }
        groups.append(group)
    }
    return groups
}

// - Time Complexity: O(n * mlogm)
//     - Where n is the length of strs, m is the longest word in strs.
// - Space Complexity: O(n)


// Hash table + counter
func groupAnagramsHashTable(_ strs: [String]) -> [[String]] {
    var groupsDict = [String: [String]]()

    for s in strs {
        var counter = Array(repeating: 0, count: 26)
        
        for char in s {
            let index = Int(char.asciiValue! - Character("a").asciiValue!)
            counter[index] += 1
        }
        // Swift 不支援動態初始化 tuple，故用 string 當 key
        let key = counter.map { String($0) }.joined(separator: "#")
        groupsDict[key, default: []].append(s)
    }
    return Array(groupsDict.values)

}

// - Time Complexity: O(nm)
//     - Where n is the length of strs, m is the longest word in strs.
// - Space Complexity: O(n)
