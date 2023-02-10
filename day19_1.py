def changenum(jin, num):
    if num < jin:
        if num > 10:
            num = chr(65 + num - 10)
        print(f'{jin}진수 : {num}', end='')
    else:
        changenum(jin, num//jin)
        if num % jin > 10:
            num = chr(65 + num - 10)
        print(num, end='')


changenum(32, 60)