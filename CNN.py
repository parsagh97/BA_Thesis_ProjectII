#pip install imagededup 
from imagededup.methods import CNN   3
model = CNN() #name of the model you want yo create and the method you use.
encodings = model.encode_images(image_dir='PATH_TO_THE_DIRECTORY')   
duplicates = model.find_duplicates(encoding_map=encodings) 
print(duplicates) #a dictionary of with a value of list which indicates the duplicat e images in the PWD 
