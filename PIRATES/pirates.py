import math

temp = input("")
N = int(temp.split(" ")[0])
M = int(temp.split(" ")[1])
Q = int(temp.split(" ")[2])

# map and searching class
class mapping:
    def __init__(self, topo):
        self.topo = topo

    def cost_function(self, x_curr, y_curr, x, y, cost_curr):
        if self.topo[x_curr][y_curr]:
            return cost_curr
        elif not self.topo[x_curr][y_curr]:
            if self.topo[x][y] == self.topo[x_curr][y_curr]:
                return cost_curr
            else:
                return cost_curr+1

    def goal_dist(self, x, y, x_goal, y_goal):
        return (math.fabs(x_goal-x)+math.fabs(y_goal-y))


# import and prepare the map
treasure_map = []
for line in range(0, N):
    row = list(input(""))
    row = [int(ord(x) == 79) for x in row]
    treasure_map.append(row)
chart = mapping(treasure_map)

cost = [[100]*M]*N
# process the Q queries
for query in range(0, Q):
    temp = input("")
    x1 = int(temp.split(" ")[0])
    y1 = int(temp.split(" ")[1])
    x2 = int(temp.split(" ")[2])
    y2 = int(temp.split(" ")[3])
    # initialize first point as start point
    x_curr = x1; y_curr = y1; cost[x1][y1] = 0;
    TREASURE = False
    while not TREASURE:
        min_cost = 10000; candidates = [];
        # scan the neighbours
        for i in range(-1,2):
            if TREASURE:
                break
            for j in range(-1,2):
                if i or j:
                    x = x_curr + i; y = y_curr + j;
                    if x == x2 and y == y2:
                        TREASURE = True
                        break
                    if x < 0 or y < 0 or x > M or y > N:
                        break
                    # check the cost function and save value for neighbours
                    cost[x][y] = chart.cost_function(x_curr, y_curr, x, y, cost[x_curr][y_curr])
                    if cost[x][y] < min_cost:
                        candidates = []
                        min_cost = cost[x][y]
                        candidates.append([x,y])
                    elif cost[x][y] == min_cost:
                        candidates.append([x,y])
        # update x_curr, y_curr to be new source
        
        # min_dist = 10000
        # for can in candidates:
        #     dist = chart.goal_dist(can[0], can[1], x2, y2)
        #     if dist < min_dist:
        #         x_curr = can[0]; y_curr = can[1]

    print(cost[x2][y2])
