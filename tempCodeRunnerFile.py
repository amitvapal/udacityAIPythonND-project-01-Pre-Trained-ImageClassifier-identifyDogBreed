in_files = listdir(image_dir)
print("\n")
#print(in_files)


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

#print("\n\n\n\n\n\n")        
#print(list_pet_labels)

# Create empty dictionary named results_dic
results_dic = dict()

# Determine number of items in dictionary
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

