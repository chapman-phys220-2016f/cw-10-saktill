#! /usr/bin/env python 3

""""""

import numpy as np
import matplotlib.pyplot as plt

def random_walk_2D_final(Np, ns):

	# initialize arrays for x and y components of position
    xpositions = np.zeros(Np)
    ypositions = np.zeros(Np)

    # generates random integers 1-4, puts them in 2d array
    moves = np.random.randint(1,5,size=Np*ns)
    moves.shape = (ns,Np)

    # Estimate max and min positions
    xymax = 3*np.sqrt(ns)
    xymin = -xymax

    # give numerical values to coordinate directions
    north = 1; south = 2; east = 3; west = 4

    # modify x and y coordinate values by turning moves matrix into a matrix
    # of 1's, -1's and 0's, based on whether that value was north, south, 
    # east, or west, then adding together all the rows; each row represents 
    # one step, each column represents one particle; so the end result is a 
    # row vector(a 1d array), with np elements, representing the x position of 
    # of each particle, and likewise for y
    xpositions += (np.where(moves == east,1,0) - np.where(moves == west,1,0)).sum(0)
    ypositions += (np.where(moves == north,1,0) - np.where(moves == south,1,0)).sum(0)

    plt.plot(xpositions,ypositions,'ko',0,0,'bo')
    plt.axis([xymin,xymax,xymin,xymax])
    plt.title("%d particles after %d steps"%(Np,ns))
    plt.savefig("tmp_%d.eps"%(ns))

    return(xpositions,ypositions)

def random_walk_2D(Np,ns,plot_step):
    """Generates arraysfor the x and y components of the position of
    Np particles after ns steps in a random walk. Also generates a sequence
    of pdf files, each of them being a plot of the random walk after i steps,
    for each i in ns."""

    # initialize arrays for x and y components of position
    xpositions = np.zeros(Np)
    ypositions = np.zeros(Np)

    # generates random integers 1-4, puts them in 2d array
    moves = np.random.randint(1,5,size=Np*ns)
    moves.shape = (ns,Np)

    # Estimate max and min positions
    xymax = 3*np.sqrt(ns)
    xymin = -xymax

    # give numerical values to coordinate directions
    north = 1; south = 2; east = 3; west = 4


    
    # amend each xpositions and ypositions based on the moves matrix,
    # depending on whether it randomly general north, south, east, or west
    for step in range(ns):
        this_move = moves[step,:]
        xpositions += np.where(this_move == east,1,0)
        xpositions -= np.where(this_move == west,1,0)
        ypositions += np.where(this_move == north,1,0)
        ypositions -= np.where(this_move == south,1,0)

        if ((step+1) % plot_step == 0):
            plt.plot(xpositions,ypositions,'ko')
            plt.title(["%d particles after %d steps" %(Np, step+1)])
            plt.axis([xymin,xymax,xymin,xymax])
            plt.savefig("tmp_%03d.png"%(step+1))
            plt.clf()
    return(xpositions,ypositions)

def main(Np,ns,plot_step):
    import numpy as np
    import sys
    np.random.seed(11)
    x, y = random_walk_2D(Np,ns,plot_step)

if (__name__ == "__main__"):
    import sys
    Np = int(sys.argv[1])
    ns = int(sys.argv[2])
    plot_step = int(sys.argv[3])
    main(Np,ns,plot_step)