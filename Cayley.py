# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 14:38:46 2021

@author: sohei
"""
import numpy as np
import operator

def Quaternion(R):
    #This function takes as input a 3x3 rotation matrix and returns the
    #corresponding unit quaternion. It implements Cayley's method. For 
    #details, see:
    #S. Sarabandi and F. Thomas, "A survey on the computation of quaternions 
    #from rotation matrices," ASME Journal of Mechanisms and Robotics, 
    #Vol. 11, No. 2, 021006, 2019
    e0 = 0.25*np.sqrt((1+R[0,0]+R[1,1]+R[2,2])**2 + (R[2,1]-R[1,2])**2 + (R[0,2]-R[2,0])**2 + (R[1,0]-R[0,1])**2)
    e1 = 0.25*np.sqrt((R[2,1]-R[1,2])**2 + (1+R[0,0]-R[1,1]-R[2,2])**2 + (R[0,1]+R[1,0])**2 + (R[2,0]+R[0,2])**2)
    e2 = 0.25*np.sqrt((R[0,2]-R[2,0])**2 + (R[0,1]+R[1,0])**2 + (1-R[0,0]+R[1,1]-R[2,2])**2 + (R[1,2]+R[2,1])**2)
    e3 = 0.25*np.sqrt((R[1,0]-R[0,1])**2 + (R[2,0]+R[0,2])**2 + (R[1,2]+R[2,1])**2 + (1-R[0,0]-R[1,1]+R[2,2])**2)
    e=[e0,e1,e2,e3]
    index, max_value = max(enumerate(e), key=operator.itemgetter(1))
    

    if index==0:
        e[0]=e0
        e[1] = np.sign(R[2,1]-R[1,2])*e1
        e[2] = np.sign(R[0,2]-R[2,0])*e2
        e[3] = np.sign(R[1,0]-R[0,1])*e3
    elif index==1:
        e[0]=  np.sign(R[2,1]-R[1,2])*e0
        e[1] = e1
        e[2] = np.sign(R[1,0]+R[0,1])*e2
        e[3] = np.sign(R[0,2]+R[2,0])*e3
    elif index==2:
        e[0] = np.sign(R[0,2]-R[2,0])*e0
        e[1] = np.sign(R[1,0]+R[0,1])*e1
        e[2] = e2
        e[3] = np.sign(R[2,1]+R[1,2])*e3
    else:
        e[0] = np.sign(R[1,0]-R[0,1])*e0
        e[1] = np.sign(R[0,2]+R[2,0])*e1
        e[2] = np.sign(R[2,1]+R[1,2])*e2
        e[3] = e3  

    return e/np.linalg.norm(e)