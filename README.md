# Cat Finder
### Everything is this world is either a cat or not a cat!

![alt text](https://github.com/anthonymirand/CatFinder/blob/master/detected/cat_04_detected.png)


## Implementation
The script utilizes the [Cat](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalcatface.xml) Haar features from [OpenCV](https://github.com/opencv/opencv/)'s collection. This is simply an exercise in OpenCV.


## How to Install
The script makes heavy use of the [OpenCV](https://github.com/opencv/opencv/) Python library. If you do not have this installed, you can run the command `$ brew install opencv` in your command-line/terminal of choice. If you don't have [Homebrew](https://github.com/Homebrew) installed, you should. Go ahead and run `$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"` to save yourself from future headaches.


## Use
To find cats, Github gives you two options to do so using this repository: cloning (through git) or downloading as a compressed file. Navigate to the root folder and run `$ python cat_finder.py` to get started: this will run the script on a default cat image and places the detected image in the 'detected' folder. To use your own image, you can run either `$ python cat_finder.py --image=PATH/TO/IMAGE` or `$ python cat_finder.py -i PATH/TO/IMAGE`.

