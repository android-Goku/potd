# Problem Link - https://leetcode.com/problems/most-profitable-path-in-a-tree/
# Solution Link - https://algo.monster/liteproblems/2467

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        def dfs_reach_time(i, prev, t):
            if i == 0:
                reach_time[i] = min(reach_time[i], t)
                return True
            for neighbor in graph[i]:
                if neighbor != prev and dfs_reach_time(neighbor, i, t + 1):
                    reach_time[neighbor] = min(reach_time[neighbor], t + 1)
                    return True
            return False

        def dfs_max_profit(i, prev, t, current_profit):
            if t == reach_time[i]:
                current_profit += amount[i] // 2
            elif t < reach_time[i]:
                current_profit += amount[i]
            nonlocal max_profit
            if len(graph[i]) == 1 and graph[i][0] == prev:
                max_profit = max(max_profit, current_profit)
                return
            for neighbor in graph[i]:
                if neighbor != prev:
                    dfs_max_profit(neighbor, i, t + 1, current_profit)

        num_nodes = len(edges) + 1
        graph = defaultdict(list)
        reach_time = [num_nodes] * num_nodes
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        dfs_reach_time(bob, -1, 0)
        reach_time[bob] = 0 
        max_profit = float('-inf') 
        dfs_max_profit(0, -1, 0, 0)
        return max_profit