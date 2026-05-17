
class WordFreq:
    def __init__(self,count,word):
        self.count = count
        self.word = word

    def __lt__(self,other):
        if self.count == other.count:
            return self.word > other.word
        return self.count < other.count
    def __eq__(self,other):
        self.count == other.count and self.word == other.word
class Solution:

    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        hash_map = defaultdict(int)
        for word in words:
            hash_map[word]+=1
        
        heap = []
        for word in hash_map:
            new_word = WordFreq(hash_map[word],word)
            heapq.heappush(heap,(new_word))

            if len(heap)> k:
                heapq.heappop(heap)
        
        heap.sort(reverse =True)


        return [x.word for x in heap]


        