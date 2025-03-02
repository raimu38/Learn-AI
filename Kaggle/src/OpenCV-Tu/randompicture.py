
import random

WIDTH = 10
HEIGHT = 10


def get_pixels():
    pictures = [[randomPixcel() for _ in range(WIDTH)] for  _  in range(HEIGHT)]
    return pictures
    
def randomPixcel():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return r, g , b


pictures = get_pixels()
print(pictures)


def create_image(image_path):
    with open(image_path, "w") as f:
        f.write(f"P3\n{WIDTH}{HEIGHT}\n255\n")
        for _ in range(HEIGHT):
            for _ in range(WIDTH):
                r, g, b = randomPixcel()
                f.write(f"{r}{g}{b},")
            f.write("\n")
create_image("./img/random.ppm")


    

