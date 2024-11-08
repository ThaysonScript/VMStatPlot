import sys
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

class DataPlotter:
    def __init__(self, filename, ylabel, datetime_col="date_time", title=None, 
                 separator=';', decimal_separator=",", dayfirst=False, 
                 multiply=1, division=1, decimals_quantity=2, include_col_ylabel=False, 
                 cols_to_divide=[], cols_to_multiply=[]):
        self.filename = filename
        self.ylabel = ylabel
        self.datetime_col = datetime_col
        self.title = title
        self.separator = separator
        self.decimal_separator = decimal_separator
        self.dayfirst = dayfirst
        self.multiply = multiply
        self.division = division
        self.decimals_quantity = decimals_quantity
        self.include_col_ylabel = include_col_ylabel
        self.cols_to_divide = cols_to_divide
        self.cols_to_multiply = cols_to_multiply

        self.data = self.load_data()

    def load_data(self):
        """Load CSV data and preprocess it."""
        try:
            df = pd.read_csv(self.filename, sep=self.separator, decimal=self.decimal_separator, 
                             dayfirst=self.dayfirst, parse_dates=[self.datetime_col])
            df = df.rename(columns={self.datetime_col: 'seconds'})
        except ValueError:
            try:
                df = pd.read_csv(self.filename, sep=self.separator, decimal=self.decimal_separator, 
                                 dayfirst=self.dayfirst, parse_dates=['time'])
                df = df.rename(columns={'time': 'seconds'})
            except Exception as e:
                print(f"Erro ao ler o arquivo CSV: {e}")
                sys.exit(1)
        
        df.dropna(inplace=True)
        df['seconds'] = (df['seconds'] - df['seconds'][0]).dt.total_seconds() / 3600
        df = df.set_index('seconds').replace(',', '.', regex=True).apply(lambda x: pd.to_numeric(x, errors='ignore'))
        
        return df

    def apply_transformations(self):
        """Apply multiplication and division to the specified columns."""
        if not self.cols_to_multiply:
            self.cols_to_multiply = self.data.columns
        self.data[self.cols_to_multiply] = self.data[self.cols_to_multiply].mul(self.multiply)

        if not self.cols_to_divide:
            self.cols_to_divide = self.data.columns
        self.data[self.cols_to_divide] = self.data[self.cols_to_divide].div(self.division)

        if self.filename == './plotagem/registros de monitoramento dos testes de envelhecimento/outros/logs/response_times.csv':
            self.data['response_time'] = self.data['response_time'] / 1000

    def plot_column(self, col):
        """Plot a specific column with a regression line."""
        ylabel = (col + " " + self.ylabel) if isinstance(self.ylabel, str) and self.include_col_ylabel else self.ylabel
        x = self.data.index.to_numpy().reshape((-1, 1))
        y = self.data[col].fillna(0).to_numpy().reshape((-1, 1))

        model = LinearRegression()
        model.fit(x, y)
        y_pred = model.predict(x)

        ax = self.data.plot(
            y=col,
            legend=0,
            xlabel='Time(h)',
            ylabel=ylabel if isinstance(self.ylabel, str) else self.ylabel.get(col, col),
            title=self.title if isinstance(self.title, str) else self.title.get(col, col),
            figsize=(10, 5),
            style='k',
        )
        
        ax.plot(x, y_pred, color='red')  # Add regression line
        plt.show()

        fig = ax.get_figure()
        fig.savefig(f'./plotagem/plot_images/{self.title}-{col}.png')

    def plot(self):
        """Plot all columns after transformations."""
        self.apply_transformations()
        for col in self.data.columns:
            self.plot_column(col)


try:
    plotter = DataPlotter(
        filename='data.csv',
        ylabel='Response Time (ms)',
        datetime_col='date_time',
        title='Response Times Over Time',
        separator=';',
        decimal_separator=',',
        dayfirst=False,
        multiply=1,
        division=1,
        include_col_ylabel=False,
        cols_to_divide=['response_time'],
        cols_to_multiply=['response_time']
    )
    plotter.plot()
except ImportError as e:
    print(f'Erro de importação: {e}')
    sys.exit(1)
