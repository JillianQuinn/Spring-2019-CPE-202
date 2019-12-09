from stack_array import * # Needed for Depth First Search
from queue_array import * # Needed for Breadth First Search


class Vertex:
    """Add additional helper methods if necessary."""
    def __init__(self, key):
        """Add other attributes as necessary"""
        self.id = key
        self.adjacent_to = []
        self.visited = 0
        self.stacked = False
        self.color = ""


class Graph:
    """Add additional helper methods if necessary."""
    def __init__(self, filename):
        """reads in the specification of a graph and creates a graph using an adjacency list representation.
           You may assume the graph is not empty and is a correct specification.  E.g. each edge is 
           represented by a pair of vertices.  Note that the graph is not directed so each edge specified 
           in the input file should appear on the adjacency list of each vertex of the two vertices associated 
           with the edge."""
        fp = open(filename)
        line = fp.readline()
        self.adjacency = {}
        while line:
            vertices = line.strip("\n").split(" ")
            self.add_vertex(vertices[0])
            self.add_vertex(vertices[1])
            self.add_edge(vertices[0], vertices[1])
            line = fp.readline()
        fp.close()

    def add_vertex(self, key):
        """Add vertex to graph, only if the vertex is not already in the graph."""
        if self.adjacency.get(key) is None:
            self.adjacency[key] = Vertex(key)

    def get_vertex(self, key):
        """Return the Vertex object associated with the id. If id is not in the graph, return None"""
        return self.adjacency.get(key)

    def add_edge(self, v1, v2):
        """v1 and v2 are vertex id's. As this is an undirected graph, add an
           edge from v1 to v2 and an edge from v2 to v1.  You can assume that
           v1 and v2 are already in the graph"""
        if v1 not in self.adjacency[v2].adjacent_to:
            self.adjacency[v2].adjacent_to.append(v1)
            self.adjacency[v1].adjacent_to.append(v2)

    def get_vertices(self):
        """Returns a list of id's representing the vertices in the graph, in ascending order"""
        lst = []
        for j in self.adjacency:
            lst.append(j)
        lst.sort()
        return lst

    def conn_components(self): 
        """Returns a list of lists.  For example, if there are three connected components
           then you will return a list of three lists.  Each sub list will contain the 
           vertices (in ascending order) in the connected component represented by that list.
           The overall list will also be in ascending order based on the first item of each sublist.
           This method MUST use Depth First Search logic!"""
        """vertices = self.get_vertices()
                con = []
                for i in vertices:
                    start = self.adjacency.get(i)
                    lst = []
                    start.visited += 1
                    if start.visited <= 1:
                        s = Stack(len(self.adjacency)*2+1)
                        s.push(start)
                        con.append(self.conn_helper(lst, [], s))
                con.sort(key=lambda x: x[0][2:])
                return con

            def conn_helper(self, lst, sub, s):
                while not s.is_empty():
                    vertex = s.pop()
                    vertices = vertex.adjacent_to
                    for i in vertices:
                        i = self.get_vertex(i)
                        i.visited += 1
                        if i.visited <= 1 and i.id not in sub:
                            s.push(i)
                            sub += [i.id]
                            #vertex.visited += 1
                            if vertex.visited <= 1 and vertex.id not in sub:
                                sub += [vertex.id]
                            self.conn_helper(lst, sub, s)
                sub.sort()
                return sub"""
        vertices = self.get_vertices()
        con = []
        s = Stack(len(self.adjacency))
        while len(vertices) > 0:
            start = self.adjacency.get(vertices[0])
            lst = []
            s.push(start)
            start.stacked = True
            while not s.is_empty():
                vertex = s.pop()
                if vertex.id not in lst:
                    lst.append(vertex.id)
                    vertices.remove(vertex.id)
                adj = vertex.adjacent_to
                for i in adj:
                    i = self.get_vertex(i)
                    if not i.stacked and i.id not in lst and i.id in vertices:
                        s.push(i)
                        i.stacked = True
            lst.sort()
            con.append(lst)
        con.sort(key=lambda x: x[0][2:])
        return con

    def is_bipartite(self):
        """Returns True if the graph is bicolorable and False otherwise.
           This method MUST use Breadth First Search logic!"""
        vertices = self.get_vertices()
        q = Queue(len(self.adjacency))
        while len(vertices) > 0:
            start = self.get_vertex(vertices[0])
            start.color = "black"
            q.enqueue(start)
            while not q.is_empty():
                current = q.dequeue()
                if current.id in vertices:
                    adj = current.adjacent_to
                    if current.color == "black":
                        for i in adj:
                            if self.get_vertex(i).color == "black":
                                return False
                            self.get_vertex(i).color = "red"
                            q.enqueue(self.get_vertex(i))
                    elif current.color == "red":
                        for i in adj:
                            if self.get_vertex(i).color == "red":
                                return False
                            self.get_vertex(i).color = "black"
                            q.enqueue(self.get_vertex(i))
                    vertices.remove(current.id)
        # vertices.remove(self.get_vertex(vertices[0]))
        return True


