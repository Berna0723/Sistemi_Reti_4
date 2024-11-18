import turtle

def disegnaPoligono(n, l):
    pino = turtle.Turtle()
    for valore in range(0, n):
        pino.forward(l)
        pino.left(360/n)
    pino.screen.mainloop()

n = int(input("inserisci numero lati: "))

if(n < 2):
    exit()

l = int(input("inserisci lunghezza lati: "))

disegnaPoligono(n, l)
