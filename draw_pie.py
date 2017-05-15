# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.mlab as mlab
import pandas
import matplotlib.pyplot as plt#Call the Matplotlib module for the next drawing
def draw_pie(year):
  ph = pandas.read_csv('Crimes_2012-2015.csv')#Read data
  ph['year']=ph['Date.Rptd'].str.slice(6,10).astype(int)
  ph=ph[ph['year'] == year]
  labels = ph['CrmCd.Desc'].value_counts().keys()[0:10] #slice program
  labels_list=list()
  #Take the first ten of the crime, and the other types of crime as a total of other categories
  for i in range(len(labels)):
    labels_list.append(labels[i])
  labels_list.append('OTHER')
  print(list)
  X_list=[]
  X= ph['CrmCd.Desc'].value_counts()[0:10]
  print(X)
  #Calculate the total number of other categories of crime
  sum = X.sum()
  other_sum = len(ph)-sum
  for i in range(len(X)):
    X_list.append(X[i])#Table joins
  X_list.append(other_sum)#Table joins

  fig = plt.figure()
  plt.pie(X_list, labels=labels_list, autopct='%1.2f%%') #Plots/histograms
  plt.title("Criminal Type")

  plt.show()
  plt.savefig("Criminal Type")
draw_pie(2015)