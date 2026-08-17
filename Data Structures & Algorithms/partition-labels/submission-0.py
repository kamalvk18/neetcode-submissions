class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_char_map = defaultdict(int)
        for i, c in enumerate(s):
            last_char_map[c] = i

        partitions = []
        cnt = 0
        curr_boundary = 0
        for i, c in enumerate(s):
            cnt += 1
            curr_boundary = max(curr_boundary, last_char_map[c])
            if curr_boundary <= i:
                partitions.append(cnt)
                cnt = 0

        return partitions