import pandas as pd
from plotagem.logs import PASTA_LOGS, NAME_FORMAT

class FragmentationAnalysis:
    def __init__(self, log_file, minimum_process_occurrences=1):
        self.log_file = log_file
        self.minimum_process_occurrences = minimum_process_occurrences
        self.df = self.load_data()

    def load_data(self):
        """Load and clean the CSV file."""
        try:
            df = pd.read_csv(self.log_file, delimiter=';')  # Read the CSV file into a DataFrame
            df = df.dropna()  # Drop rows with NaN values
        except Exception as e:
            print(f"Erro ao ler o arquivo CSV: {e}")
            return None
        return df

    def preprocess_data(self):
        """Preprocess the DataFrame by converting the datetime and calculating time passed."""
        self.df['datetime'] = pd.to_datetime(self.df['datetime'])  # Convert the datetime column
        self.df = self.df.set_index('datetime')  # Set the datetime as index
        self.df['time_passed'] = (self.df.index - self.df.index[0]).total_seconds() / 3600  # Calculate time passed in hours
        self.df = self.df.set_index('time_passed')  # Reset index to 'time_passed'

    def filter_data(self):
        """Filter the DataFrame based on minimum process occurrences."""
        self.df_filtered = self.df[self.df['process_occurrences'] >= self.minimum_process_occurrences]  # Apply filter

    def pivot_data(self):
        """Pivot the DataFrame for analysis."""
        self.df_pivot = self.df_filtered.pivot(columns='process', values='process_occurrences')  # Pivot based on process

    def plot(self):
        """Plot the data and save the figure."""
        ax = self.df_pivot.plot(ylabel='Process occurrences (qtt)', xlabel='Time(H)')
        ax.set_yticks(ax.get_yticks())
        ax.set_yticklabels(ax.get_yticks().astype(int))
        
        # Save the figure
        fig = ax.get_figure()
        fig.savefig(f'./plotagem/plot_images/{NAME_FORMAT}.png')

    def run_analysis(self):
        """Execute the complete analysis workflow."""
        self.preprocess_data()
        self.filter_data()
        self.pivot_data()
        self.plot()


if __name__ == '__main__':
    pasta_logs = f'{PASTA_LOGS}/fragmentation.csv'
    
    analysis = FragmentationAnalysis(log_file=pasta_logs, minimum_process_occurrences=1)
    analysis.run_analysis()
