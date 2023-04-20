# Video Analysis/Face Recognition Script

This code was tested in Windows 10 and 11 with Python 3.6-3.11.

<b>Required Windows Programs:</b>
- CMake (For certain modules to install correctly. Mainly dlib.)
- Visual Studio (C, C++, and Python) (For certain modules to install correctly. Mainly dlib.)
- ImageMagik (Only needed if you intend to fix sRGB color profiles in .png files with pngfix.bat)

<b>You will need the following Python modules installed:</b>
- Opencv (python -m pip install opencv-python)
- dlib (python -m pip install dlib) #If you recieve an error try the alternate installation
- dlib (alternate install) (First run: python -m pip install cmake , Then Run: python -m pip install dlib)
- imutils (python -m pip install imutils)
- pillow/PIL (python -m pip install pillow)
- pyautogui (python -m pip install pyautogui) # For errors in installation try (python -m pip install win32gui (now pywin32)) first.
- numpy (python -m pip install numpy)

<b>All you need for the file structure is:</b>
- faces
- images
- VidSplit-DetectBlur.py

- If you want to use pngfix.bat put a copy in images and faces

<b>The file is split into functions that:</b>
- Split video by FPS.
- Save as .jpg/.png images.
- Detects faces and crops image to detected face.
- Attempt to correct color profile in certain .png images.
- Deletes files created by the script.
- Deletes files that are exact duplicates even if they have different filenames.
- Delete images too blurry to be used as training data for machine learning.

All functions besides the color profile correction are in the Python script, the pngfix.bat file contains the color profile correction code using ImageMagik.
