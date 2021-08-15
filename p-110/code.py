import csv
import statistics
import random
import pandas as pd
import plotly.figure_factory as ff


df=pd.read_csv("data.csv")
data = df["reading_time"].tolist()
print("Population mean ", statistics.mean(data))
print("Population Stdev ", statistics.stdev(data))



def random30means(counter):
    dataSet=[]
    for i in range(0,counter):
        randomIndex=random.randint(0,len(data))
        value=data[randomIndex]
        dataSet.append(value)
    mean=statistics.mean(dataSet)
    return mean



def show_fig(mean_list):
    df=mean_list
    fig=ff.create_distplot([df], ["reading_time"], show_hist=False)
    fig.show()



def setup():
    mean_list=[]
    for i in range(0,100):
        set_of_means=random30means(30)
        mean_list.append(set_of_means)
    show_fig(mean_list) 
    print( "Sample Mean ",statistics.mean(mean_list))
    stdev=statistics.stdev(mean_list)
    print("Sample Stdev ",statistics.stdev(mean_list))
setup()