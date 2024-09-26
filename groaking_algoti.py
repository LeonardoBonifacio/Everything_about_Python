from collections import deque

def countdown(i):
    print(i)
    if i <= 0:
        return
    else:
        countdown(i - 1)

def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)


def sum_array(array):
    if array == []:
        return 0
    else:
        return array[0] + sum_array(array[1:])

def count(lista):
    if lista == []:
        return 0
    return 1 + count(lista[1:])


def max(lista):
    if len(lista) == 2:
        return lista[0] if lista[0] > lista[1] else lista[1]    
    
    sub_max = max(lista[1:])
    return lista[0] if lista[0] > sub_max else sub_max

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i < pivot]
        greater = [i for i in array[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)
    


graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def person_is_seller(person):
    return person[-1] == "m"

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(f"{person} is a mango seller")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

graph_weight = {}
graph_weight["start"] = {}
graph_weight["start"]["a"] = 6
graph_weight["start"]["b"] = 2
graph_weight["a"] = {}
graph_weight["a"]["fin"] = 1
graph_weight["b"] = {}
graph_weight["b"]["a"] = 3
graph_weight["b"]["fin"] = 5
graph_weight["fin"] = {}

infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity


parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

processed = []


def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph_weight[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

# countdown(50)
# print(fact(10))
# print(sum_array([1, 2, 3]))
# print(count([1, 2, 3]))
# print(max([1, 2, 3, 4, 5, 6]))
print(quicksort([10, 5, 2, 3]))
