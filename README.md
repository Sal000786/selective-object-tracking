This is a simple project for selectively tracking an object in a video frame. 

Selective Object Tracking with OpenCV
This repository demonstrates how to perform selective object tracking in a video stream using OpenCV. The code utilizes the CSRT (Channel and Spatial Reliability Tracker) tracker and the selectROI function to enable users to select a region of interest (ROI) in the initial frame of the video for tracking.

How it Works

Video Capture Initialization:

The code initializes a video capture object using cv2.VideoCapture to capture frames from the video stream.

CSRT Tracker Creation:

The CSRT tracker is created using cv2.TrackerCSRT_create().

Select ROI:

The selectROI function is used to interactively select the region of interest (ROI) in the first frame of the video. This function provides a user-friendly way to specify the area to be tracked.

Tracker Initialization:

The CSRT tracker is initialized with the selected ROI using the tracker.init method.

Object Tracking Loop:

The code enters a loop where it continuously reads frames from the video stream and updates the tracker with each new frame.
Drawing Rectangle:

The updated ROI from the tracker is obtained, and a rectangle is drawn around the tracked object on the frame using cv2.rectangle.
Displaying Frame:

The frame with the tracking rectangle is displayed using cv2.imshow.
Exiting the Loop:

The loop continues until the user presses the 'q' key, at which point the program exits.
Release Resources:

After the loop, the video capture object is released using cap.release() to free up system resources.
Close OpenCV Windows:

Finally, all OpenCV windows are closed using cv2.destroyAllWindows().
How to Use
Clone the repository to your local machine.

Install the required dependencies (opencv-python)(that supports csrt or kcf tracker) using pip install -r requirements.txt.

Run the script by providing the path to your video file.

bash
Copy code
python selective_object_tracking.py -v path/to/your/video.mp4
Follow the instructions to select the region of interest (ROI) in the initial frame by clicking and dragging.

Dependencies
OpenCV: Open Source Computer Vision Library
