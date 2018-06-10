import numpy as np
from PIL import Image
import copy
import sys

path_image = sys.argv[1]
path_filter = sys.argv[2]
path_dest = sys.argv[3]
print(sys.argv)



img = Image.open(path_image, 'r')
print(np.array(img).shape)
img_w, img_h = img.size
filter_img = Image.open(path_filter, 'r')
filter_img = filter_img.resize((img_w, img_h))
ft_w, ft_h = filter_img.size

img.paste(filter_img, (0,0), filter_img)
#imshow(np.asarray(img))
img.save(path_dest)

#img, filteri = transform('./transformed.png', './filter.png', './output.png')
