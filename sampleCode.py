graph = {'1': ['2', '3', '4'],
        '2': ['5', '6'],
        '5': ['9', '10'],
        '4' : ['7', '8'],
        '7' : ['11', '12']}

def bfs(graph,start,goal):
        queue=[]
        queue.append(start)
        while(queue):
                path=queue.pop(0)
                node=path[-1]
                if node==goal:
                        return path
                for every_successor in graph.get(node,[]):
                        new_path=list(path)
                        new_path.append(every_successor)
                        queue.append(new_path)

print(bfs(graph,'1','11'))