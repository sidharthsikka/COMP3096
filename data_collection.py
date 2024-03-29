import pandas as pd

filenames = ['WIOD_Data/WIOT2000_Nov16_ROW.xlsx','WIOD_Data/WIOT2001_Nov16_ROW.xlsx','WIOD_Data/WIOT2002_Nov16_ROW.xlsx','WIOD_Data/WIOT2003_Nov16_ROW.xlsx','WIOD_Data/WIOT2004_Nov16_ROW.xlsx','WIOD_Data/WIOT2005_Nov16_ROW.xlsx', 'WIOD_Data/WIOT2006_Nov16_ROW.xlsx','WIOD_Data/WIOT2007_Nov16_ROW.xlsx','WIOD_Data/WIOT2008_Nov16_ROW.xlsx','WIOD_Data/WIOT2009_Nov16_ROW.xlsx','WIOD_Data/WIOT2010_Nov16_ROW.xlsx','WIOD_Data/WIOT2011_Nov16_ROW.xlsx','WIOD_Data/WIOT2012_Nov16_ROW.xlsx','WIOD_Data/WIOT2013_Nov16_ROW.xlsx','WIOD_Data/WIOT2014_Nov16_ROW.xlsx']

output = list(range(2000,2015))

for i in range(0, len(filenames)):
	df = pd.read_excel(filenames[i], skiprows=[1,2],index_col=0, parse_cols=([0] + list(range(3,2467))))
	# Delete any self pointing edges
	for col in df.columns:
		df.loc[col,col] = 0.0

	# Delete any country where there is no trade
	for col in df.columns:
		if df[col].sum() == 0.0 and df.loc[col].sum() == 0.0:
			df = df.drop(col, axis=0)
			df = df.drop(col, axis=1)

	df.to_pickle('WIOD_Data/pickled_data/' + str(output[i]) + '.pkl')
	print(str(output[i]) + " DONE")