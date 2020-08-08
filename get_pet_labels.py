#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: 
# DATE CREATED:                                  
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
'''
def get_pet_labels(image_dir):


  """
  Creates a dictionary of pet labels (results_dic) based upon the filenames 
  of the image files. These pet image labels are used to check the accuracy 
  of the labels that are returned by the classifier function, since the 
  filenames of the images contain the true identity of the pet in the image.
  Be sure to format the pet labels so that they are in all lower case letters
  and with leading and trailing whitespace characters stripped from them.
  (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
  Parameters:
    image_dir - The (full) path to the folder of images that are to be
                classified by the classifier function (string)
  Returns:
    results_dic - Dictionary with 'key' as image filename and 'value' as a 
    List. The list contains for following item:
        index 0 = pet image label (string)
  """
  # Replace None with the results_dic dictionary that you created with this
  # function

  in_files = listdir(image_dir)
  #print(in_files

  list_pet_labels = []
  for idx in range(0, len(in_files), 1):    
    # Skips file if starts with . (like .DS_Store of Mac OSX) because it 
    # isn't an pet image file
    if in_files[idx][0] != ".":
      # Creates temporary label variable to hold pet label name extracted 
      pet_label = in_files[idx].split("_")
      #print(pet_label)

      # TODO: 2a. BELOW REPLACE pass with CODE that will process each 
      #          filename in the in_files list to extract the dog breed 
      #          name from the filename. Recall that each filename can be
      #          accessed by in_files[idx]. Be certain to place the 
      #          extracted dog breed name in the variable pet_label 
      #          that's created as an empty string ABOVE
      if len(pet_label) == 2:
        #print(pet_label[0])
        pet_label_01 = pet_label[0]
        list_pet_labels.append(pet_label_01)

      elif len(pet_label) == 3:
        #print(" ".join(pet_label[0:2]))
        pet_label_01 = " ".join(pet_label[0:2])
        list_pet_labels.append(pet_label_01)

      elif len(pet_label) == 4:
        #print(" ".join(pet_label[0:3]))
        pet_label_01 = " ".join(pet_label[0:3])
        list_pet_labels.append(pet_label_01)


  print(len(in_files))
  print(len(list_pet_labels))

  # Create empty dictionary named results_dic
  results_dic = dict()

  # Add new key-value pairs to dictionary ONLY when key doesn't already exist. This dictionary's a list that contains only on item - the pet image label.

  for idx in range(0, len(in_files)):
    if in_files[idx] not in results_dic:
      results_dic[in_files[idx]] = list_pet_labels[idx]
    else:
      print("** Warning: Key=", in_files[idx], "already exists in results_dic with value =", results_dic[in_files[idx]])

  #print(results_dic)

  return results_dic
'''

def get_pet_labels(image_dir):
  in_files = listdir(image_dir)
  #print(len(in_files))

  list_pet_labels = []

  for idx in range(0, len(in_files), 1):
    if in_files[idx][0] != ".":
      pet_label = in_files[idx].split("_")

      if len(pet_label) == 2:
        #print(pet_label[0])
        pet_label_01 = pet_label[0]
        list_pet_labels.append([pet_label_01.lower()])
      elif len(pet_label) == 3:
        #print(" ".join(pet_label[0:2]))
        pet_label_01 = " ".join(pet_label[0:2])
        list_pet_labels.append([pet_label_01.lower()])
      elif len(pet_label) == 4:
        #print(" ".join(pet_label[0:3]))
        pet_label_01 = " ".join(pet_label[0:3])
        list_pet_labels.append([pet_label_01.lower()])
  results_dic = dict()
  items_in_dic = len(results_dic)
  
  #print("\nEmpty Dictionary results_dic - n items=", items_in_dic)

  # Add new key-value pairs to dictionary ONLY when key doesn't already exist. This dictionary's a list that contains only on item - the pet image label.

  #print(len(in_files))
  #print(len(list_pet_labels))

  for idx in range(0, len(in_files)):
    if in_files[idx] not in results_dic:
      results_dic[in_files[idx]] = list_pet_labels[idx]
    else:
      print("** Warning: Key=", in_files[idx], "already exists in results_dic with value =", results_dic[in_files[idx]])

  return results_dic




