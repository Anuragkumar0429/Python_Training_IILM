class Solution:
    def merge(self, intervals):
        # Step 1: sort by start time
        intervals.sort()

        merged = []

        for interval in intervals:
            # if merged is empty OR no overlap
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # overlap → merge
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
