# -*- coding: utf-8 -*-
"""

This is the code for Biogeography-Based Optimization (BBO)
@author: Dan Simon
Reference: D. Simon, Biogeography-Based Optimization, IEEE Transactions on Evolutionary Computation, in print (2008).
Coded by: Raju Pal (emailid: raju3131.pal@gmail.com) and Himanshu Mittal (emailid: himanshu.mittal224@gmail.com)

-- Solution variable File: Defining the solution variable for saving the output variables

Code compatible:
 -- Python: 2.* or 3.*
"""

class solution:
    def __init__(self):
        self.best = 0
        self.bestIndividual=[]
        self.convergence = []
        self.optimizer=""
        self.objfname=""
        self.startTime=0
        self.endTime=0
        self.executionTime=0
        self.lb=0
        self.ub=0
        self.dim=0
        self.popnum=0
        self.maxiers=0
