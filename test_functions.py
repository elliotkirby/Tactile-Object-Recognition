# -*- coding: utf-8 -*-
import numpy as np
import math
"""
This file contains functions to be used as part of the robotic classifier project.
"""

def get_maximum_consecutive_changes(array):
    """ 
    A function which identifies the maximum number of consecutive changes between frames from the tactile data
    
    """
    max_count=0 
    continuous_count = 0 
    for i in array: 
        if i == 1:
            continuous_count +=1
        else: 
            if continuous_count > max_count: 
                max_count = continuous_count 
            continuous_count = 0 
    return max_count

def get_maximum_consecutive_stability(array):
    """ 
    A function which identifies the maximum number of consecutive stable frames from the tactile data
    Additional consideration is made to ensure only frames between tactile changes are considered 
    """
    max_count=0 
    continuous_count = 0 
    changes = np.nonzero(array == 1)
    
    if len(changes[0]) == 0: 
        return 0
    
    # Identifies the first and last recorded tactile changes during the experimental procedure    
    start = changes[0][0]
    end = changes[0][-1] + 1

    # It only loops through the period of recorded tactile activity
    for i in array[start:end]: 
        if i == 0:
            continuous_count +=1
        else: 
            if continuous_count > max_count: 
                max_count = continuous_count 
            continuous_count = 0 
    return max_count

def percentage_change_tolerance(v1,v2,t): 
    """
    A function which checks whether a change in recorded values is within a predetermined threshold value 
    Returns a flag as either True or False
    """

    perc_change = np.abs((v1 - v2) / v1)
    if perc_change <= t: 
        return True
    else: 
        return False
    
def cart2pol(x,y):
    """"
    A function for converting cartesian values into polar co-ordinates. 
    Polar co-ordinates are returned as an angle/phi (in degrees) and a magnitude (rho)
    """
    rho_tracker = []
    phi_tracker = []
    for i,j in zip(x,y): 
        rho = np.sqrt((i**2 + j**2))
        phi = np.arctan2(j,i)
        phi *= 180/math.pi
#         print(f"phi: {phi}, rho: {rho}")
        rho_tracker.append(rho)
        phi_tracker.append(phi)
    

    return (rho_tracker, phi_tracker)

def compare_vectors(phi, index1, index2):
    
    """
    A function which compares the directions of two vectors given by polar co-ordinates. 
    The two vectors are identified as being in the same (or opposite) directions for x and y.
    The returned array indicates which one of 4 possible alignments the two vectors are oriented in.
    """
    results = np.zeros(4)
    if phi[index2] ==0: 
        return results

    if np.sign(phi[index1]) == np.sign(phi[index2]): 
#         print("Same direction re: x ")
        x = True
    else: 
#         print("Opposite x")
        x = False
    if (np.abs(phi[index1]) <= 90 and np.abs(phi[index2]) <=90) or (np.abs(phi[index1]) >= 90 and np.abs(phi[index2]) >=90): 
#         print("Same direction re: y ")
        y = True
    else: 
#         print("Opposite y")
        y = False 
    
    # Check which conditions are satisfied to identify the relevant classification of the two vectors.      
    if x and y: 
        results[0]=1
    elif x and not y: 
        results[1]=1
    elif not x and y:
        results[2] =1
    else: 
        results[3]=1
#     print(results)
    return results

def compare_all_vectors(phi, mag):
    """
    A function which looks at the direction of all shear forces and returns flags which indicate evidence of symmetry or parallel forces.
    Information of the direction of shear forces at all taxels is used as input
    """
    a = np.abs(phi) <= 90
    b = np.sign(phi) == np.sign(1)
    
    c1,c2,c3,c4 = 0,0,0,0 
    
    for i,j in zip(a,b): 
        if i == True and j == True:
            c1+=1
        elif i == False and j == True: 
            c2+=1
        elif i == False and j == False: 
            c3+=1
        else: 
            c4+=1

    score_array  = [c1,c2,c3,c4]
    symmetry = False
    
    # Checks for evidence of symmetry based on a roughly equal (and non-zero) number of shear forces pointing in opposite directions
    if np.abs(c1-c3)<=3 and (c1 != 0 and c3 != 0):
        symmetry = True
    elif np.abs(c2-c4)<= 3 and (c2!=0 and c4!= 0): 
        symmetry = True

    # Checks which 2 components are the most dominant across all taxels
    principle_component = np.argmax(score_array)
    score_array[principle_component]=0
    
    secondary_component = np.argmax(score_array)
    components = [principle_component, secondary_component]
    components.sort()
    
    parallel_directions = [[0,1],[1,2],[2,3],[0,3]]
    
    # If the two predominant components of the shear forces are adjacent then a flag is raised to indicate evidence of forces working in parallel
    if components in parallel_directions: 
        parallel = True
    else: 
        parallel = False
    
    return symmetry, parallel

def select_desired_features(full_features, desired_features, feature_dict): 
    """
    A function which reduces a feature set down to only the desired features specified in a list 
    Features must match with keys stored in the passed dictionary 
    """
    
    # print(f"{full_features.shape[1]} attributes available for selection")
    feature_index_list = []
    for i in desired_features: 
        feature_index_list.append(feature_dict[i])
    new_features = full_features[:,feature_index_list]  
    # print(f"{new_features.shape[1]} attributes selected for classification")
    return new_features