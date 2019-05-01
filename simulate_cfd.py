import sys
sys.path.insert(0, "lib")
import cfd_burger_anim50 as cfd
import generate_gif as gg

def main():
    cfd.simulate()
    gg.gen_gif()
    gg.remove_images()
    return True

main()