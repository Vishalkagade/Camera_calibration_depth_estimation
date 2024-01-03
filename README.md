# Monocular Camera Calibration
The project aim is to calibrate monocular and sterio camera using opencv.


## Data collection and preprossing
The 8*6 chess board is used for camera calibration.27 images of chess board is captured from different angle.The distance between 2 squares is 2.4 cm.The camera is calibrated using the corner of chess boxes which can be found using opencv.

The 3d coordinate in real world(objpoints) and 2d coordinate in image plane (imagepoints) found using opencv function to find the corner of chess sqaures is used to find out the calibration matrix and parameters using opencv.

<img width="404" alt="image" src="https://github.com/Vishalkagade/Camera_calibration_depth_estimation/assets/105672962/dd45eae5-5a9d-4133-9c46-f6c5ae9a2935"> <img width="409" alt="image" src="https://github.com/Vishalkagade/Camera_calibration_depth_estimation/assets/105672962/e51fe1f8-2d7a-4288-9651-e6336d9dcf70">

## Results 
![image](https://github.com/Vishalkagade/Camera_calibration_depth_estimation/assets/105672962/ec4998a8-be32-4c0e-9b33-62639425189b)

refer **test.ipynb** to evaulte result
results without flags

## References
https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html

https://docs.opencv.org/4.x/d9/d0c/group__calib3d.html#ga687a1ab946686f0d85ae0363b5af1d7b

https://courses.thinkautonomous.ai/stereo-vision


