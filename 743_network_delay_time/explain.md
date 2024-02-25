# 題目連結

https://leetcode.com/problems/network-delay-time/description/

# 解題思路

1. 從起點開始，並搭配 BFS，一層一層地拜訪從起點開始到其相鄰的 nodes，並記錄路徑權重（從起點開始的加總）以及到達的點。接著從這些 nodes 中，我們只拜訪最短距離的那個 node。為了達到這一點，可以用 min heap 來實作。

2. 持續拜訪直到 graph 中每個點都拜訪過，並回傳最後一次拜訪 node 所記錄的距離權重。

# 複雜度分析

- Time Complexity: $O(ElogV)$
    1. 初始化 edges，耗時 $O(E)$。
    2. 在最壞情況下，每條邊都會被插入到 heap 中一次。 Heap 操作的時間複雜度是 $logV$，其中$V$ 是節的數量。因此，對於所有的邊，這部分的時間複雜度為 $O(ElogV)$。
    3. 最後時間複雜度取較高的 $O(ElogV)$。
- Space Complexity: $O(E+V)$
    1. **edges**：空間複雜度為 *O*(*E*)。
    2. minHeap：在最壞的情況下包含所有的邊，因此空間複雜度為 $*O(E)*$。
    3. visit： $*O(V)*$。
    4. 總的空間複雜度為 $*O(E+V)*$。
