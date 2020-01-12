from imageio import mimsave, imread
import os


def gen_gif():
    filenames = ["frame" + str(i).zfill(5) + ".png" for i in range(0, 2510, 50)]
    images = []
    for i in filenames:
        images.append(imread(i))
    mimsave("cfd_simulation.gif", images)
    return True


def remove_images():  # call to delete images once the gif has been generated
    for i in range(0, 2510, 50):
        os.remove("frame" + str(i).zfill(5) + ".png")
    return True
