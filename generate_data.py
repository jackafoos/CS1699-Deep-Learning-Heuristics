import numpy as np
import csv

"""
generate graphs(path, num)
path := what file to store the graphs
num := how many graphs to generate
This function will iteratively generate num graphs, run them through the
heuristics and store the tuple with graph and class scores in path.
"""
def generate_graphs(path, num):
    print('Generating Data for {}'.format(path))
    g_list = []
    for i in range(num):
        if i % (num/10) == 0:
            print('{}% Generated:'.format(int(i/num * 100)))
        n = 50
        rand = np.random.uniform(0,100, int(n*(n-1)/2))
        graph = np.zeros((n, n))
        graph[np.triu_indices(n, 1)] = rand
        graph[np.tril_indices(n, -1)] = graph.T[np.tril_indices(n, -1)]
        scores = get_graph_class_scores(graph)
        g_list.append(scores)
    with open(path, 'w') as csvfile:
        wr = csv.writer(csvfile)
        wr.writerow(['graph','Nearest Neighbor', 'Christofides', 'Greedy', 'Nearest Insertion'])
        for row in g_list:
            wr.writerow(row)


"""
get_graph_class_scores(graph)
graph := the graph being tested.
This tests all 4 heuristics on the graph and generates the class scores tuple
"""
def get_graph_class_scores(graph):
    nn_score, cf_score, gd_score, ni_score = 0, 0, 0, 0
    nn_res = nearest_neighbor(graph)
    ch_res = christofides(graph)
    gd_res = greedy(graph)
    ni_res = nearest_insertion(graph)
    if nn_res <= ch_res and nn_res <= gd_res and nn_res <= ni_res:
        nn_score = 1
    elif ch_res <= nn_res and ch_res <= gd_res and ch_res <= ni_res:
        ch_score = 1
    elif gd_res <= nn_res and gd_res <= ch_res and gd_res <= ni_res:
        gd_score = 1
    elif ni_res <= nn_res and ni_res <= ch_res and ni_res <= gd_res:
        ni_score = 1
    return (graph, nn_score, cf_score, gd_score, ni_score)

"""
Nearest Neighbor picks a starting node in 'graph' and iteratively finds the nearest
unselected adjacent node and adds it next in the tour.
Returns the total distance for the tour.
"""
def nearest_neighbor(graph):
    raise NotImplementedError

"""
Christofides builds a minimum spanning tree from all nodes. Then it creates a minumum
weight matching on the set of nodes having an odd degree and adds it with the MST.
Creates an Euler cycle from the combined graph.
Returns the total distance for the tour.
"""
def christofides(graph):
    raise NotImplementedError

"""
The Greedy algorithm flattens the graph and removes duplicate edges. Then select
the shortest edge and make sure that it doesnt make a cycle with < N edges. Either
repeat or stop when N edges are added.
Returns the total distance for the tour.
"""
def greedy(graph):
    raise NotImplementedError

"""
Nearest Insertion selects the shortest edge and makes a subtour of it. Then select
a city not in the subtour with the shortest edge connecting to one of the cities
in the subtour. Then find an edge in the subtour such that the cost of insertion
is minimal.
Returns the total distance for the tour.
"""
def nearest_insertion(graph):
    raise NotImplementedError


# Generate Graphs for training and test data
generate_graphs('training_graphs.csv', 9000)
generate_graphs('validation_graphs.csv', 1000)
generate_graphs('testing_graphs.csv', 4000)
