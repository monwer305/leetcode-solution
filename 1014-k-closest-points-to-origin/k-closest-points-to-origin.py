class Solution:

    def eDistance(self,x2,y2):
        return ((-x2)**2 + (-y2)**2) ** 0.5
        
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []

        for point in points:
            dist = self.eDistance(point[0],point[1])
            heapq.heappush(heap, (-dist,point))

            if len(heap)>k:
                heapq.heappop(heap)
            
        
        return [x[1] for x in heap]
        