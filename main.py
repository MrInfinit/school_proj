import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


pathofmainfile = r'vgchartz-2024.csv'
pathofabbriviations = r'data_dictionary.csv'


df = pd.read_csv(pathofmainfile)
vg_df = df.ffill()
no_of_rows = len(df.index)

ab_df = pd.read_csv(pathofabbriviations)

#Creating a List of all Genres in the dataframe
genre_list = []
for i in range(no_of_rows):
    if vg_df.at[i,'Genre'] not in genre_list:
        genre_list.append(vg_df.at[i,'Genre'])
#print(genre_list)

#Creating a List of avg critic scores per genres
critic_score_list = []
for j in genre_list:
    sum = 0
    for i in range(no_of_rows):
        if j == vg_df.at[i,'Genre']:
            sum =+ vg_df.at[i,'Critic_Score']
    critic_score_list.append(sum)
#print(critic_score_list)

#Creating a List of total sales per genre
total_sales_list = []

for j in genre_list:
    sum = 0
    for i in range(no_of_rows):
        if j == vg_df.at[i,'Genre']:
            num = int(vg_df.at[i,'Total_Sales'])
            sum += num
    total_sales_list.append(sum)
#print(total_sales_list)

#Creating a List of sales in north america per genre
NA_sales_list = []
for j in genre_list:
    sum = 0
    for i in range(no_of_rows):
        if j == vg_df.at[i,'Genre']:
            num = int(vg_df.at[i,'NA_Sales'])
            sum += num
    NA_sales_list.append(sum)
#print(NA_sales_list)

#Creating a List of sales in japan per genre
JP_sales_list = []
for j in genre_list:
    sum = 0
    for i in range(no_of_rows):
        if j == vg_df.at[i,'Genre']:
            num = int(vg_df.at[i,'JP_Sales'])
            sum += num
    JP_sales_list.append(sum)
#print(JP_sales_list)

#Creating a List of sales in europe and africa per genre
PAL_sales_list = []
for j in genre_list:
    sum = 0
    for i in range(no_of_rows):
        if j == vg_df.at[i,'Genre']:
            num = int(vg_df.at[i,'PAL_Sales'])
            sum += num
    PAL_sales_list.append(sum)
#print(PAL_sales_list)

#Creating a list of sales in other parts of the world per genre
other_sales_list = []
for j in genre_list:
    sum = 0
    for i in range(no_of_rows):
        if j == vg_df.at[i,'Genre']:
            num = int(vg_df.at[i,'Other_Sales'])
            sum += num
    other_sales_list.append(sum)
#print(other_sales_list)

def readcsv():
    print(vg_df)

def abbriviations():
    print(ab_df)

def critic_score_sort():
    plt.bar(genre_list, critic_score_list)
    plt.show()

def sales_world():
    plt.bar(genre_list, total_sales_list)
    plt.show()

def sales_NA():
    plt.bar(genre_list,NA_sales_list)
    plt.show()

def sales_JP():
    plt.bar(genre_list,JP_sales_list)
    plt.show()

def sales_PAL():
    plt.bar(genre_list,PAL_sales_list)
    plt.show()

def sales_other():
    plt.bar(genre_list, other_sales_list)
    plt.show()

while True:
    print('=============================================================')
    print('1. show dataframe')
    print('2. Show Abbriviations')
    print('=============================================================')
    print('3. Genre of games sorted by Critic Score')
    print('4. Genre of games sorted by sales world wide')
    print('5. Genre of games sorted by sales in north america')
    print('6. Genre of games sorted by sales in japan')
    print('7. Genre of games sorted by sales in europe and africa')
    print('8. Genre of games sorted by sales in other parts of the world')
    print('=============================================================')
    option = eval(input('choose option: '))
    print('=============================================================')

    if option == 1:
        readcsv()
    elif option == 2:
        abbriviations()
    elif option == 3:
        critic_score_sort()
    elif option == 4:
        sales_world()
    elif option == 5:
        sales_NA()
    elif option == 6:
        sales_JP()
    elif option == 7:
        sales_PAL()
    elif option == 8:
        sales_other()
    elif option == 9:
        quit()
    else:
        pass
