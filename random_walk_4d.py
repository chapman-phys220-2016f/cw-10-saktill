#! /usr/bin/env python

""""""
import numpy as np
import matplotlib.pyplot as plt

def random_walk_4D(N,numStep,stepInt):
	
    xpositions = np.zeros(N)
    #Initializing arrays of x and y coordinates for N particles
    ypositions = np.zeros(N)
    zpositions = np.zeros(N)
    wpositions = np.zeros(N)

    # generate random moves in any one of EIGHT POSSIBLE DIRECTIONS WOW!!!
    # with a column for each particle, and each row signifying a new step
    moves = np.random.randint(1,9,size=N*numStep)
    moves.shape = [numStep,N]

    # estimate max and min positions
    xymax = 3*np.sqrt(numStep)
    xymin = -xymax

    # no need to assign directions because compass directions are lame and 2D

    for step in range(numStep):
        this_move = moves[step,:]
        xpositions += np.where(this_move == 1,1,0) - np.where(this_move == 2,1,0)
        ypositions += np.where(this_move == 3,1,0) - np.where(this_move == 4,1,0)
        zpositions += np.where(this_move == 5,1,0) - np.where(this_move == 6,1,0)
        wpositions += np.where(this_move == 7,1,0) - np.where(this_move == 8,1,0)

        

        if ((step+1) % stepInt == 0):
            t = np.dot(np.transpose(np.tile(zpositions,(10,1))),np.tile(wpositions,(10,1)))
            plt.xlabel("X Position")
            plt.ylabel("Y Position")
            plt.axis([xymin,xymax,xymin,xymax])
            plt.pcolormesh(xpositions,ypositions,t,cmap="viridis")
            plt.savefig("tmp_%03d.pdf"%(step+1))
    return(xpositions,ypositions,zpositions,wpositions)

def main():
    import sys
    import numpy as np
    Np = int(sys.argv[1])
    ns = int(sys.argv[2])
    plot_step = int(sys.argv[3])
    x, y, z, w = random_walk_4D(Np,ns,plot_step)

if __name__ == "__main__":
	main()

