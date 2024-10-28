
n_edges = 4 * 2 # 1 is for single spiral
angle_remeinder = 89 * n_edges

assert n_edges == 8
assert angle_remeinder == 712

edge_size = 10
EDGE_CHANGE = 5

def compute_edge_remeinder(edge_size, EDGE_CHANGE):
    edge_remainder = 0
    for n in range(n_edges):
        edge_remainder += edge_size
        edge_size += EDGE_CHANGE

    return edge_remainder

assert compute_edge_remeinder(edge_size, EDGE_CHANGE) == sum([10, 15, 20, 25, 30, 35, 40, 45]), f"The edge remeinder is {edge_remainder}"# 210 [0, 5, 10, 15, 20, 25, 30, 35]


## question, If a trutle travels the same distance and completes the same rotation, would it end up in the same place if the distance and rotation is randomized in each step??
## basically, the question can be boiled down. Would a turtle end up in the same position and heading, even if we ranomize the movement?
