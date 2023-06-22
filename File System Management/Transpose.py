import openpyxl
import pandas as pd
from datetime import datetime


df=pd.read_csv('C:/Users/mlpradhan/OneDrive - alliedelec.com/Desktop/Testing/Test.csv')
print(df)
#dataframe tranpose
df1 =df.transpose
print(df1)

file_name = 'mycsvfile_' + str(datetime.now()) + '.csv'
df2=df1.to_csv('C:/Users/mlpradhan/OneDrive - alliedelec.com/Desktop/Testing/testintranspose.csv')
df2 =df1.to_csv(file_name)
print('Done')

#############################################

#writer = pd.ExcelWriter('Test.xlsx', engine='xlsxwriter')






