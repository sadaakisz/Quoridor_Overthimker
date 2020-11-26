#Lo que se busca es, dependiendo de la posición Y del peón en el tablero, los peones decidan poner una pared vertical en frente de su oponente

posPeon1Y = 0
posPeon1X = 4

posPeon2Y = 8
posPeon2X = 4

peonWall1 = 10
peonWall2 = 10

coolDown1 = 2
coolDown2 = 2


while(posPeon1Y != 8 or posPeon2Y != 0):
    if(posPeon1Y == 3 and coolDown2 == 2 and peonWall2 != 0 or posPeon1Y == posPeon2Y and coolDown2 == 2 and peonWall2 != 0):
        print("Pawn 2 added a wall in " ,posPeon1Y + 1)
        peonWall2-= 1
        coolDown2 = 0
    else:
        print("El peon 2 se mueve")
        coolDown2+= 1
    if(posPeon2Y == 6 and coolDown1 == 2 and peonWall1 != 0 or posPeon1Y == posPeon2Y and coolDown1 == 2 and peonWall1 != 0):
        print("Pawn 1 added a wall in", posPeon2Y - 1)
        peonWall1-= 1
        coolDown1 = 0
    else:
        print("El peon 1 se mueve")
        coolDown1+= 1