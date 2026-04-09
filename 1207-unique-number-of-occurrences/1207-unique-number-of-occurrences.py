from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}

        # Step 1: Count frequency of each number
        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        # Step 2: Check if frequencies are unique
        occurrences = freq.values()

        return len(occurrences) == len(set(occurrences))