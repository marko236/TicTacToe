fl=[[' ' for i in range(3)]for i in range(3)]
x=0
import os
def draw():
    os.system("clear")
    print("K   1   2   3")
    print("R /-----------\\")
    for i in range(2):
        print(str(i+1)+" | ",end="")
        for j in range(3):
            print(fl[i][j],end=' | ')
        print("\n  |-----------|")
    print("3 |",end=' ')
    for i in range(3):
        print(fl[2][i],end=' | ')
    print("\n  -------------")
while True:
    draw()
    x+=1
    k=int(input("Kolona: "))
    r=int(input("Red: "))
    k-=1
    r-=1
    if x%2==1:
        if r<=2 and k<=2:
            if fl[r][k]==' ':
                fl[r][k]='X'
            else:
                print("Greška, probaj ponovo")
                x-=1
        else:
            print("Greška, probaj ponovo.")
            x-=1
    else:
        if r<=2 and k<=2:
            if fl[r][k]==' ':
                fl[r][k]='O'
            else:
                print("Greška, probaj ponovo")
                x-=1
        else:
            print("Greška, probaj ponovo.")
            x-=1
    if fl[0][0]==fl[0][1]==fl[0][2]=='X' or fl[1][0]==fl[1][1]==fl[1][2]=='X' or fl[2][0]==fl[2][1]==fl[2][2]=='X' or fl[1][0]==fl[2][0]==fl[0][0]=='X' or fl[1][1]==fl[0][1]==fl[2][1]=='X' or fl[2][2]==fl[1][2]==fl[0][2]=='X' or fl[0][0]==fl[1][1]==fl[2][2]=="X" or fl[0][2]==fl[1][1]==fl[2][0]=='X':
        draw()
        print("Pobednik je X")
        break
    elif fl[0][0]==fl[0][1]==fl[0][2]=='O' or fl[1][0]==fl[1][1]==fl[1][2]=='O' or fl[2][0]==fl[2][1]==fl[2][2]=='O' or fl[1][0]==fl[2][0]==fl[0][0]=='O' or fl[1][1]==fl[0][1]==fl[2][1]=='O' or fl[2][2]==fl[1][2]==fl[0][2]=='O' or fl[0][0]==fl[1][1]==fl[2][2]=="O" or fl[0][2]==fl[1][1]==fl[2][0]=='O':
        draw()
        print("Pobednik je O")
        break
    if x==9:
        draw()
        print("Nerješeno")
        break
