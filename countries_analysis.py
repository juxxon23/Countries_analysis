import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tkinter

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


def main():
    fd1 = get_data_by("Country", "Colombia", ["Country", "Year", "Life expectancy"])
    fd2 = get_data_by("Country", "China", ["Country", "Year", "Life expectancy"])
    interface_activate(fd1, fd2)
    #comparative_graph(fd1, fd2, "Year", "Life expectancy")
    #lin_regr(fd1, "Year", "Life expectancy")
    

def get_data_by(key_column, value_column, list_columns):
    # Esta funcion solo funciona para verificar si un elemento es igual a otro, no trabaja con intervalos. (Pendiente)
    data_file = pd.read_csv("Life_Expectancy_Data.csv")
    filter_data = data_file.loc[data_file[key_column]==value_column, list_columns]
    return filter_data


def lin_regr(x, key_column1, key_column2):
    xp = x[key_column1].to_numpy().reshape(-1, 1)[::-1]
    yp = x[key_column2].to_numpy()[::-1]
    regr = LinearRegression()
    regr.fit(xp, yp)
    r2 = regr.score(xp, yp)
    predict = regr.predict(xp)
    print("La recta es ", regr.coef_[0], "x + ", regr.intercept_, "\nR2 = ", r2)
    return regression_graph(x, xp, predict, key_column1, key_column2)
    

def comparative_graph(fd1, fd2, key_column1, key_column2):
    plt.figure()
    plt.plot(fd1[key_column1][::-1],fd1[key_column2][::-1], label="Colombia")
    plt.plot(fd2[key_column1][::-1],fd2[key_column2][::-1], label="China")
    plt.xlabel(key_column1)
    plt.ylabel(key_column2)
    plt.grid(ls="dashed")
    plt.legend()
    plt.show()


def regression_graph(x, xp, predict, key_column1, key_column2):
    plt.figure()
    plt.plot(x[key_column1][::-1],x[key_column2][::-1], "o", label="LS de Colombia")
    plt.plot(xp, predict, label="Reg lineal")
    plt.xlabel(key_column1)
    plt.ylabel(key_column2)
    plt.grid(ls="dashed")
    plt.legend()
    plt.show()


"""
# Los datos del polinomio son muy grandes en comparacion con la informacion de muestra.
def poly_adjust(fd1, key_column1, key_column2):
    x = fd1[key_column1].to_numpy().reshape(-1, 1)[::-1]
    y = fd1[key_column2].to_numpy()[::-1]
    
    k = 2
    pf = PolynomialFeatures(degree=k)
    xp = pf.fit_transform(x)

    regr = LinearRegression()
    regr.fit(xp, y)

    print('w = ' + str(regr.coef_) + ', b = ' + str(regr.intercept_))

    coe=regr.coef_.tolist()
    coe=coe[::-1]

    poly=np.poly1d(coe)

    plt.plot(fd1[key_column1][::-1],fd1[key_column2][::-1], "o", label="LS de Colombia")
    plt.plot(x, poly(x), 'b-',  label="Ajuste polinomial grado: "+str(k))
    plt.grid(ls="dashed")
    plt.legend()
    plt.show()
"""


def interface_activate(fd1, fd2):
    w = tkinter.Tk()
    w.geometry("500x500")
    
    """
    e = tkinter.Label(w, text="Hello World!", bg="blue")
    e.pack() # side=tkinter.RIGHT, fill=tkinter.X, fill=tkinter.Y, expand=true, fill=tkinter.BOTH
    
    b1 = tkinter.Button(w, text="Comparison chart", padx=40, pady=50, command=lambda:comparative_graph(fd1, fd2, "Year", "Life expectancy"))
    b1.pack()
    
    b2 = tkinter.Button(w, text="Relate variables", padx=40, pady=50, command=lambda:lin_regr(fd1, "Year", "Life expectancy"))
    b2.pack()

    t = tkinter.Entry(w, font="Helvetica 25")
    t.pack()

    def show_text():
        t_d = t.get()
        print(t_d)
        e["text"] = t_d    
    
    b3 = tkinter.Button(w, text="Show text", padx=40, pady=50, command=show_text)
    b3.pack()
    """
    # Con GRID
    # Organizar los tamanos
    e = tkinter.Label(w, text="COUNTRY ANALYSIS") # bg="blue"
    t1 = tkinter.Entry(w, font="Helvetica 25")
    t2 = tkinter.Entry(w, font="Helvetica 25")
    t3 = tkinter.Entry(w, font="Helvetica 25")
    t4 = tkinter.Entry(w, font="Helvetica 25")
    b1 = tkinter.Button(w, text="Comparison chart", padx=40, pady=50, command=lambda:comparative_graph(fd1, fd2, "Year", "Life expectancy"))
    b2 = tkinter.Button(w, text="Relate variables", padx=40, pady=50, command=lambda:lin_regr(fd1, "Year", "Life expectancy"))
   
    e.grid(row=0, column=0)
    t1.grid(row=1, column=0)
    t2.grid(row=2, column=0)
    t3.grid(row=1, column=1)
    t4.grid(row=2, column=1)
    b1.grid(row=3, column=0)
    b2.grid(row=4, column=0)

    # ----------------------------
    # Ejemplo GRID

    #boton1 = tkinter.Button(w, text="Butututuno 1", width=10, height=5)
    #boton2 = tkinter.Button(w, text="Butututuno 2", width=10, height=5)
    #boton3 = tkinter.Button(w, text="Butututuno 3", width=10, height=5)

    #boton1.grid(row=0, column=0)
    #boton2.grid(row=1, column=0)
    #boton3.grid(row=2, column=0)

    w.mainloop()


if __name__ == "__main__":
    main()