import pygame,sys
from pygame.locals import * 

"""Algunos colores y variables que se usaran en el codigo"""
verde = (0,0,238)
blanco = (255,255,255)
ancho = 900
alto = 574


anchoL = 80
largoL = 20
colorL = (150,200,0)
colorl1 = (30,30,30)
colorl3 = (127,255,0)



class Bola(pygame.sprite.Sprite):
    """Clase que representa la bola"""
    def __init__(self, posx, posy): 
       """
          Inicializador de la clase 'Bola'.
          :param barra: Imagen bola
          :param rect: Obtiene el rectangulo de la imagen de la bola
          :param rect.centerx: Posicion inicial de la barra en x
          :param rect.centery: Posicion inicial de la barra en y
          :param veloci: Velocidad de la bola
          :param puntos: Inicializacion del puntaje en el juego
          :param sonido1: Sonido de la bola al colisionar y destruir un ladrillo
          :param sonido2: Sonido cuando la bola rebota con la plataforma
          :param sonido3: Sonido cuando pierdes el juego (la bola se cae)
          :param injuego: Variable booleana
        """
       pygame.sprite.Sprite.__init__(self)
       self.bola = pygame.image.load("imagenes/BalonChile.png")
       self.rect = self.bola.get_rect()
       self.rect.centerx = ancho/2
       self.rect.centery = alto-45
       self.veloci = [2,2]
       self.puntos = 0
       self.sonido1 = pygame.mixer.Sound('sonidos/rompe_bloque.wav')
       self.sonido2 = pygame.mixer.Sound('sonidos/fireball.wav')
       self.sonido3 = pygame.mixer.Sound('sonidos/fallo2.wav')
       self.injuego = True
       if pygame.font:
            self.font = pygame.font.Font(None, 30)
       else:
            self.font = None
       self.creacionladrillos(Barra)
       self.creacionladrillos2(Barra)
       self.creacionladrillos3(Barra)
       
    def agregar2(self, superficie):
        """Muestra bola.

           Metodo de la clase Bola, dibuja la
           bola en la ventana llamada "superficie"
        """
        superficie.blit(self.bola, self.rect)
   
    def mover(self, jugador):
       """Movimiento de la bola.

          Este metodo de la clase Bola determina el rango de movimiento
          de la bola en los margenes de la ventana y la colision que realiza
          con la plataforma, asi mismo reproduce sonidos respectivos de
          colision o cuando cae la bola
       """
       self.rect = self.rect.move(self.veloci)
       if self.injuego == True:  
          
          if self.rect.left < 0 or self.rect.right > ancho:
             self.veloci[0] = -self.veloci[0]
             
          if self.rect.bottom-33 < 0:
             self.veloci[1] = -self.veloci[1]
          if self.rect.top == alto:
             pygame.mixer.music.stop()
             self.sonido3.play()
             
          if pygame.Rect.colliderect(self.rect, jugador):
             self.veloci[1] = -self.veloci[1] 
             self.sonido2.play() 
   

    def creacionladrillos(self,barra):
         """Creacion ladrillos.
            
            Este metodo crea los ladrillos
            del nivel 1 mediante iteraciones
         """
         y_ofs = 35
         self.ladrillos = []
         for i in range(3):
            x_ofs = 35
            for j in range(9):
                self.ladrillos.append(pygame.Rect(x_ofs,y_ofs,anchoL,largoL))
                x_ofs += anchoL + 10
            y_ofs += largoL + 5
           
    def creacionladrillos2(self,barra):
         """Creacion ladrillos.
            
            Este metodo crea los ladrillos
            del nivel 2 mediante iteraciones
         """
         y_ofs = 35
         self.ladrillos2 = []
         for i in range(4):
            x_ofs = 35
            for j in range(9):
                self.ladrillos2.append(pygame.Rect(x_ofs,y_ofs,anchoL,largoL))
                x_ofs += anchoL + 10
            y_ofs += largoL + 5       
          
    def creacionladrillos3(self,barra):
         """Creacion ladrillos.
            
            Este metodo crea los ladrillos
            del nivel 3 mediante iteraciones
         """
         y_ofs = 35
         self.ladrillos3 = []
         for i in range(5):
            x_ofs = 35
            for j in range(9):
                self.ladrillos3.append(pygame.Rect(x_ofs,y_ofs,anchoL,largoL))
                x_ofs += anchoL + 10
            y_ofs += largoL + 5  
            
  
    def dibujarL(self, vent):
        """Dibuja ladrillos nivel 1.

           Esta funcion, mediante iteraciones va dibujando
           los ladrillos de la primera matriz en pantalla
           para el nivel 1          
        """
        for ladrillo in self.ladrillos: 
            pygame.draw.rect(vent, colorL, ladrillo)
        if len(self.ladrillos) == 0:
               NIVEL2()
   
    def dibujarL2(self, vent):
        """Dibuja ladrillos nivel 2.

           Esta funcion, mediante iteraciones va dibujando
           los ladrillos de la segunda matriz en pantalla
           para el nivel 2          
        """
        for ladrillo in self.ladrillos2: 
             pygame.draw.rect(vent, colorl1, ladrillo)
        if len(self.ladrillos2) == 0:
               NIVEL3()

    def dibujarL3(self, vent):
        """Dibuja ladrillos nivel 3.

           Esta funcion, mediante iteraciones va dibujando
           los ladrillos de la tercera matriz en pantalla
           para el nivel 3          
        """
        for ladrillo in self.ladrillos3: 
             pygame.draw.rect(vent, colorl3, ladrillo)
    
             
   
    def colicion(self, barra):
        """Eliminacion del ladrillo nivel 1.

           Este metodo borra el ladrillo de la
           matriz (se destruye) en el momento
           en que la bola colisiona con este
           en el nivel 1
        """
        for ladrillo in self.ladrillos:
            if self.rect.colliderect(ladrillo):
                self.puntos += 3
                self.veloci[1] = -self.veloci[1]
                self.ladrillos.remove(ladrillo)
                self.sonido1.play()

    def colicion2(self, barra):
        """Eliminacion del ladrillo nivel 2.

           Este metodo borra el ladrillo de la
           matriz (se destruye) en el momento
           en que la bola colisiona con este
           en el nivel 2
        """
        for ladrillo in self.ladrillos2:
            if self.rect.colliderect(ladrillo):
                self.puntos += 3
                self.veloci[1] = -self.veloci[1]
                self.ladrillos2.remove(ladrillo)
                self.sonido1.play()

    def colicion3(self, barra):
        """Eliminacion del ladrillo nivel 3.

           Este metodo borra el ladrillo de la
           matriz (se destruye) en el momento
           en que la bola colisiona con este
           en el nivel 3
        """
        for ladrillo in self.ladrillos3:
            if self.rect.colliderect(ladrillo):
                self.puntos += 3
                self.veloci[1] = -self.veloci[1]
                self.ladrillos3.remove(ladrillo)
                self.sonido1.play()                     
    
                            
    def puntaje(self, vent):
        """Puntos en pantalla.

           Este metodo muestra en la ventana
           los puntos ganados al momento
           de destruir los ladrillos con 
           la bola
        """
        if self.font:
            font_surface = self.font.render("PUNTOS: " + str(self.puntos) , False, blanco)
            vent.blit(font_surface, (205,5))                  


class Barra(pygame.sprite.Sprite):
    """Clase que representa la barra del nivel 1 (plataforma grande)"""
    def __init__(self):
       """
          Inicializador de la clase 'Barra'.
          :param barra: Imagen barra nivel 1
          :param rect: Obtiene el rectangulo de la imagen de la barra del nivel 1
          :param rect.centerx: Posicion inicial de la barra en x
          :param rect.centery: Posicion inicial de la barra en y
          :param veloc: Velocidad de la barra
          :param injuego: Variable booleana
        """ 
       pygame.sprite.Sprite.__init__(self)
       self.barra = pygame.image.load("imagenes/barra.png")
       self.rect = self.barra.get_rect()
       self.rect.centerx = ancho/2
       self.rect.centery = alto-15
       self.veloc = 5
       self.injuego = True
       
       
    def agregar(self, superficie):
        """Muestra barra.

           Metodo de la clase Barra, dibuja la
           barra del nivel 1 en la ventana 
           llamada "superficie"
        """
        superficie.blit(self.barra, self.rect) 
    
    def movimiento(self):
        """Movimiento de la barra.
          
           Este metodo de la clase Barra
           limita el movimiento de la barra en
           los margenes izquierdo y derecho de
           la pantalla perteneciente al nivel 1
        """
        if self.injuego == True:
            if self.rect.left <= 0:
                self.rect.left = 0
            elif self.rect.right > 900:
                self.rect.right = 900                       


class Barra2(pygame.sprite.Sprite):
    """Clase que representa la barra del nivel 2 (plataforma mediana)"""
    def __init__(self):
       """
          Inicializador de la clase 'Barra2'.
          :param barra: Imagen barra nivel 2
          :param rect: Obtiene el rectangulo de la imagen de la barra del nivel 2
          :param rect.centerx: Posicion inicial de la barra en x
          :param rect.centery: Posicion inicial de la barra en y
          :param veloc: Velocidad de la barra
          :param injuego: Variable booleana 
        """
       pygame.sprite.Sprite.__init__(self)
       self.barra = pygame.image.load("imagenes/barra2.png")
       self.rect = self.barra.get_rect()
       self.rect.centerx = ancho/2
       self.rect.centery = alto-15
       self.veloc = 10
       self.injuego = True
       
       
    def agregar(self, superficie):
        """Muestra barra.

           Metodo de la clase Barra2, dibuja la
           barra del nivel 2 en la ventana 
           llamada "superficie"
        """
        superficie.blit(self.barra, self.rect) 
    
    def movimiento(self):
        """Movimiento de la barra.
          
           Este metodo de la clase Barra2
           limita el movimiento de la barra en
           los margenes izquierdo y derecho de
           la pantalla perteneciente al nivel 2
        """
        if self.injuego == True:
            if self.rect.left <= 0:
                self.rect.left = 0
            elif self.rect.right > 900:
                self.rect.right = 900 

class Barra3(pygame.sprite.Sprite):
    """Clase que representa la barra del nivel 3 (plataforma pequenia)"""
    def __init__(self):
       """
          Inicializador de la clase 'Barra3'.
          :param barra: Imagen barra nivel 3
          :param rect: Obtiene el rectangulo de la imagen de la barra del nivel 3
          :param rect.centerx: Posicion inicial de la barra en x
          :param rect.centery: Posicion inicial de la barra en y
          :param veloc: Velocidad de la barra
          :param injuego: Variable booleana
        """
       pygame.sprite.Sprite.__init__(self)
       self.barra = pygame.image.load("imagenes/barra3.png")
       self.rect = self.barra.get_rect()
       self.rect.centerx = ancho/2
       self.rect.centery = alto-15
       self.veloc = 15
       self.injuego = True
       
       
    def agregar(self, superficie):
        """Muestra barra.

           Metodo de la clase Barra3, dibuja la
           barra del nivel 3 en la ventana 
           llamada "superficie"
        """
        superficie.blit(self.barra, self.rect) 
    
    def movimiento(self):
        """Movimiento de la barra.
          
           Este metodo de la clase Barra3
           limita el movimiento de la barra en
           los margenes izquierdo y derecho de
           la pantalla perteneciente al nivel 3
        """
        if self.injuego == True:
            if self.rect.left <= 0:
                self.rect.left = 0
            elif self.rect.right > 900:
                self.rect.right = 900     


def NIVEL1():
    """Ejecucion nivel 1.

       En esta funcion se da inicio al
       nivel 1, se instancian los objetos
       de las clases creadas
    """
    pygame.init()
    vent = pygame.display.set_mode((ancho,alto))
    pygame.display.set_caption("Arkanoid")
    imagenfondo=pygame.image.load("imagenes/fondobosque2.jpg").convert_alpha()
    pygame.mixer.music.load('sonidos/04. punch-out - boxing.mp3') 
    pygame.mixer.music.play(3)
    fuente1 = pygame.font.Font(None,15)
    text4=fuente1.render("Nivel 1",0,blanco)

    enjuego= True
    jugador = Barra()
   
    eobola=Bola(ancho/3,alto-30)
   
    while True:
      jugador.movimiento()
      eobola.mover(jugador)
      vent.blit(imagenfondo,(0,0))
     
      for evento in pygame.event.get():
        if evento.type == QUIT:
           pygame.quit()
           sys.exit()
       
      eobola.colicion(Barra) 
      eobola.puntaje(vent)
      pressed = pygame.key.get_pressed()
      if pressed[pygame.K_LEFT]:
          jugador.rect.left -= jugador.veloc
      if pressed[pygame.K_RIGHT]: 
          jugador.rect.right+= jugador.veloc
     
      
      eobola.dibujarL(vent)
      eobola.agregar2(vent)
      jugador.agregar(vent)
      vent.blit(text4,(0,10)) 
      pygame.display.flip()
      pygame.display.update()
 

def NIVEL2():
    """Ejecucion nivel 2.

       En esta funcion se da inicio al
       nivel 2, se instancian los objetos
       de las clases creadas
    """
    pygame.init()
    vent = pygame.display.set_mode((ancho,alto))
    pygame.display.set_caption("Arkanoid")
    imagenfondo = pygame.image.load("imagenes/nivel2n.jpg").convert_alpha()
    pygame.mixer.music.load('sonidos/CommonFight.ogg') 
    pygame.mixer.music.play(3)
    fuente1 = pygame.font.Font(None,15)
    text4 = fuente1.render("Nivel 2",0,blanco)
    enjuego = True
    jugador = Barra2()
   
   
    eobola = Bola(ancho/3,alto-30)
    while True:
        jugador.movimiento()
        eobola.mover(jugador)
        vent.blit(imagenfondo,(0,0))
     
        for evento in pygame.event.get():
          if evento.type == QUIT:
            pygame.quit()
            sys.exit()
         
        eobola.colicion2(Barra2) 
        eobola.puntaje(vent)
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
          jugador.rect.left -= jugador.veloc
        if pressed[pygame.K_RIGHT]: 
          jugador.rect.right+= jugador.veloc
     
      
        vent.blit(text4,(0,10))
        eobola.dibujarL2(vent)
        eobola.agregar2(vent)
        jugador.agregar(vent) 
        pygame.display.flip()
        pygame.display.update()
 

def NIVEL3():
    pygame.init()
    """Ejecucion nivel 3.

       En esta funcion se da inicio al
       nivel 3, se instancian los objetos
       de las clases creadas
    """
    vent = pygame.display.set_mode((ancho,alto))
    pygame.display.set_caption("Arkanoid")
    imagenfondo = pygame.image.load("imagenes/nivel3.jpg").convert_alpha()
    pygame.mixer.music.load('sonidos/BossFight.ogg') 
    pygame.mixer.music.play(3)
    fuente1 = pygame.font.Font(None,15)
    text4 = fuente1.render("Nivel 3",0,blanco)

    enjuego = True
    jugador = Barra3()
   
   
    eobola = Bola(ancho/3,alto-30)
    while True:
       jugador.movimiento()
       eobola.mover(jugador)
       vent.blit(imagenfondo,(0,0))
     
       for evento in pygame.event.get():
         if evento.type == QUIT:
           pygame.quit()
           sys.exit()
        
       eobola.colicion3(Barra3) 
       eobola.puntaje(vent)
       pressed = pygame.key.get_pressed()
       if pressed[pygame.K_LEFT]:
          jugador.rect.left -= jugador.veloc
       if pressed[pygame.K_RIGHT]: 
          jugador.rect.right+= jugador.veloc
     
       vent.blit(text4,(0,10))
       eobola.dibujarL3(vent)
       eobola.agregar2(vent)
       jugador.agregar(vent) 
       pygame.display.flip()
       pygame.display.update()

def Introduccion():
    """Menu de inicio.
 
       En esta funcion se crea el menu
       del juego con su respectiva
       tipologia de texto
    """
    pygame.init()
    vent = pygame.display.set_mode((ancho,alto))
    imagenin=pygame.image.load("imagenes/introd.jpg").convert_alpha()
    pygame.display.set_caption("Arkanoid")
    fuente1 = pygame.font.Font(None,50)
    texto1=fuente1.render("Bienvenido!!",0,(0,0,238))
    texto2=fuente1.render("Presione S para jugar",0,(0,0,238))
    texto3=fuente1.render("Presione P para salir",0,(0,0,238))
    introjuego = True
     
    while True:
        vent.blit(imagenin,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                introjuego = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                     NIVEL1()
                if event.key == pygame.K_p:
                    introjuego = False
                    quit()
         
         
        vent.blit(texto1,(150,200))
        vent.blit(texto2,(200,300))
        vent.blit(texto3,(200,350))
        pygame.display.flip()
        pygame.display.update()                

Introduccion() 
"""Se ejecuta el menu de inicio del juego"""