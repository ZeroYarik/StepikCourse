import matplotlib.pyplot as plt
import networkx as nx
G = nx.Graph()

nodes = ["A", "B", "C", "D", "E", "F", "G"]
edges = [("A", "B"), ("A", "F"), ("B", "C"), ("B", "G"), ("C", "D"), ("C", "E"),
         ("C", "G"), ("D", "E"), ("E", "G"), ("E", "F"), ("F", "G")]

G.add_nodes_from(nodes)
G.add_edges_from(edges)



# # nodes = [1,2,3,4,5,6,7]
# # edges = [(1,2), (1,6), (2,3), (2,7), (3,4), (3,7), (4,5), (5,6), (5,7), (6,7)]

pos = nx.circular_layout(G)

nx.draw(G, pos, with_labels=True)

nx.draw_networkx_edge_labels(
    G, pos,
    edge_labels={
        ("A", "B"): 3, ("A", "F"): 2, ("B", "C"): 3, ("B", "G"): 6, ("C", "D"): 3, ("C", "E"): 2,
         ("C", "G"): 1, ("D", "E"): 5, ("E", "G"): 3, ("E", "F"): 4, ("F", "G"):3,
                 },
    font_color='red'
)

plt.show()
print(list(nx.path_weight(G, ("A","B"), 3)))
#
# # 3 2 4 2 3 6 1 3 5 3 3
#

# f = 1
# x = int(input())
# for i in range(1, x):
#     f = f * i
# print(f)

# Проследите за изменением значений переменных i и j в следующем алгоритме при m=3 и n=4
# m, n = 3, 4
# i = 1
# j = m
# while i != n:
#     i += 1
#     j *= m
# print(j)

# Найдите целые числа, получающиеся в результате работы следующего алгоритма.
# first = 1
# print(first)
# second = 1
# print(second)
# next_i = first + second
# while next_i < 100:
#     print(next_i)
#     first = second
#     second = next_i
#     next_i = first + second

# Проследите эволюцию значений переменных l, sum и k в алгоритме, при n=6
# n = 6
# k = 1
# l = 0
# num_sum = 0
# while k < 2*n:
#     l += k
#     num_sum += l
#     k += 2
# print(num_sum)

