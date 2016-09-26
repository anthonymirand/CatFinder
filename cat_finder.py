# #!/usr/bin/python

from optparse import OptionParser
import os.path
import cv2

parser = OptionParser(usage="usage: %prog [options] image", version="%prog 1.0")
parser.add_option("-i", "--i", dest="image", help="read cat from IMAGE")
options, args = parser.parse_args()

# Reads a cat image
if options.image:
    if not os.path.isfile(options.image):
        print "File '{}' does not exist".format(options.image)
        exit()
    image = options.image
else: # Use default cat image
    image = "images/cat_01.jpg"

cat_img = cv2.imread(image)
cat_gray = cv2.cvtColor(cat_img, cv2.COLOR_BGR2GRAY)

cat_cascade = cv2.CascadeClassifier("haarcascade_frontalcatface.xml")
cat_faces = cat_cascade.detectMultiScale(cat_gray, scaleFactor=1.3, minNeighbors=10, minSize=(75, 75))

# Draw rectangle onto region where cat face is found
for (i, (x, y, w, h)) in enumerate(cat_faces):
    cv2.rectangle(cat_img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(cat_img, "CAT #{}".format(i + 1), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 255, 0), 2)

print "OpenCV detected {0} cat(s) in {1}".format(len(cat_faces), image)
if len(cat_faces) > 0:
    # Add detected image to directory
    if not os.path.exists("./detected/"):
        os.makedirs("./detected/")
    # Shows images and destroy window after 5 seconds
    cv2.imshow("Cats", cat_img)
    cv2.imwrite("detected/{}_detected.png".format(os.path.basename(image).split('.')[0]), cat_img)
    cv2.waitKey(5000)
