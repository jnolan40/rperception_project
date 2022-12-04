# MEEN 689 - Robotic Perception Project
Code repository for final project for MEEN 689 Robotic Perception

## Problem

In an empty world, we have a chair that has a linear oscillating motion. This chair is equipped with and Inertial Measurement Unit. and is being observed by a camera.

## Objective

To write a Kalman filter to combine the data from the camera and the IMU to estimate the position of the chair at any given time.

## Execution
We have YOLOv5 running on the camera output to recognize the chair ang give us a bounding box. Based on this bounding box, we are identifying the position of the chair by finding the centre  and the deviation from it's last state to measure it's displacement. This gives us a one input for the chair's position. Since we are identifying position from angular deviation, a non-linear function is used, and hence a Extended Kalman Filter is implemented here.

From the IMU we are accepting linear acceleration to get a position estimate by using a normal Kalman Filter.

## Results

