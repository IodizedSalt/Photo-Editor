import PIL, os
from PIL import Image

# os.chdir('usr\\home\\David\\Desktop') # change to directory where image is located

picture= Image.open('Transparent.jpg')

copypic = picture.rotate(90, expand=True)

copypic.save('newphotorotated.png')