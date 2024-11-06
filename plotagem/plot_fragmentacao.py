import pandas as pd
from plotagem.logs import PASTA_LOGS, NAME_FORMAT
pasta_logs = f'{PASTA_LOGS}/fragmentation.csv'
    
def analise(df, minimum_process_occurrences):
    # Convert the datetime column to a datetime object
    df['datetime'] = pd.to_datetime(df['datetime'])

    # Set the index to the datetime column
    df = df.set_index('datetime')
    
    df['time_passed'] = (df.index - df.index[0]).total_seconds() / 3600

    # Resetting the index to use 'time_passed' as index
    df = df.set_index('time_passed')

    df_filtered = df[df['process_occurrences'] >= minimum_process_occurrences]
        
    df_pivot = df_filtered.pivot(columns='process', values='process_occurrences')
    
    ax = df_pivot.plot(ylabel='Process occurrences (qtt)', xlabel='Time(H)', figsize=(10, 5))
    ax.set_yticks(ax.get_yticks())
    ax.set_yticklabels(ax.get_yticks().astype(int))
    
    # Save the figure
    fig = ax.get_figure()
    fig.savefig(f'./plotagem/plot_images/{NAME_FORMAT}.png')
    

def fragmentacao(minimum_process_occurrences=1):        
    df = pd.read_csv(pasta_logs, delimiter=';')     # Read the CSV file into a DataFrame
    
    df = df.dropna()        # drop nan column values and emptieds array
        
    analise(df, minimum_process_occurrences)