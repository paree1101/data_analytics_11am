import imageio.v3 as iio
filenames = ['team-pic1.png', 'team-pic2.png']
images = []
for file in filenames:
    images.append(iio.imread(file))

iio.imwrite('team.gif', images, duration = 500, loop = 0)

# 'team.gif': This is the name you want to give to your new GIF file.
# images: The list containing the image data.
# duration = 500: How long each picture should show in the GIF, in milliseconds.
# loop = 0: How many times the GIF should repeat (0 means it keeps looping forever).