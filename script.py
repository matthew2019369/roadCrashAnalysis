import pandas as pd 
import numpy as np
import seaborn as sns
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


class ImportData:

	def __init__(self):
		unit_2018=pd.read_csv("Datas/2018_DATA_SA_Units.csv")
		crash_2018=pd.read_csv("Datas/2018_DATA_SA_Crash.csv")
		casual_2018=pd.read_csv("Datas/2018_DATA_SA_Casualty.csv")
		unit_2017=pd.read_csv("Datas/2017_DATA_SA_Units.csv")
		crash_2017=pd.read_csv("Datas/2017_DATA_SA_Crash.csv")
		casual_2017=pd.read_csv("Datas/2017_DATA_SA_Casualty.csv")
		data = pd.merge(casual_2018,unit_2018,how='left',left_on=['REPORT_ID','UND_UNIT_NUMBER'],right_on=['REPORT_ID','Unit No'])
		full_2018 = pd.merge(data,crash_2018,how='left',on='REPORT_ID')
		data = pd.merge(casual_2017,unit_2017,how='left',left_on=['REPORT_ID','UND_UNIT_NUMBER'],right_on=['REPORT_ID','Unit No'])
		full_2017 = pd.merge(data,crash_2017,how='left',on='REPORT_ID')
		self.df= pd.concat([full_2017,full_2018],axis=0)

	def train_test_split(self):
		tmp = self.df
		if tmp is not None:
			pass
		else:
			print("Data does not exist!")

	def get_columns(self):
		tmp = self.df
		if tmp is not None:
			return tmp.columns
		else:
			print("Data does not exist!")

	def null_report(self):
		tmp = self.df
		if tmp is not None:
			val = {x:y for x,y in zip(tmp.isnull().sum().index ,tmp.isnull().sum()) if y>0}
			if not val:
				return "No null values"

			result = pd.DataFrame.from_dict(val,orient='index',columns=['Null Count'])
			result['% of null count'] = 100*result['Null Count']/tmp.shape[0]
			result['% of null count'].plot(kind='bar',title='Null report')
			plt.ylabel('% of null count')
			plt.xlabel('Variable')
			return result
		else:
			print("Data does not exist!")

	def set_data(self,new_data):
		self.df=new_data

	def get_data_shape(self):
		tmp = self.df
		if tmp is not None:
			print('The data contains {} rows and {} columns.'.format(tmp.shape[0],tmp.shape[1]))
		else:
			print("Data does not exist!")

	def get_data(self):
		return self.df

	def remove_cols_from(self, columns):
		tmp = self.df
		if tmp is not None:
			tmp = tmp.drop(columns, axis=1)
			self.df = tmp
			print('After removal, the data contains {} rows and {} columns.'.format(tmp.shape[0],tmp.shape[1]))
		else:
			print("Data does not exist!")

	def save_data_to_csv(self,path):
		tmp = self.df
		if tmp is not None:
			tmp.to_csv(path,index=False)