import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from plotagem.logs import PASTA_LOGS, vbox

def plot(
    filename, ylabel, datetime="date_time", title=None, separator=';', 
    decimal_separator=",", dayfirst=False, multiply=1, division=1,
    includeColYlabel=False, cols_to_divide=[], cols_to_multiply=[]
):
    try:
        df = pd.read_csv(filename, sep=separator, decimal=decimal_separator, dayfirst=dayfirst, parse_dates=[datetime]).rename(columns={datetime: 'seconds'})
    
    except ValueError:
        try:
            df = pd.read_csv(filename, sep=separator, decimal=decimal_separator, dayfirst=dayfirst, parse_dates=['time']).rename(columns={'time': 'seconds'})        

        except Exception as e:
            print("Erro ao ler o arquivo CSV:", e)
            return None
        
    print(f'\n\nfilename: {filename}\n\n')
    
    df['seconds'] = pd.to_datetime(df['seconds'], format="%m-%d-%Y-%H:%M:%S", errors='coerce')
    df.dropna(inplace=True)
    
    df['seconds'] = (df['seconds'] - df['seconds'][0]).dt.total_seconds() / 3600
    df = df.set_index('seconds').replace(',', '.', regex=True).apply(lambda x: pd.to_numeric(x, errors='ignore'))        
    
    if filename == "{PASTA_LOGS}/{vbox['server_response_time_monitoring']}":
        df['response_time'] = df['response_time'] / 1000    
    
    
    # perform data division
    cols_to_divide = cols_to_divide if len(cols_to_divide) != 0 else df.columns
    df[cols_to_divide] = df[cols_to_divide].div(division)
        
    for col in df.columns:            
        col_mix = col + " " + ylabel if type(ylabel) is str and includeColYlabel else ylabel

        df[col] = df[col].fillna(0)

        x = df.index.to_numpy().reshape((-1, 1))
        y = df[col].to_numpy().reshape((-1, 1))

        model = LinearRegression()
        model.fit(x, y)

        Y_pred = model.predict(x)

        ax = df.plot(
            y=col,
            legend=0,
            xlabel='Time(h)',
            ylabel=col_mix if type(ylabel) is str else ylabel[col] if type(ylabel) is dict and col in ylabel else col,
            title=title if type(title) is str else title[col] if type(title) is dict and col in title else col,
            figsize=(10,5),
            style='k',
        )
        
        ax.plot(x, Y_pred, color='red')
        
        # intervalos
        interval_1_duration = 12  # 12 horas
        interval_2_duration = 72   # 3 dias (72 horas)

        # máximo de tempo (x) dos dados
        max_time = df.index.max()

        # linha vertical no início de cada intervalo
        current_time = 0
        while current_time <= max_time:
            # linha azul no início do ciclo de 12 horas
            ax.axvline(x=current_time, color='blue', linestyle='--', label='start waiting phase' if current_time == 0 else None)
            
            # linha verde no início do ciclo de 3 dias
            ax.axvline(x=current_time + interval_1_duration, color='green', linestyle='--', label='start stress phase' if current_time == 0 else None)

            # atualizando tempo atual para o próximo ciclo de 3 dias
            current_time += interval_1_duration + interval_2_duration  # Move para o próximo início de 12h + 3 dias

        # Remover duplicatas de legenda
        handles, labels = ax.get_legend_handles_labels()
        by_label = dict(zip(labels, handles))
        ax.legend(by_label.values(), by_label.keys())
            
        plt.show()
        
        fig = ax.get_figure()
        fig.savefig(f'./plotagem/plot_images/{title}-{col}.png')