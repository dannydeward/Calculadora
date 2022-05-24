from PySide6.QtWidgets  import (QApplication,QWidget,QGridLayout,QLCDNumber,QPushButton)
from functools import partial
from helpers import *

#vamos a  trabajar  con POO para  darle  funcionabilidad  a  la  calculadora

class calculadora(QLCDNumber):
     def __init__(self): 
        super().__init__(digitCount=12, segmentStyle=QLCDNumber.Flat)
        self.texto=""
        self.reiniciar=False
        
     def escribir(self,caracter):
         if self.reiniciar:
             self.limpiar()
         if caracter =='.' and self.texto.count('.')==1: # con esto evitamos que el1  se  escriba  mas  de una  vez 
             return 
         if len(self.texto)<=12:
            self.texto+=caracter
            self.display(self.texto)
            
     def preparar(self,operacion):
         self.operacion=operacion
         self.memoria=float(self.texto)
         self.limpiar()
         print(self.operacion, self.memoria)
         
     def calcular(self):
         
         resultado=0.0
         
         if self.operacion =='+':
             resultado=self.memoria + float(self.texto)
         elif self.operacion=='-':
             resultado=self.memoria - float(self.texto)
         elif self.operacion=='*':
             resultado=self.memoria * float(self.texto)
         elif self.operacion=='/':
             resultado=self.memoria / float(self.texto)
             
         self.texto= str(round(resultado,2))
             
         if len(self.texto)>12:
             self.texto= "Error"         
         self.display(self.texto)
         self.reiniciar=True
             
         
     def limpiar(self):
         self.texto=""
         self.display(self.texto)
         self.reiniciar=False

class Window (QWidget):
    def __init__(self): 
        super().__init__()
        self.setFixedWidth(500)
        self.setFixedHeight(360)
        self.setWindowTitle('Calculadora')
        with open(absPath("Scalcula.qss"))  as  styles :
            self.setStyleSheet(styles.read())
        self.setLayout(QGridLayout())
        self.calculadora= calculadora()
        self.layout().addWidget(self.calculadora, 0,0,1,0 )#colocamos un span  con 1 para  que ocupe 1  fila  todo  el espacio
        
        
        simbolos= [
                       
            ['7','8','9','/'],
            ['4','5','6','*'],
            ['1','2','3','-'],
            ['.','0','=','+'],
                  
              ] #esta  es  la estructura  de computadora
        
        for i, fila in enumerate(simbolos):
            for j, simbolo in  enumerate(fila):
                boton= QPushButton(simbolo)
                boton.setStyleSheet('height:50px;font-size: 25px;')
                boton.clicked.connect(partial(self.boton_clicado, simbolo)) #se usa  el metodo partial para  ayudar  a  escribir en la panatalla. se da mejor  que lambda
                self.layout().addWidget(boton, i+1,j) #se suma1  en i para  saltar una  fila 
                
    def boton_clicado(self, simbolo):
        if simbolo.isdigit() or simbolo =='.': #se aplica  esta condicional, para que en pantalla  solo se  escriban  numeros 
            self.calculadora.escribir(simbolo)
        elif simbolo=='=':
            self.calculadora.calcular()
        else:
            self.calculadora.preparar(simbolo)
        
        
        
if __name__ == '__main__':
    app = QApplication()
    window = Window()
    window.show()
    app.exec_()

                   