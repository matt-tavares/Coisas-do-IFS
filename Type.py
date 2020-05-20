def tipo(valor):
    try:
        int(valor)
        return True
    except:
        TypeError

while 1:
    x = input("Digite: ")
    if tipo(x):
        print("Ok!")
        break
    else:
        print("Error!")