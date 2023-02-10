
def triangle(x, y, z):
    if z >= 3:
        print(x, y, z)
        triangle(x, y, z/2)
        triangle(x + z/2, y, z/2)
        triangle(x+z/4, y-z*3**(0.5)/4, z/2)

    else:
        return

triangle(5, 5, 20)
