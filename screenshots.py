from pickle import FALSE
import cv2
import os
from pathlib import Path

# Read video from specified path
directory = "D:/underwater"


def extract_screenshot(filename):
    cam = cv2.VideoCapture(filename)   
    ret, frame = cam.read()
    delimiter = "-"
    success = True
    if ret:
        # if video is still left continue creating images
        paths = os.path.normpath(filename).split(os.sep)
        stuff = delimiter.join(paths[-3:])
        if len(paths) != 5:
            print("Check file structure ", filename)
            success = False
        else:
            output = os.path.join(".\data", stuff +".jpg")

            print('Creating...' + output)

            # writing the extracted images
            cv2.imwrite(output, frame)

        
    cam.release()
    cv2.destroyAllWindows()
    return (filename, success)


try:
# creating a folder named data
    if not os.path.exists('data'):
        os.makedirs('data')

 # if not created then raise error
except OSError:
    print('Error: Creating directory of data')

currentframe = 0
result = list(Path(directory).rglob("*.mp4"))

problems = []

for video in result:
    file, res = extract_screenshot(str(video))
    if not res:
        problems.append(file)

with open("problems.txt", "w") as f:
    print(f"Encountered {len(problems)} errors")
    for x in problems:
        f.write(x)
        f.write("\n")

print("DONE")
