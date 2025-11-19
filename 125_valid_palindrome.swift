func isPalindrome(_ s: String) -> Bool {
    var i = s.startIndex
    var j = s.index(before: s.endIndex)
    var isPali = true

    while (i < j) {
        if (!s[i].isLetter && !s[i].isNumber) {
            i = s.index(after: i)
            continue
        }
        if (!s[j].isLetter && !s[j].isNumber) {
            j = s.index(before: j)
            continue
        }

        if (s[i].lowercased() != s[j].lowercased()) {
            isPali = false
            break
        }

        i = s.index(after: i)
        j = s.index(before: j)
    }
    return isPali
}
