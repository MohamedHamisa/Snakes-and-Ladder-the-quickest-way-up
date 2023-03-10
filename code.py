class Graph:
    def __init__(self, ladders, snakes):
        self.adj_list = {i:set() for i in range(100)}
        special = {v-1:w-1 for v, w in ladders}
        special.update({v-1:w-1 for v, w in snakes})
        for i in range(99):
            for j in range(i+1, min(100, i+7)):
                if i in special:
                    continue
                self.adj_list[i].add(special.get(j, j))

            
    def bfs(self):
        q = deque([(0, 0)])
        vis = set([0])
        while q:
            dist, v = q.popleft()
            if v == 99:
                return dist
            for u in self.adj_list[v]:
                if not u in vis:
                    vis.add(u)
                    q.append((dist+1, u))
        return -1
                    
             
def quickestWayUp(ladders, snakes):
    g = Graph(ladders, snakes)
    return g.bfs()


