#! /usr/bin/env python3
import numpy as np

def flipCoin(n):
    """Simulation of flipping a coin n times as specified by the user.
    Simulation is done through vectorized numpy methods. We then add
    up all of the times we get tails."""

    r = np.random.random(n)
    #chose 0 as tails and 1 as heads
    
    b = np.where(r<=0.5,0,1)
    a = len(b[b<1])

    return a

def test_flipCoin():
    """Testing the coin flip method."""
    if(flipCoin(10) != 0):
        return True
    else:
        return False

def main():
    """ """
    print(flipCoin(10))

