a1, b1 = input().split("/")
a = int(a1)
b = int(b1)

if (a >= 21 and b == 3) or (a <= 20 and b == 4):
    print("aries")

if (a >= 21 and b == 4) or (a <= 20 and b == 5):
    print("touro")

if (a >= 21 and b == 5) or (a <= 20 and b == 6):
    print("gemeos")

if (a >= 21 and b == 6) or (a <= 22 and b == 7):
    print("cancer")

if (a >= 23 and b == 7) or (a <= 22 and b == 8):
    print("leao")

if (a >= 23 and b == 8) or (a <= 22 and b == 9):
    print("virgem")

if (a >= 23 and b == 9) or (a <= 22 and b == 10):
    print("libra")

if (a >= 23 and b == 10) or (a <= 21 and b == 11):
    print("escorpiao")

if (a >= 22 and b == 11) or (a <= 21 and b == 12):
    print("sagitario")

if (a >= 22 and b == 12) or (a <= 19 and b == 1):
    print("capricornio")

if (a >= 20 and b == 1) or (a <= 18 and b == 2):
    print("aquario")

if (a >= 19 and b == 2) or (a <= 20 and b == 3):
    print("peixes")
    
