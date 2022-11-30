# -------------
# User Instructions
#
# Here you will be implementing a cyclic smoothing
# algorithm. This algorithm should not fix the end
# points (as you did in the unit quizzes). You
# should use the gradient descent equations that
# you used previously.
#
# Your function should return the newpath that it
# calculates..
#
# Feel free to use the provided solution_check function
# to test your code. You can find it at the bottom.
#
# --------------
# Testing Instructions
#
# To test your code, call the solution_check function with
# two arguments. The first argument should be the result of your
# smooth function. The second should be the corresponding answer.
# For example, calling
#
# solution_check(smooth(testpath1), answer1)
#
# should return True if your answer is correct and False if
# it is not.

from math import *

# Do not modify path inside your function.
path=[[0, 0], #fix
      [1, 0],
      [2, 0],
      [3, 0],
      [4, 0],
      [5, 0],
      [6, 0], #fix
      [6, 1],
      [6, 2],
      [6, 3], #fix
      [5, 3],
      [4, 3],
      [3, 3],
      [2, 3],
      [1, 3],
      [0, 3], #fix
      [0, 2],
      [0, 1]]

# Do not modify fix inside your function
fix = [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0]


############# ONLY ENTER CODE BELOW THIS LINE ##########

# ------------------------------------------------
# smooth coordinates
# If your code is timing out, make the tolerance parameter
# larger to decrease run time.
#

def smooth(path, fix, weight_data = 0.0, weight_smooth = 0.1, tolerance = 0.00001):

    #
    # Enter code here
    # Make a deep copy of path into newpath
    newpath = [[0 for col in range(len(path[0]))] for row in range(len(path))]
    for i in range(len(path)):
        for j in range(len(path[0])):
            newpath[i][j] = path[i][j]

    L = len(newpath)
    change = tolerance
    while (change >= tolerance):
        change = 0.0
        for i in range(len(path)):
            if not fix[i]:
                for j in range(len(path[0])):
                    old = newpath[i][j]
                    newpath[i][j] += weight_data*(path[i][j] - newpath[i][j])
                    newpath[i][j] += weight_smooth * (newpath[(i+1)%L][j] + newpath[(i-1)%L][j] - (2.0 * newpath[i][j]))
                    newpath[i][j] += 0.5 * weight_smooth * (2.0 * newpath[(i-1)%L][j]
                        - newpath[(i-2)%L][j] - newpath[i][j])
                    newpath[i][j] += 0.5 * weight_smooth * (2.0 * newpath[(i+1)%L][j] - newpath[(i+2)%L][j] - newpath[i][j])
                    change += abs(newpath[i][j] - old)

    return newpath # Leave this line for the grader!

    #

# thank you - EnTerr - for posting this on our discussion forum

newpath = smooth(path, fix)
for i in range(len(path)):
    print '['+ ', '.join('%.3f'%x for x in path[i]) +'] -> ['+ ', '.join('%.3f'%x for x in newpath[i]) +']'

