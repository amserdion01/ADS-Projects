from step import Step
from graph import Graph
from vertex import Vertex


class JKUMap(Graph):

    def __init__(self):
        super().__init__()

        v_spar = self.insert_vertex("Spar")
        v_lit = self.insert_vertex("LIT")
        v_openlab = self.insert_vertex("Open Lab")
        v_khg = self.insert_vertex("KHG")
        v_parking = self.insert_vertex("Parking")
        v_bellacasa = self.insert_vertex("Bella Casa")
        v_sp1 = self.insert_vertex("SP1")
        v_sp3 = self.insert_vertex("SP3")
        v_lui = self.insert_vertex("LUI")
        v_teichwerk = self.insert_vertex("Teichwerk")
        v_library = self.insert_vertex("Library")
        v_chat = self.insert_vertex("Chat")
        v_bank = self.insert_vertex("Bank")
        v_porter = self.insert_vertex("Porter")
        v_castle = self.insert_vertex("Castle")
        v_papaya = self.insert_vertex("Papaya")
        v_JKH = self.insert_vertex("JKH")

        self.insert_edge(v_spar, v_lit, 50)
        self.insert_edge(v_spar, v_porter, 103)
        self.insert_edge(v_spar, v_khg, 165)
        self.insert_edge(v_khg, v_bank, 150)
        self.insert_edge(v_khg, v_parking, 190)
        self.insert_edge(v_parking, v_bellacasa, 145)
        self.insert_edge(v_parking, v_sp1, 240)
        self.insert_edge(v_sp1, v_sp3, 130)
        self.insert_edge(v_sp1, v_lui, 175)
        self.insert_edge(v_lui, v_teichwerk, 135)
        self.insert_edge(v_lui, v_library, 90)
        self.insert_edge(v_lui, v_chat, 240)
        self.insert_edge(v_library, v_chat, 160)
        self.insert_edge(v_chat, v_bank, 115)
        self.insert_edge(v_bank, v_porter, 100)
        self.insert_edge(v_porter, v_openlab, 70)
        self.insert_edge(v_porter, v_lit, 80)
        self.insert_edge(v_castle, v_papaya, 85)
        self.insert_edge(v_papaya, v_JKH, 80)

    def get_shortest_path_from_to(self, from_vertex: Vertex, to_vertex: Vertex):
        """
        This method determines the shortest path between two POIs "from_vertex" and "to_vertex".
        It returns the list of intermediate steps of the route that have been found
        using the dijkstra algorithm.

        :param from_vertex: Start vertex
        :param to_vertex:   Destination vertex
        :return:
           The path, with all intermediate steps, returned as an list. This list
           sequentially contains each vertex along the shortest path, together with
           the already covered distance (see example on the assignment sheet).
           Returns None if there is no path between the two given vertices.
        :raises ValueError: If from_vertex or to_vertex is None, or if from_vertex equals to_vertex
        """
        if from_vertex is None or to_vertex is None or to_vertex == from_vertex:
            raise ValueError

        d, p = self._dijkstra(from_vertex, [], {from_vertex: 0},{from_vertex : 0})


        result = []
        cur = to_vertex
        #print(d)
        if cur not in d:
            return None

        while(cur != from_vertex):
            temp = Step(cur, d[cur])
            result.append(temp)
            cur = p[cur]
        result.append( Step(from_vertex, 0))
        result = result[::-1]
        #print(result)
        return result

    def get_steps_for_shortest_paths_from(self, from_vertex: Vertex):
        """
        This method determines the amount of "steps" needed on the shortest paths
        from a given "from" vertex to all other vertices.
        The number of steps (or -1 if no path exists) to each vertex is returned
        as a dictionary, using the vertex name as key and number of steps as value.
        E.g., the "from" vertex has a step count of 0 to itself and 1 to all adjacent vertices.

        :param from_vertex: start vertex
        :return:
          A map containing the number of steps (or -1 if no path exists) on the
          shortest path to each vertex, using the vertex name as key and the number of steps as value.
        :raises ValueError: If from_vertex is None.
        """
        result = {}
        if from_vertex is None:
            raise ValueError

        for elem in self.get_vertices():
            if elem == from_vertex :
                result [ elem.name ] = 0
                continue
            temp = self.get_shortest_path_from_to( from_vertex, elem )
            if temp is None :
                result[elem.name] = -1
            else:
                result[elem.name] = len(temp) -1

        return result

    def get_shortest_distances_from(self, from_vertex: Vertex):
        """
        This method determines the shortest paths from a given "from" vertex to all other vertices.
        The shortest distance (or -1 if no path exists) to each vertex is returned
        as a dictionary, using the vertex name as key and the distance as value.

        :param from_vertex: Start vertex
        :return
           A dictionary containing the shortest distance (or -1 if no path exists) to each vertex,
           using the vertex name as key and the distance as value.
        :raises ValueError: If from_vertex is None.
        """

        if from_vertex is None:
            raise ValueError

        d, p = self._dijkstra(from_vertex, [], {from_vertex: 0},{from_vertex : 0})
        result = {}
        nopaths = []
        for elem in self.vertices:
            if elem not in d:
                d[elem] = -1

        for elem in d:
            result[elem.name] = d[elem]

        return result

    def _dijkstra(self, cur: Vertex, visited_list, distances: dict, paths: dict):
        """
        This method is expected to be called with correctly initialized data structures and recursively calls itself.

        :param cur: Current vertex being processed
        :param visited_list: List which stores already visited vertices.
        :param distances: Dict (nVertices entries) which stores the min. distance to each vertex.
        :param paths: Dict (nVertices entries) which stores the shortest path to each vertex.
        """
        adjacency_list = self.get_adjacent_vertices(cur)
        # This method is not mandatory, but a recommendation by us
        for vertex in adjacency_list:
            temp_edge = self.find_edge(vertex, cur)
            weight = temp_edge.weight
            temp_distance = weight + distances[cur]
            if vertex not in distances or temp_distance < distances[vertex]:
                distances[vertex] = temp_distance
                paths[vertex] = cur
        visited_list.append(cur)
        min = 99999999

        for vertex in distances:
            if vertex not in visited_list :
                if min > distances[vertex] or min == 99999999:
                    temp_vertex = vertex
                    min = distances[vertex]

        if min != 99999999:
            return self._dijkstra(temp_vertex, visited_list, distances, paths)

        return distances,paths


j = JKUMap()
# ddd = j.get_shortest_path_from_to(j.find_vertex("JKH"),j.find_vertex("Castle"))
# for x in ddd :
#     print ( f"{x.point.name} {x.covered_distance}" )
#path = j.get_shortest_path_from_to(j.find_vertex("SP3"), j.find_vertex("Spar"))
#print(path)
j.get_steps_for_shortest_paths_from(j.find_vertex("JKH"))

#d, p = j._dijkstra(j.find_vertex("LUI"), [], {j.find_vertex("LUI"): 0},{j.find_vertex("LUI"):0})

# for elem in d:
#     if p[elem]:
#         print(elem.name, d[elem], p[elem].name)
#     else:
#         print(elem.name, d[elem], "start")

