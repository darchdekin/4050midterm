def allPathsSourceTarget(graph):
    """
    :type graph: List[List[int]]
    :rtype: List[List[int]]
    """
    return DFS(graph, 0, len(graph) - 1)

def DFS(graph, source, target):
    """
    :type graph: List[List[int]]
    :type source: int
    :type target: int
    :rtype: List[List[int]]
    """
    if(source == target):
        return [[target]]
    if (len(graph[source])==0):
        return None
    paths = []
    for node in graph[source]:
        l = DFS(graph, node, target)
        if(l != None):
            for p in l:
                p.append(source)
                paths.append(p)
    if(len(paths)==0):
        return None
    return paths