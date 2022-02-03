# Ford-Fulkerson algorith in Python


class Graph:

    def __init__(self, graph):
        self.graph = graph  # original graph
        self.residual_graph = [[cell for cell in row] for row in graph]  # cloned graph
        self.latest_augmenting_path = [[0 for cell in row] for row in
                                       graph]  # empty graph with same dimension as graph
        self.current_flow = [[0 for cell in row] for row in graph]  # empty graph with same dimension as graph
        self.maxflow = 0
        self.capacity = 0

    def update(self, path, flow):
        print(f'path:{path}')
        self.latest_augmenting_path = [[0 for cell in row] for row in
                                       self.graph]  # empty graph with same dimension as graph
        for i in range(len(path)-1):
            self.latest_augmenting_path[path[i]][path[i+1]] = flow

            if self.graph[path[i]][path[i+1]] > 0:
                self.current_flow[path[i]][path[i+1]] += flow
            else:
                self.current_flow[path[i+1]][path[i]] -= flow
        print(f'latest_augmenting_path:{self.latest_augmenting_path}')
        print(f'current_flow:{self.current_flow}')

    def bfs(self, graph, source, sink):
        visited = []
        for i in range(len(graph[source])):
            if graph[source][i] > 0:
                visited.append([source, i])
        for i in visited:
            index = i[-1]
            for j in range(len(graph[index])):
                if graph[index][j] > 0 and j not in i:
                    x = list(i)
                    x.append(j)
                    visited.append(x)
                    if x[-1] == sink:
                        return x


    def update_residual_graph(self, path, flow, graph):
        residual_graph = graph
        for i in range(len(path) - 1):
                residual_graph[path[i]][path[i+1]] -= flow
                residual_graph[path[i+1]][path[i]] += flow

        return residual_graph


    def minflow(self, path, graph):
        mn = None
        for i in range(len(path)-1):
            if mn is None or mn > graph[path[i]][path[i+1]]:
                mn = graph[path[i]][path[i+1]]

        return mn

    def ff_step(self, source, sink):
        """
        Perform a single flow augmenting iteration from source to sink
        Update the latest augmenting path, the residual graph and the current flow by the maximum possible amount according to your chosen path.
        The path must be chosen based on BFS.
        @param source the source's vertex id
        @param sink the sink's vertex id
        @return the amount by which the flow has increased.
        """

        path = self.bfs(self.residual_graph, source, sink)
        if path is None:
            print("no path")
            return 0
        print(self.residual_graph)
        flow = self.minflow(path, self.residual_graph)
        self.residual_graph = self.update_residual_graph(path, flow, self.residual_graph)
        print(f'residual_graph:{self.residual_graph}')
        self.update(path, flow)
        print(f' path : {path}')
        print(f' flow : {flow}')
        self.maxflow += flow
        return flow

    def ford_fulkerson(self, source, sink):
        """
        Execute the ford-fulkerson algorithm (i.e., repeated calls of ff_step())
        @param source the source's vertex id
        @param sink the sink's vertex id
        @return the max flow from source to sink
        """
        while(self.ff_step(source,sink)):
            pass
        else:
            return self.maxflow





x = Graph([
        [0, 16, 13, 0, 0, 0],
        [0, 10, 0, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]
    ])


