import numpy as np
import matplotlib.pyplot as plt
import random
import time

class Robot:
    __name = None
    __x = 0
    __y = 0
    __v = 0
    __vr = 0
    __vl = 0
    __heading = 0
    __wheelbase = 1
    __possible_moves = []
    __path =[]
    __visited = {}

    def __init__ (self, name, x, y, v):
        self.__name = name
        self.__x = x
        self.__y = y
        self.__v = v
        self.__path = [[x,y]]


    def randomVrVl(self):
        self.__vr = random.uniform(0,self.__v)
        self.__vl = random.uniform(0,self.__v) 
    
    def calcMove(self):
        if self.__vr == -self.__vl:
            next_x = self.__x
            next_y = self.__y
            next_heading = self.__heading + (2*self.__v)/self.__wheelbase
        elif self.__vr == self.__vl: 
            next_x = self.__x + self.__v*np.cos(heading)
            next_y = self.__y + self.__v*np.sin(heading)
            next_heading = self.__heading
        else:
            omega = (self.__vr - self.__vl)/self.__wheelbase
            AOR = (self.__wheelbase/2)*((self.__vr + self.__vl)/(self.__vr - self.__vl))
            ICC = [self.__x - AOR*np.sin(self.__heading), self.__y + AOR*np.cos(self.__heading)]
            next_x = np.cos(omega)*(self.__x - ICC[0]) - np.sin(omega)*(self.__y - ICC[1]) + ICC[0] 
            next_y = np.sin(omega)*(self.__x - ICC[0]) + np.cos(omega)*(self.__y - ICC[1]) + ICC[1] 
            next_heading = self.__heading + omega 

        return [next_x, next_y, next_heading]

    def is_frontier(self):
        for dx, dy in self.__possible_moves:
            if (self.__x+dx, self.__y+dy) in self.__visited:
                return True
        return False

    def count_unexplored(self):
        count = 0
        for dx, dy in self.__possible_moves:
            if (dx, dy) not in self.__visited:
                count += 1
        return count

    def get_bias_weight(self):
        weights = []
        for dx, dy in self.__possible_moves:
            nx, ny = self.__x + dx, self.__y + dy

            if (nx, ny) not in self.__visited:
                if self.is_frontier():
                    weights.append(3.0)
                else:
                    weights.append(1.5)
            else:
                weights.append(.1)
        return weights

    def random_move(self):
        weights = self.get_bias_weight()
        direction = random.choices([0,1,2,3], weights = weights)[0]
        self.move(direction)

    def move(self, direction):
        self.__x += self.__possible_moves[direction][0]
        self.__y += self.__possible_moves[direction][1]
        self.__path.append([self.__x, self.__y])
        self.__visited[(self.__x,self.__y)] = 1

    def ddMove(self):
        self.randomVrVl()
        nextLoc = self.calcMove()
        self.__x = nextLoc[0]
        self.__y = nextLoc[1]
        self.__heading = nextLoc[2]
        self.__path.append([self.__x, self.__y])

    def printLocation(self):
        print("x = ", self.__x, ", y = ", self.__y)
    
    def getName(self):
        return self.__name
        
    def getLocation(self):
        return [self.__x, self.__y]

    def getPath(self):
        return self.__path
        

Robots = []
RLocs = []
RPaths = []

Robots.append(Robot("R1",0,0,1))
Robots.append(Robot("R2",0,0,1))

plt.ion()
figure, ax = plt.subplots(figsize=(10, 8))
ax.set_title("Random Walk")
ax.set_xlim(-100,100)
ax.set_ylim(-100,100)
ax.set_xlabel("X position")
ax.set_ylabel("Y position")
ax.legend()
ax.grid(True)

loop_counter_text = ax.text(0.02, 0.95, "", transform=ax.transAxes,
                            fontsize=12, verticalalignment='top',
                            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

for robot in Robots:
    loc = ax.scatter(*robot.getLocation(), label=robot.getName())
    path, = ax.plot(*zip(*robot.getPath()))
    RLocs.append(loc)
    RPaths.append(path)

for n in range(1000):
    Robots[0].ddMove()
    Robots[1].ddMove()
    for i, robot in enumerate(Robots):
        path = np.array(robot.getPath())

        RLocs[i].set_offsets([robot.getLocation()])
        RPaths[i].set_data(path[:, 0], path[:, 1])
    figure.canvas.draw()
    figure.canvas.flush_events()
    loop_counter_text.set_text(f"Step: {n}")
    time.sleep(.1)

plt.ioff()
plt.show()
