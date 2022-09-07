import cv2
import os
# def video_to_frames_url_auto(url=None, folder='/home/cc/projects/'):
#     """Function to extract frames from input video url or file and save them as separate frames 
#     in an output directory. Output directory will be named starting from video_1. If a new file is downloaded,
#     a video_2 folder will be created and so on.
#     Dependencies: 
#         OpenCV
#         youtube-dl (sudo pip install --upgrade youtube_dl)
    
#     Args:
#         url: Youtube video URL.
#         folder: Directory to download and save each frames.
        
#     Returns:
#         None
        
#     Work to be done:
#     1. Handle exceptions
#     """
#     import os
#     import re
#     import cv2
#     import time
    
#     # Log start time
#     time_start = time.time()
    
#     # To make a directory for saving video automatically considering all the existing foldernames
#     reg = re.compile(r'^video_')
#     lst = sorted(os.listdir(folder))
#     newlist = filter(reg.match, lst)
#     numbers = [reg.sub('', x).strip() for x in newlist]
#     results = map(int, numbers)
#     results = sorted(results)
#     newfile = results[-1] + 1
#     # Make a directory for the video
#     # If no video's exist as of now, create a folder.
#     if(results == None):
#         os.mkdir("video_1")
#     # Create a folder according to the files that are already present.   
#     os.mkdir("video_" + str(newfile))
    
#     file_loc = folder + "video_" + str(newfile) + "/video_" + str(newfile) + ".mp4"
#     # Download from local video file
#     if (url):
#         print("Downloading Youtube Video")
#         os.system("youtube-dl -o " + file_loc + " -f mp4 " + url)
#         cap = cv2.VideoCapture(file_loc)
#     else:
#         print("This is where I should raise an error. --EXCEPTION HANDLING--")

#     video_length = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT)) - 1
#     print ("Number of frames: ", video_length)
#     count = 0
#     print ("Converting video..\n")
#     while cap.isOpened():
#         ret,frame = cap.read()

#         cv2.imwrite(folder + "video_" + str(newfile) + "/%d.jpg" % (count+1), frame)
#         count = count + 1
#         if (count > (video_length-1)):
#             time_end = time.time()
#             cap.release()
#             print ("Done extracting frames.\n%d frames extracted" %count)
#             print ("It took %d seconds for conversion." %(time_end-time_start))
#             break

# video_to_frames_url_auto(url='https://www.youtube.com/watch?v=HMOI_lkzW08', folder='./frame')
# import os

from pytube import YouTube
import os

def downloadYouTube(videourl, path):

    yt = YouTube(videourl)
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists(path):
        os.makedirs(path)
    output = yt.download(path)
    os.rename(output, 'test1.mp4')
    # print(os.rename(output, 'test1')

downloadYouTube('https://www.youtube.com/watch?v=HMOI_lkzW08', './videos/FindingNemo1')

# print("Downloading Youtube Video")
# url = 'https://www.youtube.com/watch?v=HMOI_lkzW08'
# os.system("youtube-dl -o " + "test1.mp4" + " -f mp4 " + url) 
video_name = "test1.mp4" # or any other extension like .avi etc
vidcap = cv2.VideoCapture(video_name)
success,image = vidcap.read()
count = 1
i = 1
while success:
    if count  % 100 == 1:
        cv2.imwrite("frame/frame%d.jpg" % i, image)     # save frame as JPEG file 
        i += 1     
    success,image = vidcap.read()
    print('Read a new frame: ', success)
    count += 1