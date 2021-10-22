import pandas as pd
import os


def tarefa_01(path):
    df = pd.read_csv(path)
    return df


if __name__ == '__main__':
    print(tarefa_01('menes.csv'))
