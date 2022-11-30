# ----------
# User Instructions:
#
# Define a function, search() that takes no input
# and returns a list
# in the form of [optimal path length, x, y]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1] # Make sure that the goal definition stays in the function.

delta = [[-1, 0 ], # go up
        [ 0, -1], # go left
        [ 1, 0 ], # go down
        [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost = 1

def legal(node, move):
    #tests if expanded node (node+move) is in grid size and not occupied

    return ((node[0] + move[0] < len(grid)) and
            (node[1] + move[1] < len(grid[0])) and
            (node[0] + move[0] >= 0) and
            (node[1] + move[1] >= 0) and
            (grid[node[0]+move[0]][node[1]+move[1]] == 0))

def search():
    # ----------------------------------------
    # insert code here and make sure it returns the appropriate result
    # ----------------------------------------
    open_list = [[0, init[0], init[1]]]
    searched = []

    while(len(open_list) > 0):

        print "-----"
        print "new open list: \n", open_list
        lowest = open_list[0][0]
        index = 0
        for i in range(len(open_list)-1):
            if (open_list[i][0] < lowest):
                lowest = open_list[i][0]
                index = i

        item = open_list[index]
        open_list.remove(item)

        print "take list item: \n", item
        print "searched: \n", searched


        if (item[1] == goal[0]) and (item[2] == goal[1]):
            print "****Search successful!"
            return item

        #expand all new nodes
        for d in delta:
            if legal(item[1:], d) and not (item[1:] in searched):
                open_list.append([item[0]+1, item[1]+d[0], item[2]+d[1]])

        searched.append(item[1:])

    if open_list == []:
        return 'fail'

print search()