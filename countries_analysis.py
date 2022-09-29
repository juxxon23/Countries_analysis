import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import ttk

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


def main():
    interface_activate()
    

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
    

def comparative_graph(fd1, fd2, key_column1, key_column2, label1, label2):
    plt.figure()
    plt.plot(fd1[key_column1][::-1],fd1[key_column2][::-1], label=label1)
    plt.plot(fd2[key_column1][::-1],fd2[key_column2][::-1], label=label2)
    plt.xlabel(key_column1)
    plt.ylabel(key_column2)
    plt.grid(ls="dashed")
    plt.legend()
    plt.show()


def regression_graph(x, xp, predict, key_column1, key_column2):
    plt.figure()
    plt.plot(x[key_column1][::-1],x[key_column2][::-1], "o")
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


def interface_activate():
    w = tk.Tk()
    w.title('Country Analysis')
    w.geometry("395x355")

    data_columns = ["Country","Year","Status","Life expectancy",
    "Adult Mortality","infant deaths","Alcohol","percentage expenditure",
    "Hepatitis B","Measles","BMI","under-five deaths","Polio",
    "Total expenditure","Diphtheria","HIV/AIDS","GDP","Population",
    "thinness 1-19 years","thinness 5-9 years",
    "Income composition of resources","Schooling"]

    e = tk.Label(w, text="COUNTRY ANALYSIS")
    t1 = tk.Entry(w, font="Helvetica 25", width=10)
    t2 = tk.Entry(w, font="Helvetica 25", width=10)
    t3 = ttk.Combobox(w, values=(data_columns), width=20)
    t4 = ttk.Combobox(w, values=(data_columns), width=20)
    b1 = tk.Button(w, text="Comparison chart", padx=38, pady=50, command=lambda:comparative_graph(get_data_by("Country", t1.get(), ["Country", t3.get(), t4.get()]), get_data_by("Country", t2.get(), ["Country", t3.get(), t4.get()]), t3.get(), t4.get(), t1.get(), t2.get()), width=16)
    b2 = tk.Button(w, text="Relate variables", padx=38, pady=50, command=lambda:lin_regr(get_data_by("Country", t1.get(), ["Country", t3.get(), t4.get()]), t3.get(), t4.get()), width=16)

    e.grid(row=0, column=0)
    t1.grid(row=1, column=0)
    t2.grid(row=2, column=0)
    t3.grid(row=1, column=1)
    t4.grid(row=2, column=1)
    b1.grid(row=3, column=0)
    b2.grid(row=4, column=0)

    t3.current(1)
    t4.current(3)
    w.mainloop()


if __name__ == "__main__":
    main()