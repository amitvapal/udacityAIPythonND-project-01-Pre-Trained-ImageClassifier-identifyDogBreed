
from os import listdir
def get_pet_labels(image_dir):
  in_files = listdir(image_dir)
  print(len(in_files))

  list_pet_labels = []

  for idx in range(0, len(in_files), 1):
    if in_files[idx][0] != ".":
      pet_label = in_files[idx].split("_")

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
  results_dic = dict()
  items_in_dic = len(results_dic)
  print("\nEmpty Dictionary results_dic - n items=", items_in_dic)

  # Add new key-value pairs to dictionary ONLY when key doesn't already exist. This dictionary's a list that contains only on item - the pet image label.

  print(len(in_files))
  print(len(list_pet_labels))

  for idx in range(0, len(in_files)):
    if in_files[idx] not in results_dic:
      results_dic[in_files[idx]] = list_pet_labels[idx]
    else:
      print("** Warning: Key=", in_files[idx], "already exists in results_dic with value =", results_dic[in_files[idx]])
  #print(results_dic)
  return results_dic

results_dic = get_pet_labels("/Users/amitvapal/Documents/Udacity-AI-Python/02-IntroductionToPyhton/project/AIPND-revision-master/intropyproject-classify-pet-images/pet_images")


for key in results_dic:
    modelLabel = "/Users/amitvapal/Documents/Udacity-AI-Python/02-IntroductionToPyhton/project/AIPND-revision-master/intropyproject-classify-pet-images/pet_images/" + key
    print(modelLabel)


