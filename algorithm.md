# How to find central vertex in a graph?

https://mathoverflow.net/questions/89376/how-to-find-central-vertex-in-a-graph

To state more directly what Joseph said, if we know the distance between any two vertices, it is straightforward to first find the eccentricity of vv, i.e. the maximum distance from vv to another vertex. Having done this we simply mark the vertices of lowest eccentricity as being central.

To find the distance between every pair of vertices, one can apply the Floyd-Warshall algorithm for all-pairs shortest path, which runs in O(n3)O(n3) time.

http://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm

# Combinatorial optimization
https://en.wikipedia.org/wiki/Combinatorial_optimization

# Mathematical Optimization

https://en.wikipedia.org/wiki/Mathematical_optimization
