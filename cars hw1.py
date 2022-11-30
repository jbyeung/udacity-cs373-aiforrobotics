

colors = [['red', 'green', 'green', 'red' , 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]

measurements = ['green', 'green', 'green' ,'green', 'green']


motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]

sensor_right = 0.7

p_move = 0.8

def show(p):
    for i in range(len(p)):
        print p[i]

#DO NOT USE IMPORT
#ENTER CODE BELOW HERE
#ANY CODE ABOVE WILL CAUSE
#HOMEWORK TO BE GRADED
#INCORRECT

#--------------------------------------------------------------------------
#my code


def sense(p, Z):
#sense function - senses given measurement 'Z' and adjusts distribution
    q = []
    for i in range(len(p)):
        v = [] #temp vector to accrue per row
        for j in range(len(p[i])):
            hit = (Z == colors[i][j])
            v.append(p[i][j] * (hit * sensor_right + (1 - hit) * (1 - sensor_right)))
        q.append(v)
    return q

def move(p, m):
#move function - makes move and adjusts distrubtion accordingly
#motion of [0,1] is move to right, [0,-1] is move to left, [1,0] is down, [-1,0] is up
#left/right is in j-axis, corresponding to m[0] value
#down/up is in i-axis, corresponding to m[1] value
    q = []
    for i in range(len(p)):
        v = []
        for j in range (len(p[i])):
            #moving
            s = p_move * p[(i-m[0]) % len(p)][(j-m[1]) % len(p[i])]
            #account for not moving
            s+= (1 - p_move) * p[i][j]
            v.append(s)
        q.append(v)
    return q

def normalize(p):
#normalizes p and rounds to 3 decimals
    normalizer = 0
    for i in range(len(p)):
        normalizer = normalizer + sum(p[i])

    for i in range(len(p)):
        for j in range(len(p[i])):
            p[i][j]/= normalizer
            p[i][j] = round(p[i][j], 3)



p = []

#initialize p with uniform distribution for size = to the world as a matrix

for i in range(len(colors)):
    v = [] #temp vector to build before appending to p
    for j in range(len(colors[i])):
        v.append(1./ (len(colors) * len(colors[i])))
    p.append(v)


#for each measurement/move pair, sense item in 'measurements' and then make move in 'motions' at number 'i'

for i in range(len(measurements)):
    p = move(p, motions[i])
    p = sense(p, measurements[i])

normalize(p)

#--------------------------------------------------------------------
#Your probability array must be printed
#with the following code.

show(p)




