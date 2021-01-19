`https://github.com/ridhwaans/image-comparison`
- [image comparison](#image-comparison)
  * [description](#description)
    + [example input CSV](#example-input-csv)
  * [assumptions](#assumptions)
  * [questions and answers](#questions-and-answers)
  * [installation instructions](#installation-instructions)
  * [notes on design and implementation](#notes-on-design-and-implementation)
  * [testing](#testing)
  * [license](#license)

# image comparison

## description
This program takes in a CSV containing the filenames of different image files. Then, the program reads those files and performs an image comparison on two sets of images. It then outputs a new CSV containing the numerical difference between each pair of images and the comparison elapsed time, in addition to the filenames of those images.

### example input CSV
```
image1,image2
aa.png,ba.png
ab.png,bb.png
ac.png,ac.gif
ad.png,bd.png
```

## assumptions
There were some ambiguities in the requirements and I made some assumptions
Assumptions:
1) Image files must be in the same directory as the python solution
2) Input csv must have only two headers 'image1' and 'image2'
3) Input csv must have a comma separated format
4) Supported image types are .png, .gif, .jpg, .jpeg, .bmp
5) There is no requirement if the pairs of images have equal size dimensions
6) The absolute filepath of the input csv must be given if not in the same directory 

## questions and answers

Q) How do you know if your code works?  
A) I like to automate testing such as unit tests, integration and end-to-end tests if any that verify the functionality of the features & pieces of the code. I feel safe and confident as a developer to ship working working code that is backed by a test suite. Also, code reviews should be enforced which promotes code maintainability for all stakeholders. See [testing](#testing) for more information.  

Q) How are you going to teach Bjorn how to use the program?  
A) Writing good documentation and test coverage for the program will explain its usage to Bjorn at a high level and low level. Making sure the test cases run also helps to see the flow. Also, I can schedule a walkthrough or over the shoulder meeting if new users have difficulties.  

Q) Your manager Jeanie is assigning you to a different task and is making Ferris the maintainer of your application. How do you make sure he succeeds?  
A) It is a good practice to keep your code well-documented with inline comments and design docs before checking in, because it brings visibility and tracks edge cases or specific uses which may not be clearly apparent. Code reviews also help bounce ideas off one another, familiarize Bjorn and other maintainers with your work, so that they will be able to hit the ground running.  

Q) How are you ensuring Bjorn gets the latest version of your application?  
A) It is a good practice to introduce a continuous integration & continuous deployment system across the project. With version control & continuous delivery, Bjorn the user will be able to use the latest version of the application, get notified of upcoming updates and rollback any changes if necessary.  
The application can also be containerized so Bjorn is able to get the latest versions. Using Docker or similar orchestration, one can setup service discovery and provide runnable images that help with platform independence  

## installation instructions

1) Make sure git is installed by running `git --version`, if not installed, see below:  
a) if on Mac,
```
# Check for Homebrew and install it if missing
if test ! $(which brew)
then
	echo "Installing Homebrew..."
	ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
fi
brew update
brew tap homebrew/versions
brew upgrade --all
brew install git
```
if on Linux ubuntu
```
apt update
apt install git
```
Other Linux package managers include pacman, yum, rpm etc  

2) Install python and pip through a version manager or a standalone version. It is *recommended* to install a python version manager such as `pyenv-virtualenv` to manage development environments. *(skip to step 3)*  

a) if on Mac, in Terminal
```
# install python and pip
brew install python
brew install python3
sudo easy_install pip
```
b) if on Linux ubuntu, in Terminal
```
apt install python
apt install python3
apt install python-pip python-dev build-essential
```
c) if on Windows, get linux and windows terminal
```
GET Windows Subsystem for Linux https://docs.microsoft.com/en-us/windows/wsl/install-win10#update-to-wsl-2
GET Ubuntu 20.04 LTS (Focal Fossa) from the Microsoft Store
GET Windows Terminal https://docs.microsoft.com/en-us/windows/terminal/get-started
```
Follow the instructions on how to install python on Linux ubuntu from step 2(b) previously  

3) Install `pyenv-virtualenv`  
Follow the instructions on https://github.com/pyenv/pyenv-virtualenv  

*(optional)* installing as submodules
```
git init
git submodule add -f git@github.com:pyenv/pyenv.git .pyenv
cd .pyenv
git submodule add -f git@github.com:pyenv/pyenv-virtualenv.git plugins/pyenv-virtualenv
```

*(optional)* 4) Install from web  
visit `https://www.python.org/downloads/` for the installer  

5) Download the project and install dependencies  
a) In terminal, clone the `image-comparison` GitHub repository using the provided HTTPS or SSH URL  
b) `cd` to the `image-comparison` directory containing the python source code, csv and image files  
c) run `pip install`  

6) Run `python image_comparison.py`  
a) As noted in the assumptions above, the image files and input csv must exist in the same directory as the python program  
b) Given the original CSV, enter `input_csv.csv` when asked at the python question prompt  
c) Enter a new filename for the output csv when asked at the python question prompt  
d) Exit the program `ctrl-c or ^C`. Open the output csv which should be saved in the same directory as the python program

7) Testing
Run `python -m pytest image_comparison.py`, see line `133` or [testing](#testing) for more information  

## notes on design and implementation  
I have kept the code clean and organized into single responsibility methods, guided by SOLID/DRY principles. 
I wanted to keep requiring non-standard, third party libraries at a mininum to reduce bloat so the solution is lightweight. There is some defensive programming and error checking such that exceptions are handled gracefully & there are no silent failures.  
I investigated different implementations for image comparison, and I found approaches such as `pillow imagechops` difference, `mean squared error` in `numpy` to be useful. In the final solution, I used the `opencv2` & `skimage.measure` library to measure a structural similarity index and return the difference between a pair of images.  

## testing  
Due to brevity of time, full coverage is due to be completed. Unit tests are for demonstration purposes.  
Lines `142` to `156` includes `pytest` python tests for testing the edge cases of `getCsv` of the `ImageComparison` class  
Additional test cases to do include:  
- unit tests for other components' functionality,  
- checking for a .csv extension,  
- checking for image type extension,  
- testing the error checking logic with more edge cases  

## license
This work is licensed under GPLv3 - see the [LICENSE](LICENSE) file for details
