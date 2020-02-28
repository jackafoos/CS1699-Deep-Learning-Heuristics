import numpy as np

"""
generate graphs(path, num)
path := what file to store the graphs
num := how many graphs to generate
This function will iteratively generate num graphs, run them through the
heuristics and store the tuple with graph and class scores in path.
"""
def generate_graphs(path, num):
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
        glist.append(scores)


"""
get_graph_class_scores(graph)
graph := the graph being tested.
This tests all 4 heuristics on the graph and generates the class scores tuple
"""
def get_graph_class_scores(graph):
    raise NotImplementedError

# Generate Graphs for training and test data
generate_graphs("", 10000)
