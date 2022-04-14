import matplotlib.pyplot as plt
import csv
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg # GUI 元件
from matplotlib.figure import Figure
# 換成中文的字體
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False  # 步驟二（解決座標軸負數的負號顯示問題）

#### 第1題 ######
#請自行到 openData 找自己感興趣的題目來做
#txt, CSV, XLSX, XLS
#比如：
#https://data.tycg.gov.tw/
#https://data.taipei/
#http://www.kaggle.com

#先不找JSON, XML,  SOAP

#### 第2題 ######
#分析數據
#Max, Min, Ave,  Mid 中間值, 均值......

#166-CSV-環境輻射即時監測資訊歷史資料-圖表-統計.py
#### 第3題 ######
#畫圖表
#156-作業答案-讀取excel顯示9個圖表.py



#### 第4 題 ######
#tkinter 做一個UI  和Tree 做資料的  顯示、新增 修改 刪除
#117-GUI練習-ERP訂單管理系統-解答-階段2-畫面完成.py

list1=[]
list2=[]                        #病例數
list3=[]                        #年齡
list4=[]                        #月份
list5=[]                        #男女數量
people=[]                       #男女確診數量
peopleName=["male","female"]

with open('covid19.txt', 'r',encoding="utf-8") as fin:
        read = csv.reader(fin, delimiter=',')
        header = next(read)   # 讀擋頭
        print(header)
        GPS=next(read)        # 讀 GPS
        x=0
        for row in read:
            # print(row[1])
            list1.append(int(x))                  # 第幾筆資料
            list2.append(float(row[8]))           # 取得 病例數 資料
            list3.append(float(row[7]))           #取得年齡層
            list4.append(float(row[2]))           #取得月份
            list5.append(str(row[5]))           # 取得男女數量
            plt.plot(int(x), float(row[1]), 'ro',label="")
            x=x+1


# 1. 印出所有資料
# 2. 最大 最小 平均

print("最大確診數",max(list2))                                              #最大確診數
print("最小確診數",min(list2))                                              #最小確診數
avg_value = 0 if len(list2) == 0 else sum(list2)/len(list2)
print("平均確診數",avg_value)                                               #平均確診數

print("最大年齡",max(list3))                                                #最大確診數
print("最小年齡",min(list3))
avg_age = 0 if len(list3) == 0 else sum(list3)/len(list3)
print("平均年齡",avg_age)

#計算2022年1~4月份數量
"""def calMonth(month):
    numMonth=[]
    for x in range(1, month + 1):
        num = 0
        for y in range(1, len(list4)):
            if list4[y] == x:
                num = num + 1
        numMonth.append(num)
    return numMonth
        #print(x, "月份總和為", num, end="\n")

calMonth(4)                                             #印出各月份數量"""
month=4                 #顯示1~4月的值
numMonth=[]             #將值做成陣列
for x in range(1, month + 1):
        num = 0
        for y in range(1, len(list4)):
            if list4[y] == x:
                num = num + 1
        numMonth.append(num)                    #各月份的值加入陣列的最後
        print(x, "月份總和為", num, end="\n")
#print(numMonth)
#計算男女數量
"""def calPeople():
    male = 0
    female = 0
    for x in range(1, len(list5)):
        if list5[x]=="F":
            male=male+1
        else:
            female=female+1
    #print("男生數量為",male,"\n女生數量為",female, end="\n")
    return male,female
print(calPeople())                                             #印出各男女數量"""

male = 0
female = 0
for x in range(1, len(list5)):
    if list5[x]=="F":
        male=male+1
    else:
        female=female+1
people.append(male)
people.append(female)
print("男生數量為",male,"\n女生數量為",female, end="\n")








fig,ax = plt.subplots(nrows=3, ncols=3)
 #第一張圖pie chart圓餅圖
#ax1 = plt.subplot(3,3,1)        #九宮格左上角
ax[0,0].pie(people,labels=peopleName,autopct='%1.1f%%',
        shadow=False, startangle=90)
#ax[0,0].axis('equal')                   #正方形的圖
ax[0,0].legend()         # 自動改變顯示的位置



# 第二張圖plot點狀圖
n=0
while n<len(numMonth):
    ax[0,1].plot( n+1 ,
                  numMonth[n],
                  "ro",
                  label=n+1)
    n=n+1
ax[0, 1].legend(loc="upper left")
ax[0, 1].set_title("每月確診數")
ax[0, 1].set_ylabel("確診數")  # 顯示y 座標的文字
ax[0, 1].set_xlabel("月份")  # 顯示x 座標的文字

ax[0,1].legend()

# 第三張圖bar長條圖(月份確診
n=0
while n<len(numMonth):
    ax[0,2].bar( n+1 ,
                  numMonth[n],
                  alpha=0.5,
                  #width=0.2+((int(numMonth[n])-n)*0.2),
                  label=n+1)
    n=n+1

ax[0, 2].legend(loc="upper left")
ax[0, 2].set_title("每月確診數")
ax[0, 2].set_ylabel("確診數")  # 顯示y 座標的文字
ax[0, 2].set_xlabel("月份")  # 顯示x 座標的文字
ax[0,2].legend()

# 第四張圖stem棉棒圖
n=0
while n<len(numMonth):
    ax[1,0].stem( n+1 ,
                  numMonth[n],
                  label=n+1)
    n=n+1


ax[1,0].legend(loc="upper left")
ax[1,0].set_title("每月確診數")
ax[1,0].set_ylabel("確診數")  # 顯示y 座標的文字
ax[1,0].set_xlabel("月份")  # 顯示x 座標的文字
ax[1,0].legend()

# 第五張圖bar長條圖(男女確診
n=0
while n<len(peopleName):
    ax[1,1].bar(str(peopleName[n]),
                 people[n],
                 label=peopleName[n])
    n=n+1

ax[1,1].legend(loc="upper left")
ax[1,1].set_title("男女確診人數")
ax[1,1].set_ylabel("確診數")  # 顯示y 座標的文字
ax[1,1].set_xlabel("性別")  # 顯示x 座標的文字"""
ax[1,1].legend()

#第六張圖step階層圖
n=0
while n<len(peopleName):
    ax[1,2].step(str(peopleName[n]),
                 people[n],
                 label=peopleName[n])
    n=n+1
ax[1,2].legend()

plt.show()

