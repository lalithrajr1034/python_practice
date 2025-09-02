Pandas Functions (100+)

📌 Data Creation
pd.Series() – Create a Series object.
pd.DataFrame() – Create a DataFrame object.
pd.read_csv() – Load data from a CSV file.
pd.read_excel() – Load data from an Excel file.
pd.read_sql() – Load data from SQL query or database.
pd.read_json() – Load data from a JSON file.
pd.read_html() – Parse tables from HTML.
pd.read_clipboard() – Load data from clipboard.
pd.read_parquet() – Load data from Parquet file.
pd.read_orc() – Load data from ORC file.
pd.read_feather() – Load data from Feather file.

📌 Data Inspection
.head() – Show first rows.
.tail() – Show last rows.
.shape – Get dimensions (rows, columns).
.info() – Show summary info.
.describe() – Get statistical summary.
.dtypes – Data types of each column.
.index – Show index info.
.columns – List all column names.
.memory_usage() – Memory usage of DataFrame.
.sample() – Random sample of rows.

📌 Selection & Indexing
.loc[] – Select rows/cols by label.
.iloc[] – Select rows/cols by position.
.at[] – Fast access by label.
.iat[] – Fast access by integer index.
.xs() – Cross-section selection.
.get() – Retrieve column with default.
.set_index() – Set column as index.
.reset_index() – Reset index.
.sort_index() – Sort by index.
.reindex() – Conform DataFrame to new index.

📌 Data Cleaning
.drop() – Drop rows/columns.
.dropna() – Drop missing values.
.fillna() – Fill missing values.
.isna() – Detect missing values.
.notna() – Detect non-missing values.
.replace() – Replace values.
.astype() – Change data type.
.rename() – Rename labels.
.duplicated() – Detect duplicates.
.drop_duplicates() – Remove duplicates.

📌 Data Transformation
.apply() – Apply function along axis.
.applymap() – Apply function elementwise.
.map() – Map values in Series.
.transform() – Transform values per group.
.pipe() – Apply function in method chain.
.eval() – Evaluate string expressions.
.query() – Query using expressions.

📌 Aggregations & Statistics
.sum() – Sum values.
.mean() – Mean values.
.median() – Median values.
.mode() – Mode values.
.min() – Minimum values.
.max() – Maximum values.
.std() – Standard deviation.
.var() – Variance.
.count() – Count non-NA.
.corr() – Correlation.
.cov() – Covariance.
.rank() – Ranking values.

📌 Grouping & Combining
.groupby() – Group data.
.pivot_table() – Create pivot tables.
.pivot() – Reshape data.
.melt() – Unpivot data.
.crosstab() – Cross-tabulation.
.merge() – Merge DataFrames.
.join() – Join DataFrames.
.concat() – Concatenate DataFrames.
.combine_first() – Fill NA with another DataFrame.

📌 Time Series
.to_datetime() – Convert to datetime.
.dt accessor – Access datetime properties.
.resample() – Resample time series.
.asfreq() – Convert to given frequency.
.shift() – Shift values.
.tshift() – Shift index.
.rolling() – Rolling window calculations.
.expanding() – Expanding window calculations.
.ewm() – Exponentially weighted calculations.

📌 Input/Output
.to_csv() – Export to CSV.
.to_excel() – Export to Excel.
.to_sql() – Export to SQL database.
.to_json() – Export to JSON.
.to_html() – Export to HTML.
.to_parquet() – Export to Parquet.
.to_feather() – Export to Feather.
.to_clipboard() – Copy to clipboard.
.to_markdown() – Export to Markdown.