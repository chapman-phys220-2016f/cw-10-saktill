# PHYS220 CW 10 

**Author(s):** _\<Will and Sakthi\>_

[![Build Status](https://travis-ci.org/chapman-phys220-2016f/cw-10-saktill.svg?branch=master)](https://travis-ci.org/chapman-phys220-2016f/cw-10-saktill)

**Due date:** 2016/11/08

## Specification

**Reminder: We have switched to Python3 officially.**

Complete the following exercises from the primary textbook, placing your solutions into separate files. In each file, write the solution as a callable function, so that you can write suitable test functions that demonstrate correct output using the nose framework. GitHub will automatically run your tests on every commit, indicating any failures via the Travis framework with build status above.

1. p.508, 8.15, in ```flip_coin_vec.py```. Learning to vectorize conditionals using numpy is this way is a useful prototype for the remainder of the assignment.
1. Re-implement the code in ```walk2Dv.py``` shown on p.497 of the textbook. That is, fix this code so that it is correctly formatted, commented, and uses a proper ```__main__``` block for running it as a script on the command line. Use better (more descriptive) variable names, and generally clean up the algorithm.
1. The output of the random walk code is a sequence of .pdf files that you can later collect into animated gifs using a simple bash command: ```convert -delay 50 -loop 0 tmp_*.pdf walk.gif```  This command uses the ImageMagick file conversion suite in linux, which is also installed in your Sage Cloud account. The delay parameter specifies frame delay in milliseconds. The loop parameter of 0 specifies an infinite number of loops for the gif. Create such an animated gif for the 2D random walk and commit it to the repository. (Do not commit any individual pdf frames.) Using 1000 particles that walk for 400 steps.

To cleanly present your work, create a Jupyter notebook ```cw8-randomwalk.ipynb``` that imports each file and carefully discusses the algorithms being implemented. The notebook should be formatted professionally using Markdown headings, including your name and a brief description of each homework section. 

Pro-tip: using git to manage conflicts on Jupyter notebooks is a pain. I recommend delegating one person from your group to edit the notebook, to avoid merge conflicts.

## Assessment

Analyze in this section what you found useful about this assignment in your own words. Include any lingering questions or comments that you may have.

I had way too much fun with the gifs, but also couldn't find a way to embed them into my Jupyter notebook, so they are just included in the repository as separate files.

## Honor Pledge

I pledge that all the work in this repository is my own with only the following exceptions:

* Content of starter files supplied by the instructor;
* Code borrowed from another source, documented with correct attribution in the code and summarized here.

Signed,

Saktill
