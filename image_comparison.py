'''
There were some ambiguities in the requirements and I made some assumptions
Assumptions:
1) Image files must be in the same directory as the python solution
2) Input csv must have only two headers 'image1' and 'image2'
3) Input csv must have a comma separated format
4) Supported image types are .png, .gif, .jpg, .jpeg, .bmp
5) There is no requirement if the pairs of images have equal size dimensions
6) The absolute filepath of the input csv must be given if not in the same directory 
'''
__author__ = 'Ridhwaan Shakeel'
__email__ = 'shakeel.ridhwaan@gmail.com'

import os
import mock
import pytest
import builtins
import csv
import sys
import cv2
from skimage.measure import compare_ssim
import time

class ImageComparison():
    def __init__(self):
        self.input_csv = None
        self.output_csv = None
        self.dict_list = {}

    def getCsv(self, prompt):
        """CLI prompt that queries for the input and output csv names
        """
        while True:
            filename = input(prompt) #ask for filename using the given prompt
            if self.validate(filename):
                if (self.input_csv is None):
                    self.input_csv = filename
                else:
                    self.output_csv = filename
                break
            else:
                print("Not found. Try again")

    def buildDictionary(self):
        """Data structure later used for comparing images and writing to CSV
        """
        try:
            reader = csv.DictReader(open(self.input_csv, 'r'))
            fields = [item.lower() for item in reader.fieldnames]
            if (fields != ["image1", "image2"]):
                raise AttributeError
            self.dict_list[reader.fieldnames[0]] = []
            self.dict_list[reader.fieldnames[1]] = []
            for line in reader:
                self.dict_list[reader.fieldnames[0]].append(line[reader.fieldnames[0]])
                self.dict_list[reader.fieldnames[1]].append(line[reader.fieldnames[1]])
            if len(self.dict_list[reader.fieldnames[0]]) != len(self.dict_list[reader.fieldnames[1]]):
                raise ValueError
        except AttributeError:
            print("Not a valid field")
        except TypeError:
            print("Not a valid image type")
        except ValueError:
            print("Not a valid number of pairs")
        except:
            print("An unknown error occurred when building the dictionary")

    def compare(self):
        """Image comparison algorithm which takes in pairs of images defined in the input CSV
        """
        try:
            self.dict_list["similar"] = []
            self.dict_list["elapsed"] = []
            for i, val in enumerate(self.dict_list["image1"]):
                one = cv2.imread(self.dict_list["image1"][i])
                two = cv2.imread(self.dict_list["image2"][i])
                start_time = time.time()
                # convert the images to grayscale
                grayA = cv2.cvtColor(one, cv2.COLOR_BGR2GRAY)
                grayB = cv2.cvtColor(two, cv2.COLOR_BGR2GRAY)
                # compute the Structural Similarity Index (SSIM)
                (score, diff) = compare_ssim(grayA, grayB, full=True)
                elapsed_time = time.time() - start_time
                # record the difference and time spent to perform the comparison
                self.dict_list["similar"].append(score)
                self.dict_list["elapsed"].append(elapsed_time)
        except IOError:
            print("Image not found")
        except AttributeError:
            print("Image sizes are not identical")
        except:
            print("An unknown error occurred during comparison")
    
    def saveCsv(self):
        """Saves the results dictionary into a CSV by the name of user's choice
        """
        if (self.output_csv):
            with open(self.output_csv, 'w') as csv_file:  
                writer = csv.writer(csv_file)
                writer.writerow(("image1", "image2", "similar", "elapsed"))
                for i, val in enumerate(self.dict_list["image1"]):
                    writer.writerow((
                        [self.dict_list["image1"][i], 
                         self.dict_list["image2"][i],
                         self.dict_list["similar"][i],
                         self.dict_list["elapsed"][i]]))
        print("File saved. Check directory")

    def validate(self, filename):
        """Checks if the input file exists
        """
        if filename is None:
            return False
        filename = filename.strip()
        if filename == '':
            return False
        elif (self.input_csv is None) and not (os.path.exists(filename)):
            return False
        else:
            return True

if __name__ == "__main__":
    try:
        imgCompare = ImageComparison()
        imgCompare.getCsv("Enter the path and filename of input CSV:") # input_csv.csv
        imgCompare.buildDictionary()
        imgCompare.compare()
        imgCompare.getCsv("Enter a filename for output CSV (same directory):") # output.csv  
        imgCompare.saveCsv()
    except:
        print("An unknown error occured")

# python -m pytest image_comparison.py
# valid: ['print-file.py']
# invalid: [None, '', 'nonexistent']
# additional test cases include: 
# unit tests for other components  
# checking for a .csv extension,  
# checking for image type extension 
def test_01():
    with mock.patch.object(builtins, 'input', side_effect=['aa.jpg']):
        assert main("Enter filename") == "File exists"

def test_02():
    with mock.patch.object(builtins, 'input', side_effect=['  ']):
        assert main("Enter filename") == "File does not exist"

def test_03():
    with mock.patch.object(builtins, 'input', side_effect=[None]):
        assert main("Enter filename") == "File does not exist"

def test_04():
    with mock.patch.object(builtins, 'input', side_effect=['nonexistent']):
        assert main("Enter filename") == "File does not exist"