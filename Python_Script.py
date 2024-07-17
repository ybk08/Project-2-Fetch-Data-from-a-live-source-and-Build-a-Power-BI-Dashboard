import pandas as pd

# URL of the raw Csv file on GitHub
url = "https://raw.githubusercontent.com/LokeshKumarChauhan/DE_with_powerBI/main/Walmart.csv"

# Read the Csv file into a pandas DataFrame
df = pd.read_csv(url)

# Display the rows of DataFrame
print(df)