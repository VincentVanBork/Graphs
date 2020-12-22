from graphs import graph, graph_path
from queue import Queue

routes = []
routes_weights = []

def BFS(nodes, starting_node):
    g = graph(nodes)
    print(g.all)
    first_layer = g.all[starting_node]
    current_node = starting_node

    for letter in first_layer:
        routes.append(starting_node)
        routes_weights.append(None)

    print(g.current)

    checking_now = Queue()
    for node in g.current[current_node]:
        checking_now.put(node)

    while not checking_now.empty():
        node = checking_now.get()
        for index, route in enumerate(routes):
            if route[-1] == current_node and (route + node) not in routes:
                routes.append(route+node)
                routes_weights.append(g.get_node(current_node).calculate_distance_to(g.get_node(node)))

        checking_now.task_done()


BFS(5, 'a')
print(routes)
print(routes_weights)

# print("THIS IS NODE", node)
# for route in routes:
#     print("THIS IS PATH", route.order)

#     if route.order[-1] == current_node:
#         if (route.order[-1] + node) 
#         route.value = g.get_node(current_node).calculate_distance_to(g.get_node(node))
#         route.order += node
# for route in routes:
#     print(route.order, route.value)