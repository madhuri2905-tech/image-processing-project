In the first line of this code, we are importing cv2 library
At the second line of the code we're are defining a variable - "cap". And insode this variable we are we are capturing the vedio using the function - VideoCapture
In the third line and it's following two lines of the code, we are putting a condition saying - if the video is unable to be opened or not able to axis, then a massage will appear saying - "cannot open camera", then the screen will exit automatically.
At the sixth line of the code, we are starting a infinity loop - "while True:"
The lines (code) iside the loop:-
  - we are defining two varables, ret and frame
  - ret(return) is a boolean variable which returns true if the frame is projected and returns false if it is not
  - and in the next line there is a condition saying if frame is not found and the ret returns false then, a massage is printed saying "cannot recieve the frame"
  - then the loop breaks.
  - if the ret returns True, then the frame is projected.
  - in the eleventh line of code inside the loop, we are projecting the frame using the function "imshow".
  - then another condition is written which lets the screen or frmae to close when "q" is pressed on the keyboard.
  - and at last the lood breaks.
At the last the function release is used to break the link with the video source and clear the pointer, preventing dangling references.
At the end of the code we are closing all the windows.
