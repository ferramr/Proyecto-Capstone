# *************************************
#
# Clase: --> Graficador 
# Modulo: -> graficador.py
# Ubicacion -> v.graficador
#
# Descripción:
#   Grafica posicion, velocidad y aceleracion
#
# Fecha:
#   enero 18/2022
#
# ************************************

import numpy as np
import matplotlib.pyplot as plt
import imutils
import cv2

class Graficador:

    # -------------------------------------------------------
    #           CONSTRUCTOR
    # -------------------------------------------------------
    def __init__(self):
        print("----------------------------")
        print(" CONSTRUCTOR: Graficador")
        print("----------------------------")

    def graficar_curvas_resultantes1(self,frame,t,d,modelos):
       
        # --------------------------------------------------
        # --- Modelos matemáticos en formato de polinomios
        # --------------------------------------------------
        model_d, model_v, model_a = modelos
        # --- model_d:
        #       -> Distancia(t) = ax^2 +bx + c
        # --- modelo_v:
        #       -> Velocidad(t) = d(Distancia)/dt = 2ax +b <- 1era. DERIVADA
        # --- model_a:
        #       -> Aceleracion(t) = d2(Distancia)/dt = 2a <- 2nda. DERIVADA
    
        # -----------------------------------------------------
        #   3 Graficas en una sola ventana:
        #       desplazamiento  -> verde    (subplot(2,2,1))
        #       velocidad       -> azul     (subplot(2,2,2))
        #       aceleracion     -> magenta  (subplot(2,2,3))
        # -----------------------------------------------------
        plt.clf()
        plt.figure(0)
        
        plt.subplot(2, 2, 1)
        plt.plot(t,model_d(t)/100, 'r-')
        #plt.xlabel("tiempo")
        plt.ylabel("distancia [m]")
        plt.grid()

        plt.subplot(2, 2, 2)
        plt.plot(t,model_v(t)/100, 'b-')
        #plt.xlabel("tiempo")
        plt.ylabel("velocidad [m/s]")
        plt.grid()

        plt.subplot(2, 2, 3)
        plt.plot(t,model_a(t)/100, 'm-')
        plt.xlabel("tiempo")
        plt.ylabel("aceleracion [m/s^2]")
        plt.grid()

        plt.subplot(2, 2, 4)
        plt.plot(t, d, 'bo')
        plt.xlabel("tiempo")
        plt.ylabel("muestras")
        plt.grid()

        plt.savefig("grafica_0.jpg")

        # --- Imagen para superposicion y transparencia ---
        overlay = frame.copy()   
        # --------------------------------------------------------------
        #    overlay --> Imagen superpuesta a mostrar en tamaño DISPLAY 
        # --------------------------------------------------------------
        grafica = imutils.resize(cv2.imread("grafica_0.jpg"),400)
        h, w = grafica.shape[:2]    # 300 x 400
        hf, wf = frame.shape[:2]    # 637 x 850
        #print(" frame hf = ",hf," |wf = ",wf)

        grafica = imutils.resize(grafica, width=600)
        h, w = grafica.shape[:2]

        pip_h = 40 #25
        pip_w = 20 
            
        overlay[pip_h:pip_h+h,pip_w:pip_w+w] = grafica

        # --- Overlay de dos imagenes ---
        alpha = 0.6 # 0.6 el mejor # 0.8
        cv2.addWeighted(overlay,alpha,frame,1-alpha,0,frame)

    def graficar_curvas_resultantes2(self,frame,t_original,d,modelos):

        # --------------------------------------------------
        # Graficas realizadas para mostrarse en NODE-RED con
        # un tiempo fijo en el eje "x" de 1.2 segundos y una
        # amplitud máxima de :
        # desplazamiento:   0.4 m
        # velocidad :       1.6 m/s
        # aceleracion:      4.4 m/s^2
        # --------------------------------------------------

        # --------------------------------------------------
        # --- Modelos matemáticos en formato de polinomios
        # --------------------------------------------------
        model_d, model_v, model_a = modelos
        # --- model_d:
        #       -> Distancia(t) = ax^2 +bx + c
        # --- modelo_v:
        #       -> Velocidad(t) = d(Distancia)/dt = 2ax +b <- 1era. DERIVADA
        # --- model_a:
        #       -> Aceleracion(t) = d2(Distancia)/dt = 2a <- 2nda. DERIVADA
  
        # -----------------------------------------------------
        #   3 Graficas en una sola ventana:
        #       desplazamiento  -> verde    (subplot(2,2,1))
        #       velocidad       -> azul     (subplot(2,2,2))
        #       aceleracion     -> magenta  (subplot(2,2,3))
        # -----------------------------------------------------
        plt.clf()
        plt.figure(0)

        # -----------------------------------------------------
        # Preparación de la graficas para formato de NODE-RED
        # -----------------------------------------------------
        
        # - Grafica de DESPLAZAMIENTO: t < 1.2s; d(t) < 0.4 m
        t = []
        for i in range(0,120,2):
            if model_d(i/100) <= 40:
                t.append(i/100)
        
        plt.subplot(2, 2, 1)
        plt.plot(t,model_d(t)/100, 'r-')
        #plt.xlabel("tiempo")
        plt.ylabel("distancia [m]")
        plt.grid()

        # - Grafica de VELOCIDAD: t < 1.2s; v(t) < 1.6 m/s
        t = []
        for i in range(0,120,2):
            if model_v(i/100) <= 160:
                t.append(i/100)

        plt.subplot(2, 2, 2)
        plt.plot(t,model_v(t)/100, 'b-')
        #plt.xlabel("tiempo")
        plt.ylabel("velocidad [m/s]")
        plt.grid()

        # - Grafica de ACELERACION: t < 1.2s; v(t) < 4.4 m/s^2
        t = []
        for i in range(0,120,2):
            if model_a(i/100) <= 440:
                t.append(i/100)

        plt.subplot(2, 2, 3)
        plt.plot(t,model_a(t)/100, 'm-')
        plt.xlabel("tiempo")
        plt.ylabel("aceleracion [m/s^2]")
        plt.grid()

        plt.subplot(2, 2, 4)
        plt.plot(t_original, d, 'bo')
        plt.xlabel("tiempo")
        plt.ylabel("muestras")
        plt.grid()

        plt.savefig("grafica_0.jpg")

        # --- Imagen para superposicion y transparencia ---
        overlay = frame.copy()   
        # --------------------------------------------------------------
        #    overlay --> Imagen superpuesta a mostrar en tamaño DISPLAY 
        # --------------------------------------------------------------
        grafica = imutils.resize(cv2.imread("grafica_0.jpg"),400)
        h, w = grafica.shape[:2]    # 300 x 400
        hf, wf = frame.shape[:2]    # 637 x 850
        #print(" frame hf = ",hf," |wf = ",wf)

        grafica = imutils.resize(grafica, width=600)
        h, w = grafica.shape[:2]

        pip_h = 40 #25
        pip_w = 20 
            
        overlay[pip_h:pip_h+h,pip_w:pip_w+w] = grafica

        # --- Overlay de dos imagenes ---
        alpha = 0.6 # 0.6 el mejor # 0.8
        cv2.addWeighted(overlay,alpha,frame,1-alpha,0,frame)
            
