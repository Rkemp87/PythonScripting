import sys
import os
from PIL import Image

#grab first and second arguments

original_folder = sys.argv[1]
converted_folder = sys.argv[2]
# print(help(sys))


#check if new exists, if not create it
if not os.path.exists(converted_folder):
    os.makedirs(converted_folder)

#loop through pokedex folder

path_lists = os.listdir(original_folder)
print(path_lists)

#convert images to png
#save to new folder

for path in path_lists:
    img = Image.open(original_folder + '/' + path)
    file_stem = os.path.splitext(os.path.basename(path))[0]
    print(file_stem)
    img.save(f'./new/{file_stem}.png', 'png')