import numpy as np
import matplotlib.pyplot as plt
import random
import time

class Robot:
    __name = None
    __x = 0
    __y = 0
    __possible_moves = []
    __path =[]
    __visited = {}

    def __init__ (self, name, x, y):
        self.__name = name
        self.__x = x
        self.__y = y
        self.__path = [[x,y]]
        self.__possible_moves = [[1,0],[-1,0],[0,1],[0,-1]]

    def getName(self):
        return self.__name

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

    def printLocation(self):
        print("x = ", self.__x, ", y = ", self.__y)
    
    def getLocation(self):
        return [self.__x, self.__y]

    def getPath(self):
        return self.__path
        

Robots = [];
RLocs = []
RPaths = []

Robots.append(Robot("R1",0,0))
Robots.append(Robot("R2",0,0))

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
    Robots[0].random_move()
    Robots[1].move(random.randint(0,3))
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
