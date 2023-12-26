import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
import glob
import os

class mono_camera_calibration:
    def __init__(self,path):
        self.path = path

    def visualize_images(self,index=21):
        self.calibration_images = glob.glob(f'{self.path}/left_*.png')
        plt.imshow(mpimg.imread(self.calibration_images [index]))
        plt.show()

    def prepare_object_points(self,rows = 6,coloumns=9,square_size=24):
        """
        Prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0) like in a array.
        for my chess board the distance between two sqaures is 2.4 cm (we are taking in mm everytime)
        """
        self.objp = np.zeros((rows*coloumns,3), np.float32)
        self.objp[:,:2] = np.mgrid[0:coloumns, 0:rows].T.reshape(-1,2)*square_size
        ## TYPE OF OUTPUT WE'RE LOOKING FOR:
        ## [[  0.   0.   0.]
        ## [ 24.   0.   0.]
        ## [ 48.   0.   0.]
        ## ...
        ## [192. 120.   0.]]

    #steps to follow 
        # Read a series of images in a loop, typically containing chessboard patterns, using OpenCV's imread function.
        # Convert each image to grayscale using OpenCV's cvtColor function to simplify the corner detection process.
        # Utilize the cv2.findChessboardCorners function to automatically detect the corners of the chessboard in each grayscale image.
        # Optionally refine corner positions with cv2.cornerSubPix for better precision in calibration.
        # Draw the detected chessboard corners on the original images and display them to visually inspect the calibration accuracy.
        # Return the calculated object points (3D points of chessboard corners in the world coordinate system) and image points (2D points of detected corners in image coordinates) for camera calibration


    def get_points(self,rows=6, columns=9):
        # Arrays to store object points and image points from all the images.
        objpoints = [] # 3d points in real world space
        imgpoints = [] # 2d points in image plane.

        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
        # Step through the list and search for chessboard corners
        for idx, fname in enumerate(self.calibration_images):
            image = cv2.imread(fname)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            # Find the chessboard corners
            ret, corners = cv2.findChessboardCorners(gray, (columns,rows), None)

            # If found, add object points, image points
            if ret == True:
                objpoints.append(self.objp)
                imgpoints.append(corners)
                # Draw and display the corners
                cv2.drawChessboardCorners(image, (9,6), corners, ret)
                plt.imshow(image)
                plt.show()
                cv2.waitKey(500)
        return objpoints, imgpoints

    def calibration_funtion(self,img_shape,objpoints, imgpoints):
        flags = (cv2.CALIB_FIX_K1 + cv2.CALIB_FIX_K2+ cv2.CALIB_FIX_K3)

        self.ret,self.mtx, self.dist, self.rvecs, self.tvecs = cv2.calibrateCamera(objpoints, imgpoints, img_shape, None, None,flags=flags)

        print("-- Camera Parameters --")
        print("Root Mean Squared Error (between 0.1 and 1)")
        print(self.ret)
        print("")
        print("Camera Matrix")
        print(self.mtx)
        print("")
        print("Distorion Coefficients Matrix")
        print(self.dist)
        print("")
        print("Rotation Vector")
        print(self.rvecs)
        print("")
        print("Translation Vector")
        print(self.tvecs)
    def show_undistort_image(self):
        img = mpimg.imread(self.calibration_images[0])
        undistorted = cv2.undistort(img, self.mtx, self.dist, None, self.mtx)

        ## TODO2: Display the image before and after distortion
        f, (ax0, ax1) = plt.subplots(1,2,figsize=(20,10))
        ax0.imshow(img)
        ax0.set_title("Original Image")
        ax1.imshow(undistorted)
        ax1.set_title("Undistorted Image")
        plt.show()