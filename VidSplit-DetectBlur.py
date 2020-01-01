import dlib
import cv2
import imutils
import datetime
import os, errno
from subprocess import Popen, PIPE
import sys
import shutil
import pyautogui
import math
from PIL import Image
import numpy as np
import filecmp

def vid_split():

    print("Splitting videos to images(.jpg) at the videos frames per second.",
          "\n", "For example at 30 FPS, you'll get 30 images for every second of video.", "\n")

    directories = ['C:/', 'D:/', 'X:/']

    for directory in directories:
        video_folder = directory

        filelen = 0
        maxfile = sum([len(files) for r, d, files in os.walk(video_folder)])
        
        pic_num = 1

        for root, dirs, files in os.walk(video_folder):
            for file in files:

                filelen += 1
                print(f"\rProcessed: {filelen} of {maxfile}",end="")
                sys.stdout.flush()
                
                if file.lower().endswith('.wmv'):
                    try:
                        videoFile = os.path.join(root, file)
                        imagesFolder = "images"
                        destFolder = "images"

                        cap = cv2.VideoCapture(videoFile)
                        frameRate = cap.get(cv2.CAP_PROP_FPS)
                        
                        while(cap.isOpened()):

                            frameId = cap.get(1) #current frame number
                            ret, frame = cap.read()
                            if (ret != True):
                                break

                            if (frameId % math.floor(frameRate) == 0):
                                filename = imagesFolder+"/"+str(pic_num)+' - '+str(file)+".jpg"
                                cv2.imwrite(str(filename), frame)
                                pic_num += 1
                        cap.release()
                    except:
                        pass
                elif file.lower().endswith('.mkv'):
                    try:
                        videoFile = os.path.join(root, file)
                        imagesFolder = "images"
                        destFolder = "images"

                        cap = cv2.VideoCapture(videoFile)
                        frameRate = cap.get(cv2.CAP_PROP_FPS)
                        
                        while(cap.isOpened()):

                            frameId = cap.get(1) #current frame number
                            ret, frame = cap.read()
                            if (ret != True):
                                break

                            if (frameId % math.floor(frameRate) == 0):
                                filename = imagesFolder+"/"+str(pic_num)+' - '+str(file)+".jpg"
                                cv2.imwrite(str(filename), frame)
                                pic_num += 1
                        cap.release()
                    except:
                        pass
                elif file.lower().endswith('.avi'):
                    try:
                        videoFile = os.path.join(root, file)
                        imagesFolder = "images"
                        destFolder = "images"

                        cap = cv2.VideoCapture(videoFile)
                        frameRate = cap.get(cv2.CAP_PROP_FPS)
                        
                        while(cap.isOpened()):

                            frameId = cap.get(1) #current frame number
                            ret, frame = cap.read()
                            if (ret != True):
                                break

                            if (frameId % math.floor(frameRate) == 0):
                                filename = imagesFolder+"/"+str(pic_num)+' - '+str(file)+".jpg"
                                cv2.imwrite(str(filename), frame)
                                pic_num += 1
                        cap.release()
                    except:
                        pass
                elif file.lower().endswith('.3gp'):
                    try:
                        videoFile = os.path.join(root, file)
                        imagesFolder = "images"
                        destFolder = "images"

                        cap = cv2.VideoCapture(videoFile)
                        frameRate = cap.get(cv2.CAP_PROP_FPS)
                        
                        while(cap.isOpened()):

                            frameId = cap.get(1) #current frame number
                            ret, frame = cap.read()
                            if (ret != True):
                                break

                            if (frameId % math.floor(frameRate) == 0):
                                filename = imagesFolder+"/"+str(pic_num)+' - '+str(file)+".jpg"
                                cv2.imwrite(str(filename), frame)
                                pic_num += 1
                        cap.release()
                    except:
                        pass
                elif file.lower().endswith('.mp4'):
                    try:
                        videoFile = os.path.join(root, file)
                        imagesFolder = "images"
                        destFolder = "images"

                        cap = cv2.VideoCapture(videoFile)
                        frameRate = cap.get(cv2.CAP_PROP_FPS)
                        
                        while(cap.isOpened()):

                            frameId = cap.get(1) #current frame number
                            ret, frame = cap.read()
                            if (ret != True):
                                break

                            if (frameId % math.floor(frameRate) == 0):
                                filename = imagesFolder+"/"+str(pic_num)+' - '+str(file)+".jpg"
                                cv2.imwrite(str(filename), frame)
                                pic_num += 1
                        cap.release()
                    except:
                        pass
                elif file.lower().endswith('.webm'):
                    try:
                        videoFile = os.path.join(root, file)
                        imagesFolder = "images"
                        destFolder = "images"

                        cap = cv2.VideoCapture(videoFile)
                        frameRate = cap.get(cv2.CAP_PROP_FPS)
                        
                        while(cap.isOpened()):

                            frameId = cap.get(1) #current frame number
                            ret, frame = cap.read()
                            if (ret != True):
                                break

                            if (frameId % math.floor(frameRate) == 0):
                                filename = imagesFolder+"/"+str(pic_num)+' - '+str(file)+".jpg"
                                cv2.imwrite(str(filename), frame)
                                pic_num += 1
                        cap.release()
                    except:
                        pass
                else:
                    pass

                print("[*] Completed Video Operations! ", "\n")

def faceit():

    print("--->>> DETECTING FACES,", "\n")

    directories = ['C:/', 'D:/', 'X:/']

    for directory in directories:

        image_folder = directory
        facesFolder = "faces"

        filelen = 0
        maxfile = sum([len(files) for r, d, files in os.walk(image_folder)])

        pic_num = 1

        for root, dirs, files in os.walk(image_folder):
            for file in files:

                filelen += 1
                print(f"\rProcessed: {filelen} of {maxfile}",end="")
                sys.stdout.flush()
                
                if file.lower().endswith('.jpg'):
                    try:
                        # Face detector
                        detector = dlib.get_frontal_face_detector()
                        
                        frame = cv2.imread(os.path.join(root,file))
                        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                        # detect faces in the gray scale frame
                        face_rects = detector(gray, 0)

                        # loop over the face detections
                        for i, d in enumerate(face_rects):
                            face_rect = d.left(), d.top(), d.right(), d.bottom()
                            face = Image.fromarray(frame).crop(face_rect)
                            img = np.array(face)
                            fname = "faces/"+str(pic_num)+' - '+str(file)
                            fnameGAN = 'data/'+str(pic_num)+' - '+str(file)
                            cv2.imwrite(str(fname), img) ## REMEMBER TO UNCOMMENT!!!
                            cv2.imwrite(str(fnameGAN), img)
                            #os.remove(os.path.join(root, file))
                            pic_num += 1
                    except Exception as e:
                        pass
                elif file.lower().endswith('.png'):
                    try:
                        # Face detector
                        detector = dlib.get_frontal_face_detector()
                        
                        frame = cv2.imread(os.path.join(root,file))
                        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                        # detect faces in the gray scale frame
                        face_rects = detector(gray, 0)

                        # loop over the face detections
                        for i, d in enumerate(face_rects):
                            face_rect = d.left(), d.top(), d.right(), d.bottom()
                            face = Image.fromarray(frame).crop(face_rect)
                            img = np.array(face)
                            fname = "faces/"+str(pic_num)+' - '+str(file)
                            fnameGAN = 'data/'+str(pic_num)+' - '+str(file)
                            cv2.imwrite(str(fname), img) ## REMEMBER TO UNCOMMENT!!!
                            cv2.imwrite(str(fnameGAN), img)
                            #os.remove(os.path.join(root, file))
                            pic_num += 1
                    except Exception as e:
                        pass
        print("Completed Face Detection!", "\n")

def blurred():

    print("Removing images that are too blurry.", "\n")

    def variance_of_laplacian(image):
            return cv2.Laplacian(image, cv2.CV_64F).var()

    search_folder = "images"

    filelen = 0
    maxfile = sum([len(files) for r, d, files in os.walk(search_folder)])

    for root, dirs, files in os.walk(search_folder):
        for file in files:

            filelen += 1
            print(f"\rProcessed: {filelen} of {maxfile}",end="")
            sys.stdout.flush()
            
            if file.lower().endswith('.bat') != True:
                try:
                    image = cv2.imread(os.path.join(root, file))
                    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                    fm = variance_of_laplacian(gray)

                    if fm < float(64):
                        try:
                            os.remove(os.path.join(root, file))
                        except Exception as e:
                            pass
                except:
                    pass
            elif file.lower().endswith('.bat'):
                pass
    print("Finished!", "\n")

    search_folder = "faces"

    filelen = 0
    maxfile = sum([len(files) for r, d, files in os.walk(search_folder)])

    for root, dirs, files in os.walk(search_folder):
        for file in files:

            filelen += 1
            print(f"\rProcessed: {filelen} of {maxfile}",end="")
            sys.stdout.flush()
            
            if file.lower().endswith('.bat') != True:
                try:
                    image = cv2.imread(os.path.join(root, file))
                    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                    fm = variance_of_laplacian(gray)

                    if fm < float(64):
                        try:
                            os.remove(os.path.join(root, file))
                        except Exception as e:
                            pass
                except:
                    pass
            elif file.lower().endswith('.bat'):
                pass
    print("Finished!", "\n")

def pngfix():
    print("Correcting sRGB color profile of png files.", "\n")
    cwd = os.getcwd()
    print(cwd)
    os.chdir("images")
    print(cwd)
    line = 'pngfix.bat'
    line = str(line)
    process = Popen(line)
    process.wait()
    os.chdir("faces")
    print(cwd)
    line = 'pngfix.bat'
    line = str(line)
    process = Popen(line)
    process.wait()

def Cleanup():

    print("Cleaning up leftovers, removing images below 25x25 in size.", "\n")

    search_folder = ""

    filelen = 0
    maxfile = sum([len(files) for r, d, files in os.walk(search_folder)])

    for root, dirs, files in os.walk(search_folder):
        for file in files:

            filelen += 1
            print(f"\rProcessed: {filelen} of {maxfile}",end="")
            sys.stdout.flush()

            def silentremove(root, file):
                try:
                    os.remove(os.path.join(root, file))
                except OSError as e:
                    if "WinError 5" in str(e):
                        # if cmd sticks on sh try pyautogui.typewrite 
                        line = '(sh '+'&& '+'cd '+root+' &&'+' chmod 777 '+file+')'
                        line = str(line)
                        process = Popen(line, shell=True)
                        process.wait() # Need to Popen chmod 777 the file.
                        os.remove(os.path.join(root, file))
                        #print("Access Denied!")
                    if "WinError 32" in str(e):
                        pass
                    else:
                        pass

            if file.lower().endswith('.jpg_original'):
                silentremove(root, file)
            else:
                pass
            if file.lower().endswith('.png_original'):
                silentremove(root, file)
            else:
                pass
            if file.lower().endswith('.jpg'):
                im = Image.open(file)
                width, height = im.size
                if width <= 25 and height <= 25:
                    silentremove(root, file)
                elif width >= 25 and height >= 25:
                    fbytes = os.path.getsize(os.path.join(root, file))
                    if fbytes <= 0:
                        silentremove(root, file)
                    else:
                        pass
            else:
                pass
            if file.lower().endswith('.png'):
                im = Image.open(file)
                width, height = im.size
                if width <= 25 and height <= 25:
                    silentremove(root, file)
                elif width >= 25 and height >= 25:
                    fbytes = os.path.getsize(os.path.join(root, file))
                    if fbytes <= 0:
                        silentremove(root, file)
                    else:
                        pass
            else:
                pass
            
    blurred()

def del_dupls():

    print("Deleting duplicate images, and sorting images.", "\n")

    def filter_and_move():

        image_folder = "images"
        destFolder = "faces"

        def filter_img(root, file):
            print("Detecting Duplicates", "\n")
            for r, ds, fils in os.walk(destFolder):
                for f in fils:
                    comp = filecmp.cmp(os.path.join(root, file), os.path.join(r, f), shallow=False)
                    if comp == True:
                        os.remove(os.path.join(r, f))
                        print('Duplicate!!')

        def move_img(root, file):
            src = os.path.join(root, file)
            dst = os.path.join(destFolder, file)
            shutil.move(src,dst)
            print('< IMG >')

        for root, dirs, files in os.walk(image_folder):
            for file in files:
                if file.lower().endswith('.jpg'):
                    filter_img(root, file)
                    move_img(root, file)
                elif file.lower().endswith('.png'):
                    filter_img(root, file)
                    move_img(root, file)


    filter_and_move()

blurred()
vid_split()
blurred()
faceit()
pngfix()
Cleanup()
del_dupls()
