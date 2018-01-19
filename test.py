from casacore.images import image
im = image('example_cube.image')
print(im.getdata().mean())
