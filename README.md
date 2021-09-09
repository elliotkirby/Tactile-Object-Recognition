# Tactile-Object-Recognition
This repository stores code used as part of tactile object recognition task.

10 objects were grasped with a robot gripper with a tactile sensor which is able to detect both shear and normal forces. 

Author: Elliot Kirby, Rodrigo Zenha, Dr Lorenzo Jamone
Project Title: Tactile Object Recognition for objects subjected to the dynamic motion of a robot gripper
Supervisor: Dr Lorenzo Jamone

Overview:
-------------------------------
This README provides a brief overview of the following files:
* Test_functions.py
* Feature Extraction and Visualisations.ipynb
* Test Script - Dynamic Validation.ipynb
* Test Script - Static and Short Dynamic Validation.ipynb
* Test Script - Generalisation Testing.ipynb

An explanation for why an executable file has not been submitted as part of the supporting material is also provided below.

Test_functions.py
-------------------------------
This file contains a number of functions written for the purposes of the project.
It is essential that this module is imported using the name "func" for all other scripts to run.

A brief overview of the functions contained in this file are summarised below:
* get_maximum_stability: Identifies the longest consecutive sequence of zeros from a provided array, indicating the longest duration within the experimental routine where the object is stable with regards to shear and normal forces experienced by the tactile sensor.
* get_maximum_changes: Identifies the longest consecutive sequence of ones from a provided array, indicating the longest duration within the experimental routine where the object is unstable with regards to changing shear and normal forces experienced by the tactile sensor.
* percentage_change_tolerance: Compares the percentage change between two values with a pre-determined threshold value. If the percentage change is less than the threshold amount then a flag of "True" is returned, otherwise it is "False".
* cart2pol: A function for converting cartesian values into polar co-ordinates. Polar co-ordinates are returned as an angle (in degrees) and a magnitude.
* compare_vectors: Compares two vectors to identify the orientation of their directions in relation to one another.
* compare_all_vectors: Compares the directions of shear forces experienced by all 18 taxels from the tactile array. The function highlights evidence of symmetry or forces acting in a parallel direction.
* select_desired_features: A function which is provided with the full set of features extracted, a list of desired features and a dictionary mapping the names of features to the relevant index in the features. The feature array is reduced to only include the values for the features provided in the given list.

Feature Extraction and Visualisations.ipynb
-------------------------------
This file provides an introduction to the way in which features are extracted from the original files containing the data collected from the tactile sensor during the experimental routine.
A number of visualisation techniques are shown which were used to try to identify features which would be beneficial for classification purposes.
Other visualisations include a 3D surface plot which was used to represent how each individual force component (x/y/z) changes between frames.

Test Script - Dynamic Validation.ipynb
-------------------------------
* This notebook is one of three which were used for different elements of testing.
* This notebook was used for testing features using a dynamic data validation approach. This means that validation data is of the same form as training data with access to  the whole experimental routine.
* Each feature is tested in isolation and then promising features have been iteratively combined to form different combinations of features. All individual features and combinations of features are tested using 6 different classifiers.
* Where possible, features have been split into shear and normal forces to provide a comparison of using each component individually and combined.
* The final classifier and combination of features is identified as those which provide the highest accuracy of object identification using the validation dataset.

Test Script - Static and Short Dynamic Validation.ipynb
-------------------------------
* This notebook is one of three which were used for different elements of testing.
* This notebook was used for testing features using a static data validation approach and a short dynamic validation approach
* In the static case a single frame from the experimental routine is used in both training and validation. In each experiment the last 30% of frames are not considered for selecting a frame at random due to the risk that it may represent a frame where the object has already been placed or fallen.
* In the short dynamic approach a 2 second window is extracted at random from the whole experimental routine with the experiments then being split randomly for validation and training datasets.
* In all cases the training:validation split is 70:30.
* Each feature is tested in isolation and then promising features have been iteratively combined to form different combinations of features. All individual features and combinations of features are tested using 6 different classifiers.
* The final classifier and combination of features is identified as those which provide the highest accuracy of object identification using the validation dataset. 
* The purpose of this set of testing is to identify how a static or short dynamic validation approach impacts classification accuracy. Classifiers which require different periods of time to extract information required for accurate classification will have different potential applications.

Test Script - Generalisation Testing
-------------------------------
* This notebook is one of three which were used for different elements of testing.
* This notebook was used for testing features using a dynamic data validation approach. This means that validation data is of the same form as training data with access to the whole experimental routine.
* For this set of testing one of the 5 potential poses is withheld from the initial training / validation datasets.
* The features selected are those which performed best during the dynamic validation approach where all samples were split randomly across all poses.
* The purpose of this set of testing is to identify how the classifier might generalise in a real-world scenario where objects are found in poses not observed during training.

Executable File - Not Possible
-------------------------------
It has not been possible to submit an executable file as part of the provided supporting material.
The reason for this is that the data, which was originally gathered for an alternative project (1), is too large to be included, even after it has been processed. Access to the raw unprocessed data can be provided by Rodrigo (1) via a OneDrive portal.

The original data is stored in ROSbags which can only be accessed using ROS Kinetic and a Linux Ubuntu (16.04) operating system. The first step required is to extract the relevant frames of data available in the ROS bags using a third party piece of software called grid_map (2). Using this package it is possible to move forward and backwards through the frames and to save a section of them by identifying the starting frame and the final frame. To replicate the data collected for this project the starting frame should be the frame prior to any tactile readings being observed and the final frame is when tactile readings are no longer observed. This process would need to be repeated for all objects referenced in the final report, for all poses and experiments. Once desired frames have been identified the files are saved as H5PY files. Further instructions for manipulating H5Py files can be found on Github (3). Before the scripts are to work as expected the details contained in the "object_path_dictionary" seen in each of the test scripts must be changed to reflect the updated file paths and the names of the objects used.


References
-------------------------------
(1) Zenha, R., Denoun, B., Coppola, C., & Jamone, L., 2021. "Tactile Slip Detection in the Wild Leveraging Distributed Sensing of both Normal and Shear Forces". International Conference on Intelligent Robots and Systems (IROS), 2021. (To Appear).
(2) Github, github.com/ANYbotics/grid_map
(3) Github, https://github.com/h5py/h5py
