def main():
    print("Введиет слова которые хотите зашифровать:")
    sh = input()
    length = len(sh)
    for i in range(length):        
        print(rot(sh[i]))
    test()
def rot(arg):
    if(ord(arg) != 32 and ord(arg) < 110):
        t = ord(arg)
        t += 13
        sym = chr(t)  
    if(ord(arg) != 32 and ord(arg) >= 110):
        t = ord(arg) 
        t -= 13
        sym = chr(t)
    if(ord(arg) == 32):
        sym = arg
    return sym 
main()
