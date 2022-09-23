import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression
# TO_DO:
#   * Funcion y grafica para Regresion no lineal
#   * Interfaz tkinter

def main():
    fd1 = get_data_by("Country", "Colombia", ["Country", "Year", "Life expectancy"])
    fd2 = get_data_by("Country", "China", ["Country", "Year", "Life expectancy"])
    comparative_graph(fd1, fd2, "Year", "Life expectancy")
    lin_regr(fd1, "Year", "Life expectancy")
    

def get_data_by(key_column, value_column, list_columns):
    # Esta funcion solo funciona para verificar si un elemento es igual a otro, no trabaja con intervalos. (Pendiente)
    data_file = pd.read_csv("Life_Expectancy_Data.csv")
    filter_data = data_file.loc[data_file[key_column]==value_column, list_columns]
    return filter_data


def lin_regr(x, key_column1, key_column2):
    xp=x[key_column1].to_numpy().reshape(-1, 1)[::-1]
    yp=x[key_column2].to_numpy()[::-1]
    regr = LinearRegression()
    regr.fit(xp, yp)
    r2 = regr.score(xp, yp)
    predict = regr.predict(xp)
    print("La recta es ", regr.coef_[0], "x + ", regr.intercept_, "\nR2 = ", r2)
    return regression_graph(x, xp, predict, key_column1, key_column2)
    

def comparative_graph(fd1, fd2, key_column1, key_column2 ):
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


if __name__ == "__main__":
    main()