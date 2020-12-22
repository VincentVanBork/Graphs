from graphs import graph, graph_path
from queue import Queue

routes = []
routes_weights = []

def BFS(g, current_node):
    layer = g.all[current_node]
    checking_now = Queue()
    for node in g.current[current_node]:
        checking_now.put(node)

    g.remove_node(current_node)

    while not checking_now.empty():
        
        node = checking_now.get()
        for index, route in enumerate(routes):
            if route[-1] == current_node and (route + node) not in routes:
                routes.append(route+node)
                routes_weights.append(routes_weights[index]+g.get_node(current_node).calculate_distance_to(g.get_node(node)))
        
        checking_now.task_done()

    g.reset_graph()
        
    

g = graph(4)
print('all', g.all)
print('current', g.current)
starting_node = 'a'
first_layer = g.all[starting_node]

for letter in first_layer:
    routes.append(starting_node)
    routes_weights.append(0)

print('----------------------------')
BFS(g, 'a')
print(routes)
print('all', g.all)
print('current', g.current)

print('----------------------------')
BFS(g, 'b')
print(routes)
print('all', g.all)
print('current', g.current)
# print(routes_weights)
