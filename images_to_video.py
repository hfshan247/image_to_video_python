# Attempt 1

# import cv2
# import numpy as np
# import glob
 
# img_array = []

# for filename in glob.glob('FLOWS_frame3.tif'):
#     img = cv2.imread(filename)
#     height, width, layers = img.shape
#     size = (width,height)
#     img_array.append(img)
 
 
# out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
 
# for i in range(len(img_array)):
#     out.write(img_array[i])
# out.release()


# Attempt 2

# import cv2
import os

# image_folder = 'flows'
# video_name = 'video.avi'

# images = [img for img in os.listdir(image_folder) if img.endswith(".tif")]
# frame = cv2.imread(os.path.join(image_folder, images[0]))
# height, width, layers = frame.shape

# video = cv2.VideoWriter(video_name, 0, 1, (width,height))

# for image in images:
#     video.write(cv2.imread(os.path.join(image_folder, image)))

# cv2.destroyAllWindows()
# video.release()


# Attempt 3

import cv2
import numpy as np
import glob
import os
 
img_array = []

images = os.listdir("flows")
images.sort()

for filename in images:
    print(filename)
    image = glob.glob('flows/' + filename)
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)

for filename in img_array:
    print(filename)

files = os.listdir("output")
output_name = 'output/project' + str(len(files)) + '.mp4'
out = cv2.VideoWriter(output_name,fourcc=cv2.VideoWriter_fourcc(*'mp4v'),fps=1, frameSize= (width,height))

for i in range(len(img_array)):
    out.write(img_array[i])
out.release()