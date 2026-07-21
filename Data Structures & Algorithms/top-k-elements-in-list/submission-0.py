class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num not in count:
             count[num] = 0
            count[num] += 1

        freq = [[] for _ in range(len(nums) + 1)]

        for num, c in count.items():
            freq[c].append(num)
    
    
        res =[]

        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

        return sorted(count, key=count.get, reverse=True)[:k]
    

    print(topKFrequent) 





            
