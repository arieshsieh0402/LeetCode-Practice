import collections
import heapq
from typing import List


def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    # 用來存儲圖中資訊，key為起點，value為(終點, 耗時)的 list
    edgeMap = collections.defaultdict(list)
    for start, end, time in times:
        edgeMap[start].append((end, time))
    
    # 使用 minHheap 實作 Dijkstra 算法，heap 中元素為: (從起點到當前節點的耗時, 當前節點)
    minHeap = [(0, k)]
    # 記錄已訪問的節點，避免重複處理
    visited = set()
    # 記錄到達所有節點所需的最長時間
    longestTime = 0

    while minHeap:
        # 取出耗時最短的路徑
        currTime, currNode = heapq.heappop(minHeap)
        if currNode in visited:
            continue
        visited.add(currNode)
        # 更新到達所有節點所需的最長時間
        longestTime = max(longestTime, currTime)

        # BFS 訪問當前節點的所有連接節點
        for nextNode, timeToNext in edgeMap[currNode]:
            if nextNode not in visited:
                heapq.heappush(minHeap, (currTime + timeToNext, nextNode))
    
    return longestTime if len(visited) == n else -1