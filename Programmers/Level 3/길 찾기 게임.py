preorder, postorder = [], []

def order(nodeinfo, levels, curlevel):
    n = nodeinfo[:]
    cur = n.pop(0)
    preorder.append(cur[2])
    if n:
        for i in range(len(n)):
            if n[i][1] == levels[curlevel + 1]:
                if n[i][0] < cur[0]:
                    order([x for x in n if x[0] < cur[0]], levels, curlevel + 1)
                else:
                    order([x for x in n if x[0] > cur[0]], levels, curlevel + 1)
                    break
    postorder.append(cur[2])


def solution(nodeinfo):
    nodeinfo = [node + [nodeinfo.index(node) + 1] for node in nodeinfo]
    nodeinfo = sorted(nodeinfo, key=lambda x: (-x[1], x[0]))
    levers = sorted(list(set([x[1] for x in nodeinfo])), reverse=True)
    print(levers)

    order(nodeinfo, levers, 0)

    return [preorder, postorder]



preorder = list() # 귀찮아서 전역으로
postorder = list()
def solution(nodeinfo):
    import sys
    sys.setrecursionlimit(10**6)
    levels = sorted(list({x[1] for x in nodeinfo}),reverse=True) # 유효한 Y좌표
    nodes = sorted(list(zip(range(1,len(nodeinfo)+1),nodeinfo)),key=lambda x:(-x[1][1],x[1][0])) # 노드 정렬
    print(nodes)
    order(nodes,levels,0)
    return [preorder,postorder]

def order(nodes,levels,curlevel):
    n = nodes[:] # copy
    cur = n.pop(0) # VISIT
    preorder.append(cur[0]) # PRE-ORDER
    if n: # stop if leaf node
        for i in range(len(n)): # find next floor
            if n[i][1][1] == levels[curlevel+1]: # next floor
                if n[i][1][0] < cur[1][0]: # LEFT CHILD
                    order([x for x in n if x[1][0] < cur[1][0]],levels,curlevel+1)
                else: # RIGHT CHILD
                    order([x for x in n if x[1][0] > cur[1][0]],levels,curlevel+1)
                    break
    postorder.append(cur[0]) # POST-ORDER


print(solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]))
# [[7, 4, 6, 9, 1, 8, 5, 2, 3], [9, 6, 5, 8, 1, 4, 3, 2, 7]]
