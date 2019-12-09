from sys import argv
from stack_array import *


class Value:

    def __init__(self, in_degree, vertices):
        self.in_degree = in_degree
        self.vertices = vertices
        self.visited = False


def tsort(vertices):
    """
    * Performs a topological sort of the specified directed acyclic graph.  The
    * graph is given as a list of vertices where each pair of vertices represents
    * an edge in the graph.  The resulting string return value will be formatted
    * identically to the Unix utility "tsort".  That is, one vertex per
    * line in topologically sorted order.
    *
    * Raises a ValueError if:
    *   - vertices is emtpy with the message "input contains no edges"
    *   - vertices has an odd number of vertices (incomplete pair) with the
    *     message "input contains an odd number of tokens"
    *   - the graph contains a cycle (isn't acyclic) with the message 
    *     "input contains a cycle"""""
    adjacency = {}
    if len(vertices) == 0:
        raise ValueError("input contains no edges")
    if len(vertices) % 2 != 0:
        raise ValueError("input contains an odd number of tokens")
    lst = []
    for i in range(0, len(vertices) - 1, 2):
        if adjacency.get(vertices[i + 1]) is not None:
            adjacency[vertices[i + 1]].in_degree += 1
        else:
            adjacency[vertices[i + 1]] = Value(1, "")
        if adjacency.get(vertices[i]) is not None:
            if adjacency.get(vertices[i]).vertices != "":
                adjacency.get(vertices[i]).vertices += " "
            adjacency[vertices[i]].vertices += vertices[i + 1]
        else:
            adjacency[vertices[i]] = Value(0, vertices[i + 1])
    s = Stack(len(adjacency))
    for j in adjacency:
        if adjacency.get(j).in_degree == 0:
            adjacency.get(j).visited = True
            s.push(j)
    if s.is_empty():
        raise ValueError("input contains a cycle")
    while not s.is_empty():
        vertex = s.pop()
        verts = adjacency[vertex].vertices
        if verts != "":
            verts = verts.split(" ")
            for i in verts:
                adjacency.get(i).in_degree -= 1
                if adjacency.get(i).in_degree == 0:
                    adjacency.get(i).visited = True
                    s.push(i)
        lst.append(vertex)
    if len(adjacency) > len(lst):
        raise ValueError("input contains a cycle")
    return "\n".join(lst)


def main():
    """Entry point for the tsort utility allowing the user to specify
       a file containing the edge of the DAG"""
    if len(argv) != 2:
        print("Usage: python3 tsort.py <filename>")
        exit()
    try:
        f = open(argv[1], 'r')
    except FileNotFoundError as e:
        print(argv[1], 'could not be found or opened')
        exit()
    
    vertices = []
    for line in f:
        vertices += line.split()
       
    try:
        result = tsort(vertices)
        print(result)
    except Exception as e:
        print(e)


if __name__ == '__main__': 
    main()
