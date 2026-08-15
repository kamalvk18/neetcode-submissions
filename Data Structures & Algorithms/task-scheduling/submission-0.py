class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        q = deque()
        time = 0

        while maxHeap or q:
            time += 1
            while q and q[0][0] == time:
                _, cnt = q.popleft()
                heapq.heappush(maxHeap, cnt)

            if maxHeap:
                cnt = heapq.heappop(maxHeap)
                cnt += 1
                if cnt == 0:
                    continue
                q.append((time + n + 1, cnt))

        return time

            
