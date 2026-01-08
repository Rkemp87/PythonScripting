from PIL import Image, ImageFilter

# img = Image.open('.\Pokedex\pikachu.jpg')
#
# filtered_img = img.filter(ImageFilter.EMBOSS)
# filtered_img.save('filtered.png', 'png')
# converted_img = img.convert('L') #transfers it to gray scale
# converted_img.save('converted.png', 'png')
# crooked = filtered_img.rotate(90)
# resize = filtered_img.resize((200, 200))
# resize.show()
# crooked.show()
# box = filtered_img.crop((100, 100, 200, 200))
# box.show()
# filtered_img.show()
# converted_img.show()


ratio_practice = Image.open('astro.jpg')
ratio_practice.thumbnail((400,400)) #saves aspect ratio with maximum value
ratio_practice.save('thumbnail.jpg')


# print(img.format)
# print(img.size)
# print(img.mode)
#
# print(dir(img))