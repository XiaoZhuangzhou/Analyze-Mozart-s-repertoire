import xlrd
import xlwt
import pandas as pd
import numpy as np

class ITEM(object):
 def __init__(self):
  self.df = pd.DataFrame
 def save_to_excel(self,filename):
  try :
   self.df.to_excel(filename)
   print("save OK!")
  except:
   print("save error")
 def read_from_excel(self,filename='list_of_liszt.xlsx'):
  data = xlrd.open_workbook('list_of_liszt.xlsx')
  table = data.sheets()[0]
  nrows = table.nrows
  list = []
  for i in range(20):#len(nrows)
   # print table.row_values(i)
   if table.row_values(i)[1] != '':
    list.append(table.row_values(i))
  self.df = pd.DataFrame(list)
  self.df.columns = ['name', 'orchestration', 'key', 'date', 'genre', 'description']

 def add_to_df(self,list):
   D={}
   for i in range(len(list)):
    D[self.df.columns[i]]=list[i]
   self.df=self.df.append(D,ignore_index=True)

 def search_to_df(self,list):
  for i in range(len(list)):
   if(list[i]==''):
    continue
   else:
    sea_df=self.df[self.df[self.df.columns[i]].isin([list[i]])]
  return sea_df
 def sort_df(self,value):
  return self.df.sort_index(by=value)

w=ITEM()
w.read_from_excel()
w.add_to_df([1,2,3,5,4,6])
w.add_to_df([1,2,3,5,6,6])
w.add_to_df([1,2,3,5,5,6])
print(w.df)
sea_df=w.search_to_df([1,2,3,5,'',6])
print(sea_df)
print(w.sort_df('genre'))