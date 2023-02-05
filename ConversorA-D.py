import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import Tk,Text,ttk

def strtoint():
    def tren_impulso(t):
        return (t % 1 == 0) * 1

    def binary(lon, num):
        i, binario = 0, 0
        while num >= 1:
            binario += (num % 2) * (10 ** i)
            i += 1
            num //= 2
        return str(binario).zfill(lon)

    def decimal(num):
        dec, i = 0, 0
        while (num >= 1):
            d = num % 10
            num = num // 10
            dec += d * pow(2, i)
            i = i + 1
        return dec

    def meadthread(Vmin, Vmax, M, valM):
        L = int(2 ** M)
        intq = (Vmax - Vmin) / L
        valQ, valC = [], []
        x, y = [], []
        for i in range(-int(L / 2), 1 + int(L / 2)):
            x.append(intq * (i - 1 / 2))
            y.append(i * intq)
        for i in range(len(valM)):
            for j in range(1, len(x)):
                if x[j - 1] < valM[i] <= x[j]:
                    valQ.append(y[j - 1])
                    valC.append(binary(M, int(j + (y[j - 1] < 0) * (L / 2 - 1) - (y[j - 1] >= 0) * ((L + 1) / 2))))
        return valQ, valC, x, y

    def graphmead(Trama, L, intq):
        isbinary = True
        xtrama = np.linspace(0, 1, len(Trama))
        mx = []
        for i in Trama:
            i = int(i)
            if isbinary:
                i = decimal(i)
            mx.append(intq * i) if i < L / 2 else mx.append(-(L - i) * intq)
        ax[1, 0].stem(xtrama, mx)

    def x_sigma(t, Ts):
        return tren_impulso(t / Ts)

    def diganalogo(L, intq, signal_converter, valorinicial, valorfinal):
        xtrama = np.round(np.linspace(valorinicial, valorfinal + a_t, len(valC)), 2)
        dist = (xtrama[1] - xtrama[0])
        for i in range(1, len(newvalc) + 1):
            ax[1, 1].plot([xtrama[i - 1] - (i > 1) * (dist / 2), xtrama[i - 1] + dist / 2],
                          [newvalc[i - 1], newvalc[i - 1]], color="red")
            ax[1, 2].plot([xtrama[i - 1] - (i > 1) * (dist / 2), xtrama[i - 1] + dist / 2],
                          [newvalc[i - 1], newvalc[i - 1]], color="red")
            if i < len(valC):
                ax[1, 1].plot([xtrama[i - 1] + dist / 2, xtrama[i - 1] + dist / 2], [newvalc[i - 1], newvalc[i]],
                              color="red")
                ax[1, 2].plot([xtrama[i - 1] + dist / 2, xtrama[i - 1] + dist / 2], [newvalc[i - 1], newvalc[i]],
                              color="red")
        ax[1, 2].plot(t, xc(t), color="blue")
        if len(signal_muestreada) == len(newvalc):
            error_mean=np.mean(signal_muestreada - newvalc)
            Errormean.config(text=f"Error de cuantificación (promedio) = {error_mean}")

    def xc(t):
        return np.sin(t)
    print(Aproximacion.get())
    A_dec=int(Aproximacion.get())
    a_t = 10/(10**(A_dec+1))
    Ts = round(1/float(T_s.get()),A_dec)
    Valor_inicial, Valor_final = float(Valor_inicial1.get()), float(Valor_final1.get())
    Vmin, Vmax, r = float(V_min.get()), float(V_max.get()), int(M.get())
    t = np.round(np.arange(Valor_inicial, Valor_final + a_t, a_t), A_dec)
    fig, ax = plt.subplots(2, 3)
    ax[0, 0].set_title("Señal analógica")
    ax[0, 1].set_title("Señal muestreada")
    ax[0, 2].set_title("Cuantizador Mead Thread")
    ax[1, 1].set_title("Señal resultante")
    ax[1, 2].set_title("Comparación de señales")
    ax[0, 0].plot(t, xc(t))
    signal_muestreada = xc(t) * x_sigma(t, Ts)
    ax[0, 1].plot(t, signal_muestreada)
    signal_muestreada = xc(t)[np.where(x_sigma(t, Ts) == np.max(x_sigma(t, Ts)))]

    valM = signal_muestreada
    valQ, valC, x, y = meadthread(Vmin, Vmax, r, valM)
    for i in range(1, 2 ** r + 1):
        ax[0, 2].plot([x[i - 1], x[i]], [y[i - 1], y[i - 1]], color="blue")
        # plt.annotate(binary(r,int(i+(y[i-1]<0)*(int(2**r)/2-1)-(y[i-1]>=0)*((int(2**r)+1)/2))),(x[i-1],y[i-1]))
        if i != (2 ** r):
            ax[0, 2].plot([x[i], x[i]], [y[i - 1], y[i]], color="blue")
    for i in range(len(valM)):
        ax[0, 2].plot([valM[i], valM[i]], [min(y), max(y)], linestyle='dotted', color="red")
    ValoresQ.config(text=f"Q = {valQ}")
    ValoresC.config(text=f"C = {valC}")
    graphmead(valC, int(2 ** r), (Vmax - Vmin) / int(2 ** r))
    L = int(2 ** r)
    intq = (Vmax - Vmin) / L
    newvalc = np.array([decimal(int(i)) for i in valC])
    newvalc = ((newvalc >= L / 2) * (newvalc - L) + (newvalc < L / 2) * (newvalc)) * intq
    diganalogo(L, intq, newvalc, Valor_inicial, Valor_final)
    plt.show()

root=Tk()
root.title("Conversor Análogo - Digital")
##FRECUENCIA MUESTREO
frecuencia_muestreo=ttk.Label(text="Frecuencia de muestreo:")
frecuencia_muestreo.place(x=20,y=20)
T_s=ttk.Entry()
T_s.place(x=220,y=20)
(ttk.Label(text="decimales")).place(x=75,y=90)
Aproximacion=ttk.Combobox(width=5,values=["2","3","4"],state="readonly")
Aproximacion.place(x=20,y=90)
##VALOR INICIAL Y FINAL DE LA SEÑAL ANALÓGICA
valorinicial,valorfinal=ttk.Label(text="Valor inicial:"),ttk.Label(text="Valor final:")
valorinicial.place(x=20,y=50)
valorfinal.place(x=280,y=50)
Valor_inicial1,Valor_final1=ttk.Entry(),ttk.Entry()
Valor_inicial1.place(x=100,y=50),Valor_final1.place(x=360,y=50)
##VALORES CUANTIZADOR
(ttk.Label(text="Valores cuantizador:")).place(x=20,y=120)
(ttk.Label(text="- Valores mínimo:")).place(x=20,y=150)
(ttk.Label(text="- Valores máximo:")).place(x=160,y=150)
(ttk.Label(text="- Número de bits:")).place(x=20,y=200)
V_min,V_max,M=ttk.Entry(),ttk.Entry(),ttk.Entry()
V_min.place(x=30,y=170),V_max.place(x=170,y=170),M.place(x=30,y=220)
(ttk.Button(text="Conversión",command=strtoint)).place(x=20,y=280)
ValoresC=ttk.Label(text="C =")
ValoresC.place(x=20,y=320)
ValoresQ=ttk.Label(text="Q =")
ValoresQ.place(x=20,y=340)
Errormean=ttk.Label(text="Error de cuantificación (promedio) =")
Errormean.place(x=20,y=360)
root.mainloop()



