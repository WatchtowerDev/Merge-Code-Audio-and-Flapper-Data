import pandas as pd
import numpy as np
import math
import xlsxwriter
from scipy import stats

audio1repeat=pd.read_csv("data from first audio trial.csv")
audio2repeat=pd.read_csv("data (1).csv")

#Can convert audio data into milliseconds, but is a massive memory use
#audio1repeat=pd.concat([audio1repeat]*1000000)
#audio1repeat=audio1repeat.sort_values(by="Time (Minutes)")
#audio1repeat["TimeS"]=np.nan

#Handles misaligned indexes
audio1repeat=audio1repeat.reset_index()
audio2repeat=audio2repeat.reset_index()

#audio1repeat["TimeS"]=audio1repeat["Time S"]*1000000 + audio1repeat.index%1000000
flapper1data=pd.read_csv("Wise_Run4_Trimed.csv")

#Converts milliseconds to seconds and floors each observation
flapper1data["TimeS"]=np.floor(flapper1data["Time S"]/1000)
flapper1data["Time (Minutes)"]=flapper1data["Time S"]/60
#flapper1data["TimeS"] =flapper1data.TimeS.astype(int)



mergeData = pd.merge(audio1repeat, flapper1data, on="TimeS")
mergeData = pd.merge(mergeData, audio2repeat, on="TimeS")
mergeData["Time (Minutes)_x"]=mergeData["TimeS"]/60
mergeData=mergeData.reset_index()
mergeData['Anomaly']=0
mergeData['Anomaly']=mergeData['Cluster'].apply(lambda x: 3 if (x==4 or x==24 or x==35
                                                or x==7 or x==17) else 2 if (x==3 or
                                                x==11 or x==11 or x==14 or
                                                x==16 or x==19 or x==21 or
                                                x==23 or x==29 or x==33) else 1)
mergeData=mergeData.sort_values(by=['Cluster'])

'''
mergeDataSelected=mergeData[((mergeData['Cluster']==7) | (mergeData['Cluster']==14) | (mergeData['Cluster']==17))]
mergeDataSelected=mergeDataSelected.sort_values(by=['Cluster'])
mergeDataSelected.to_csv("Merged Data Cluster 7 14 17.csv")

'''

mergeData.to_csv("MergedDataAudioandFlappersRun1FULL.csv")
'''
mergeData1 = mergeData[((((mergeData.flapper2< 21) | (mergeData.flapper3 < 16)) & (mergeData.TimeS<240)) |
                        np.logical_and((((mergeData.flapper2< 21) | (mergeData.flapper3 < 16.5))
                                           & (mergeData.TimeS>240)),(((mergeData.flapper2< 21)
                                                                    | (mergeData.flapper3 < 16.5))  & (mergeData.TimeS<540)))
                        | np.logical_and((((mergeData.flapper2< 20) | (mergeData.flapper3 < 14))
                                           & (mergeData.TimeS>540)),(((mergeData.flapper2< 20)
                                                                    | (mergeData.flapper3 < 14))  & (mergeData.TimeS<900))) |
                        np.logical_and((((mergeData.flapper2< 20) | (mergeData.flapper3 < 14))
                                           & (mergeData.TimeS>900)),(((mergeData.flapper2< 20)
                                                                    | (mergeData.flapper3 < 14))  & (mergeData.TimeS<1200))) |
                        np.logical_and((((mergeData.flapper2< 20) | (mergeData.flapper3 < 15.5))
                                           & (mergeData.TimeS>1200)),(((mergeData.flapper2< 20)
                                                                    | (mergeData.flapper3 < 15.5))  & (mergeData.TimeS<1500))) |
                        np.logical_and((((mergeData.flapper2< 19) | (mergeData.flapper3 < 14))
                                           & (mergeData.TimeS>1500)),(((mergeData.flapper2< 19)
                                                                    | (mergeData.flapper3 < 14))  & (mergeData.TimeS<1740))) |
                        np.logical_and((((mergeData.flapper2< 16.5) | (mergeData.flapper3 < 14))
                                           & (mergeData.TimeS>1740)),(((mergeData.flapper2< 16.5)
                                                                    | (mergeData.flapper3 < 14))  & (mergeData.TimeS<2040))) |
                        np.logical_and((((mergeData.flapper2< 14) | (mergeData.flapper3 < 10))
                                           & (mergeData.TimeS>2040)),(((mergeData.flapper2< 14)
                                                                    | (mergeData.flapper3 < 10))  & (mergeData.TimeS<2340))) |
                        np.logical_and((((mergeData.flapper2< 14) | (mergeData.flapper3 < 8))
                                           & (mergeData.TimeS>2340)),(((mergeData.flapper2< 14)
                                                                    | (mergeData.flapper3 < 8))  & (mergeData.TimeS<2640))) |
                        np.logical_and((((mergeData.flapper2< 14) | (mergeData.flapper3 < 6))
                                           & (mergeData.TimeS>2640)),(((mergeData.flapper2< 14)
                                                                    | (mergeData.flapper3 < 6))  & (mergeData.TimeS<2880))) |
                        np.logical_and((((mergeData.flapper2< 10) | (mergeData.flapper3 < 6))
                                           & (mergeData.TimeS>2880)),(((mergeData.flapper2< 10)
                                                                    | (mergeData.flapper3 < 6))  & (mergeData.TimeS<3300))))]
                       
mergeData1=mergeData1.sort_values(by=['Cluster'])
mergeData1.to_csv("MergedDataAudioandFlappersRun1.csv")
'''
'''
overallDescribe=pd.DataFrame()
overallDescribe["flapper0"]=mergeData["flapper0"].describe()
overallDescribe["flapper1"]=mergeData["flapper1"].describe()
overallDescribe["flapper2"]=mergeData["flapper2"].describe()
overallDescribe["flapper3"]=mergeData["flapper3"].describe()
overallDescribe["flapper4"]=mergeData["flapper4"].describe()
overallDescribe["flapper5"]=mergeData["flapper5"].describe()
overallDescribe["flapper6"]=mergeData["flapper6"].describe()
overallDescribe["flapper7"]=mergeData["flapper7"].describe()

mergeData["Delta F2"]=mergeData["Delta F2"].astype(float)
mergeData["Delta F3"]=mergeData["Delta F3"].astype(float)
mergeData["Delta Ax"]=mergeData["Delta Ax"].astype(float)
mergeData["Delta Ay"]=mergeData["Delta Ay"].astype(float)
mergeData["Delta Az"]=mergeData["Delta Az"].astype(float)
'''

ClusteredData=mergeData.groupby('Cluster')
#DescribeF0=ClusteredData["flapper0"].describe()
#DescribeF1=ClusteredData["flapper1"].describe()
DescribeF2=ClusteredData["flapper2"].describe()
DescribeF3=ClusteredData["flapper3"].describe()
#DescribeF4=ClusteredData["flapper4"].describe()
#DescribeF5=ClusteredData["flapper5"].describe()
#DescribeF6=ClusteredData["flapper6"].describe()
#DescribeF7=ClusteredData["flapper7"].describe()
#DescribeF0=DescribeF0.append(mergeData["flapper0"].describe())
#DescribeF1=DescribeF1.append(mergeData["flapper1"].describe())
DescribeF2=DescribeF2.append(mergeData["flapper2"].describe())
DescribeF3=DescribeF3.append(mergeData["flapper3"].describe())
#DescribeF4=DescribeF4.append(mergeData["flapper4"].describe())
#DescribeF5=DescribeF5.append(mergeData["flapper5"].describe())
#DescribeF6=DescribeF6.append(mergeData["flapper6"].describe())
#DescribeF7=DescribeF7.append(mergeData["flapper7"].describe())
DescribeAccx=ClusteredData["accX"].describe()
DescribeAccy=ClusteredData["accY"].describe()
DescribeAccz=ClusteredData["accZ"].describe()
DescribeAccx=DescribeAccx.append(mergeData["accX"].describe())
DescribeAccy=DescribeAccx.append(mergeData["accY"].describe())
DescribeAccz=DescribeAccz.append(mergeData["accZ"].describe())


'''
DescribeDeltaF2=ClusteredData["Delta F2"].describe()
DescribeDeltaF3=ClusteredData["Delta F3"].describe()
DescribeDeltaAx=ClusteredData["Delta Ax"].describe()
DescribeDeltaAy=ClusteredData["Delta Ay"].describe()
DescribeDeltaAz=ClusteredData["Delta Az"].describe()

DeltaF2ByCluster=pd.DataFrame()
DeltaF3ByCluster=pd.DataFrame()
DeltaAxByCluster=pd.DataFrame()
DeltaAyByCluster=pd.DataFrame()
DeltaAzByCluster=pd.DataFrame()

DeltaF2ByCluster["Cluster"]=mergeData["Cluster"]
DeltaF3ByCluster["Cluster"]=mergeData["Cluster"]
DeltaAxByCluster["Cluster"]=mergeData["Cluster"]
DeltaAyByCluster["Cluster"]=mergeData["Cluster"]
DeltaAzByCluster["Cluster"]=mergeData["Cluster"]


DeltaF2ByCluster["DeltaF2"]=mergeData["Delta F2"]
DeltaF3ByCluster["DeltaF3"]=mergeData["Delta F3"]
DeltaAxByCluster["DeltaAx"]=mergeData["Delta Ax"]
DeltaAyByCluster["DeltaAy"]=mergeData["Delta Ay"]
DeltaAzByCluster["DeltaAz"]=mergeData["Delta Az"]

DeltaF2ByCluster.groupby('Cluster')
DeltaF3ByCluster.groupby('Cluster')
DeltaAxByCluster.groupby('Cluster')
DeltaAyByCluster.groupby('Cluster')
DeltaAzByCluster.groupby('Cluster')





DescribeDeltaF2=DescribeDeltaF2.append(mergeData["Delta F2"].describe())
DescribeDeltaF3=DescribeDeltaF3.append(mergeData["Delta F3"].describe())
DescribeDeltaAx=DescribeDeltaAx.append(mergeData["Delta Ax"].describe())
DescribeDeltaAy=DescribeDeltaAy.append(mergeData["Delta Ay"].describe())
DescribeDeltaAz=DescribeDeltaAz.append(mergeData["Delta Az"].describe())


#since differences between sensor's are so small, we magnify them by a scale of 10
DescribeDeltaF2["mean"]=DescribeDeltaF2["mean"]*100
DescribeDeltaF3["mean"]=DescribeDeltaF3["mean"]*100

writer = pd.ExcelWriter('MergeDataStatsBasicForDelta.xlsx', engine='xlsxwriter')

DescribeDeltaF2.to_excel(writer, sheet_name='Delta F2')
DescribeDeltaF3.to_excel(writer, sheet_name='Delta F3')
DescribeDeltaAx.to_excel(writer, sheet_name='Delta Ax')
DescribeDeltaAy.to_excel(writer, sheet_name='Delta Ay')
DescribeDeltaAz.to_excel(writer, sheet_name='Delta Az')
DeltaF2ByCluster.to_excel(writer, sheet_name='Delta F2 By Cluster')
DeltaF3ByCluster.to_excel(writer, sheet_name='Delta F3 By Cluster')
DeltaAxByCluster.to_excel(writer, sheet_name='Delta Ax By Cluster')
DeltaAyByCluster.to_excel(writer, sheet_name='Delta Ay By Cluster')
DeltaAzByCluster.to_excel(writer, sheet_name='Delta Az By Cluster')


writer.save()

'''
#DescribeDeltaF2.to_csv('Descrive Delta F2.csv')
#DescribeDeltaF3.to_csv('Describe Delta F2.csv')
#DescribeDeltaAx.to_csv('Describe Delta F3.csv')
#DescribeDeltaAy.to_csv('Describe Delta Ax.csv')
#DescribeDeltaAz.to_csv('Describe Delta Ay.csv')
#DeltaF2ByCluster.to_csv('Delta F2 By Cluster.csv')
#DeltaF3ByCluster.to_csv('Delta F3 By Cluster.csv')
#DeltaAxByCluster.to_csv('Delta Ax By Cluster.csv')
#DeltaAyByCluster.to_csv('Delta Ay By Cluster.csv')
#DeltaAzByCluster.to_csv('Delta Az By Cluster.csv')
#writer = pd.ExcelWriter('MergeDataStatsBasic1.xlsx', engine='xlsxwriter')

#DescribeF0.to_excel(writer, sheet_name='Flapper0')

#DescribeF1.to_excel(writer, sheet_name='Flapper1')

#DescribeF2.to_excel(writer, sheet_name='Flapper2')

#DescribeF3.to_excel(writer, sheet_name='Flapper3')

#DescribeF4.to_excel(writer, sheet_name='Flapper4')

#DescribeF5.to_excel(writer, sheet_name='Flapper5')

#DescribeF6.to_excel(writer, sheet_name='Flapper6')

#DescribeF7.to_excel(writer, sheet_name='Flapper7')

#DescribeAccx.to_excel(writer, sheet_name='Accx')

#DescribeAccy.to_excel(writer, sheet_name='Accy')

#DescribeAccz.to_excel(writer, sheet_name='Accz')

#writer.save()

#z0 = np.abs(stats.zscore(DescribeF0["mean"]))
#z1 = np.abs(stats.zscore(DescribeF1["mean"]))
#z2 = np.abs(stats.zscore(DescribeF2["mean"]))
#z3 = np.abs(stats.zscore(DescribeF3["mean"]))
#z4 = np.abs(stats.zscore(DescribeF4["mean"]))
#z5 = np.abs(stats.zscore(DescribeF5["mean"]))
#z6 = np.abs(stats.zscore(DescribeF6["mean"]))
#z7 = np.abs(stats.zscore(DescribeF7["mean"]))

#This is the hypothesis testing of each average mean to find the outliers
zF2 = np.abs(stats.zscore(DescribeF2["mean"]))
zF3 = np.abs(stats.zscore(DescribeF3["mean"]))
zAx = np.abs(stats.zscore(DescribeAccx["mean"]))
zAy = np.abs(stats.zscore(DescribeAccy["mean"]))
zAz = np.abs(stats.zscore(DescribeAccz["mean"]))

AnomaliesforStats=pd.read_csv("Anomaly recordings for stat testing run 1 .csv")
zStatAnom=np.abs(stats.zscore(AnomaliesforStats["Anomaly Recording"]))

#All pictures with model results
AnomalyListFull=pd.read_csv("All pictures with model results.csv", dtype={"Image Link": str, "Results": str, "Score": str})
AnomalyListFull=AnomalyListFull[AnomalyListFull.Results != "'One', 'Three'] "]

AnomalyListFull=AnomalyListFull.sort_values(by=['Image Link'])
mergeData=mergeData.sort_values(by=['Image Link'])
AnomalyListFull1=pd.merge(AnomalyListFull, mergeData[['Image Link', 'Time (Minutes)_x']], on='Image Link')
AnomalyListFull1=AnomalyListFull1.drop_duplicates()
AnomalyListFull1.to_csv("FullAnomalyListRun1.csv")

#DescribeC1["flapper0"]=mergeData["flapper0"].describe((mergeData["Cluster"]==1))
