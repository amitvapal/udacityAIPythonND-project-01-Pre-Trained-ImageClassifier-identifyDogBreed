import os


import ast
from PIL import Image
import torchvision.transforms as transforms
from torch.autograd import Variable
import torchvision.models as models
from torch import __version__

resnet18 = models.resnet18(pretrained=True)
alexnet = models.alexnet(pretrained=True)
vgg16 = models.vgg16(pretrained=True)

models = {'resnet': resnet18, 'alexnet': alexnet, 'vgg': vgg16}

# obtain ImageNet labels
with open('imagenet1000_clsid_to_human.txt') as imagenet_classes_file:
    imagenet_classes_dict = ast.literal_eval(imagenet_classes_file.read())

def classifier(img_path, model_name):
    # load the image
    img_pil = Image.open(img_path)

    # define transforms
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    
    # preprocess the image
    img_tensor = preprocess(img_pil)
    
    # resize the tensor (add dimension for batch)
    img_tensor.unsqueeze_(0)
    
    # wrap input in variable, wrap input in variable - no longer needed for
    # v 0.4 & higher code changed 04/26/2018 by Jennifer S. to handle PyTorch upgrade
    pytorch_ver = __version__.split('.')
    
    # pytorch versions 0.4 & hihger - Variable depreciated so that it returns
    # a tensor. So to address tensor as output (not wrapper) and to mimic the 
    # affect of setting volatile = True (because we are using pretrained models
    # for inference) we can set requires_gradient to False. Here we just set 
    # requires_grad_ to False on our tensor 
    if int(pytorch_ver[0]) > 0 or int(pytorch_ver[1]) >= 4:
        img_tensor.requires_grad_(False)
    
    # pytorch versions less than 0.4 - uses Variable because not-depreciated
    else:
        # apply model to input
        # wrap input in variable
        data = Variable(img_tensor, volatile = True) 

    # apply model to input
    model = models[model_name]

    # puts model in evaluation mode
    # instead of (default)training mode
    model = model.eval()
    
    # apply data to model - adjusted based upon version to account for 
    # operating on a Tensor for version 0.4 & higher.
    if int(pytorch_ver[0]) > 0 or int(pytorch_ver[1]) >= 4:
        output = model(img_tensor)

    # pytorch versions less than 0.4
    else:
        # apply data to model
        output = model(data)

    # return index corresponding to predicted class
    pred_idx = output.data.numpy().argmax()

    return imagenet_classes_dict[pred_idx]


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

  return results_dic


file_path = "/Users/amitvapal/Documents/Udacity-AI-Python/02-IntroductionToPyhton/project/AIPND-revision-master/intropyproject-classify-pet-images/pet_images/" 

#print(os.listdir(file_path))

for item in os.listdir(file_path):
    #print(item)
    file_path_1 = file_path + item
    model_label = classifier(file_path_1, "vgg")
    #print(model_label)
    model_label = model_label.lower()
    model_label= model_label.strip()

    #print(file_path_1)

#model_label = classifier([file_path + item for item in os.listdir(file_path)], "vgg")
#print(model_label)
#prep = [file_path + item for item in os.listdir(file_path)]
#print(prep)
print("hi")