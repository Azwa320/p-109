import csv
import plotly.express as pd
import plotly.figure_factory as ff
import pandas as pd
import statistics
import random
import plotly.graph_objects as go

df=pd.read_csv("data.csv")
data= df["reading score"].tolist()

mean=sum(data)/len(data)
std_deviation=statistics.stdev(data)
median=statistics.median(data)
mode=statistics.mode(data)

first_std_deviation_start,first_std_deviation_end=mean-std_deviation,mean+std_deviation
second_std_deviation_start,second_std_deviation_end=mean-(2*std_deviation),mean+(2*std_deviation)
third_std_deviation_start,third_std_deviation_end=mean-(3*std_deviation),mean+(3*std_deviation)

fig=ff.create_distplot([data],["reading score"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start,first_std_deviation_start],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start,first_std_deviation_start],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end,first_std_deviation_end],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 2"))
fig.show()

list_data_1_std_dev=[result for result in data if result> first_std_deviation_start and result< first_std_deviation_end]
list_data_2_std_dev=[result for result in data if result> second_std_deviation_start and result< second_std_deviation_end]
list_data_3_std_dev=[result for result in data if result> third_std_deviation_start and result< third_std_deviation_end]

print("mean of the data is {}".format(mean))
print("median of the data is {}".format(median))
print("mode of the data is {}".format(mode))
print("standard deviation of the data is {}".format(std_deviation))
print("{} of data lies within first standard deviation".format(len(list_data_1_std_dev)*100.0/len(data)))
print("{} of data lies within second standard deviation".format(len(list_data_2_std_dev)*100.0/len(data)))
print("{} of data lies within third standard deviation".format(len(list_data_3_std_dev)*100.0/len(data)))