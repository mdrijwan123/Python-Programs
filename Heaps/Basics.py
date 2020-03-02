import heapq

H = [3,5,8,8,1,2,6,7,4]
heapq.heapify(H)
print(H)
heapq.heappush(H,9)
print(H)
heapq.heappop(H)
print(H)
heapq.heapreplace(H,8)
print(H)