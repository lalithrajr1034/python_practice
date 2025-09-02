Pandas Functions (100+)
<br>📌 Data Creation
<br>pd.Series()         – Create a Series object.
<br>pd.DataFrame()      – Create a DataFrame object.
<br>pd.read_csv()       – Load data from a CSV file.
<br>pd.read_excel()     – Load data from an Excel file.
<br>pd.read_sql()       – Load data from SQL query or database.
<br>pd.read_json()      – Load data from a JSON file.
<br>pd.read_html()      – Parse tables from HTML.
<br>pd.read_clipboard() – Load data from clipboard.
<br>pd.read_parquet()   – Load data from Parquet file.
<br>pd.read_orc()       – Load data from ORC file.
<br>pd.read_feather()   – Load data from Feather file.

<br>📌 Data Inspection
<br>.head()             – Show first rows.
<br>.tail()             – Show last rows.
<br>.shape              – Get dimensions (rows, columns).
<br>.info()             – Show summary info.
<br>.describe()         – Get statistical summary.
<br>.dtypes             – Data types of each column.
<br>.index              – Show index info.
<br>.columns            – List all column names.
<br>.memory_usage()     – Memory usage of DataFrame.
<br>.sample()           – Random sample of rows.

<br>📌 Selection & Indexing
<br>.loc[]              – Select rows/cols by label.
<br>.iloc[]             – Select rows/cols by position.
<br>.at[]               – Fast access by label.
<br>.iat[]              – Fast access by integer index.
<br>.xs()               – Cross-section selection.
<br>.get()              – Retrieve column with default.
<br>.set_index()        – Set column as index.
<br>.reset_index()      – Reset index.
<br>.sort_index()       – Sort by index.
<br>.reindex()          – Conform DataFrame to new index.

<br>📌 Data Cleaning
<br>.drop()              – Drop rows/columns.
<br>.dropna()            – Drop missing values.
<br>.fillna()            – Fill missing values.
<br>.isna()              – Detect missing values.
<br>.notna()             – Detect non-missing values.
<br>.replace()           – Replace values.
<br>.astype()            – Change data type.
<br>.rename()            – Rename labels.
<br>.duplicated()        – Detect duplicates.
<br>.drop_duplicates()   – Remove duplicates.

<br>📌 Data Transformation
<br>.apply()         – Apply function along axis.
<br>.applymap()      – Apply function elementwise.
<br>.map()           – Map values in Series.
<br>.transform()     – Transform values per group.
<br>.pipe()          – Apply function in method chain.
<br>.eval()          – Evaluate string expressions.
<br>.query()         – Query using expressions.

<br>📌 Aggregations & Statistics
<br>.sum()     – Sum values.
<br>.mean()    – Mean values.
<br>.median()  – Median values.
<br>.mode()    – Mode values. 
<br>.max()     – Maximum values.
<br>.std()     – Standard deviation.
<br>.var()     – Variance.
<br>.count()   – Count non-NA.
<br>.corr()    – Correlation.
<br>.cov()     – Covariance.
<br>.rank()    – Ranking values.

<br>📌 Grouping & Combining
<br>.groupby()     – Group data.
<br>.pivot_table() – Create pivot tables.
<br>.pivot()       – Reshape data.
<br>.melt()        – Unpivot data.
<br>.crosstab()    – Cross-tabulation.
<br>.merge()       – Merge DataFrames.
<br>.join()        – Join DataFrames.
<br>.concat()      – Concatenate DataFrames.
<br>.combine_first() – Fill NA with another DataFrame.

<br>📌 Time Series
<br>.to_datetime()   – Convert to datetime.
<br>.dt accessor     – Access datetime properties.
<br>.resample()      – Resample time series.
<br>.asfreq()        – Convert to given frequency.
<br>.shift()         – Shift values.
<br>.tshift()        – Shift index.
<br>.rolling()       – Rolling window calculations.
<br>.expanding()     – Expanding window calculations.
<br>.ewm()           – Exponentially weighted calculations.

<br>📌 Input/Output
<br>.to_csv()        – Export to CSV.
<br>.to_excel()      – Export to Excel.
<br>.to_sql()        – Export to SQL database.
<br>.to_json()       – Export to JSON.
<br>.to_html()       – Export to HTML.
<br>.to_parquet()    – Export to Parquet.
<br>.to_feather()    – Export to Feather.
<br>.to_clipboard()  – Copy to clipboard.
<br>.to_markdown()   – Export to Markdown.