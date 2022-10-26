import collections

class Solution:
    def validPath(self, n: int, edges: list, source: int, destination: int) -> bool:
        explored = [False]*n
        stack = [source]
        curr_node = None
        edges_dict = collections.defaultdict(list)
        for a,b in edges:
            edges_dict[a].append(b)
            edges_dict[b].append(a)

        explored[source] = True

        while stack:
            curr_node = stack.pop()
            for node in edges_dict[curr_node]:
                if node == destination:
                    return True
                if not explored[node]:
                    stack.append(node)
        return False
