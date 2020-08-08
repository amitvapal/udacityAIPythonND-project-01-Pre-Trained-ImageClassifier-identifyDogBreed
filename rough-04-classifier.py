# Defining lists to populate dictionary 
filenames = ["Beagle_01141.jpg", "Beagle_01125.jpg", "skunk_029.jpg" ]
pet_labels = ["beagle", "beagle", "skunk"]
classifier_labels = ["walker hound, walker foxhound", "beagle",
                     "skunk, polecat, wood pussy"]
pet_label_is_dog = [1, 1, 0]
classifier_label_is_dog = [1, 1, 0]

# Defining empty dictionary
results_dic = dict()

for index in range(0, len(filenames), 1):
    print(index)

    if filenames[index] not in results_dic:
        results_dic[filenames[index]] = [pet_labels[index], classifier_labels[index]]
    
    if pet_labels[index] in classifier_labels[index]:
        results_dic[filenames[index]].append(1)
    else:
        results_dic[filenames[index]].append(0)


for idx in range(0, len(filenames), 1):
    results_dic[filenames[idx]].extend([pet_label_is_dog[idx],classifier_label_is_dog[idx]])




print(results_dic)

for key in results_dic:
    print(key)
    print(f"\nFilename={key} \npet_image Label={results_dic[key][0]} \nClassifier_Label = {results_dic[key][1]} \nMatch={results_dic[key][2]} \nImage is dog={results_dic[key][3]} \nClassifier is dog={results_dic[key][4]}")


    print(sum(results_dic[key][2:])) 
    if sum(results_dic[key][2:]) == 3:
        print("Breed Match")
    
    if sum(results_dic[key][3:]) == 2:
        print("Is a dog match")
    
    if sum(results_dic[key][3:]) == 0 and results_dic[key][2] == 1:
        print("Not a Dog Match")
        

