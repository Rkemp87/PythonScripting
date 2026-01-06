from PIL import Image, ImageFilter

img = Image.open('.\Pokedex\pikachu.jpg')

filtered_img = img.filter(ImageFilter.EMBOSS)
filtered_img.save('filtered.png', 'png')
converted_img = img.convert('L') #transfers it to gray scale
converted_img.save('converted.png', 'png')

# print(img.format)
# print(img.size)
# print(img.mode)
#
# print(dir(img))