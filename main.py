import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


pathofmainfile = r'C:\Users\ksail\Documents\Python Code\School_Proj\vgchartz-2024.csv'
pathofabbriviations = r'C:\Users\ksail\Documents\Python Code\School_Proj\data_dictionary.csv'


df = pd.read_csv(pathofmainfile)
vg_df = df.ffill()
no_of_rows = len(df.index)

ab_df = pd.read_csv(pathofabbriviations)

#Creating a List of all Genres in the dataframe
genre_list = []
for i in range(no_of_rows):
    if vg_df.at[i,'Genre'] not in genre_list:
        genre_list.append(vg_df.at[i,'Genre'])

def readcsv():
    print(vg_df)

def abbriviations():
    print(ab_df)

def critic_score_sort():
    #Creating a List of avg critic scores per genres
    critic_score_list = []
    for j in genre_list:
        sum = 0
        for i in range(no_of_rows):
            if j == vg_df.at[i,'Genre']:
                sum =+ vg_df.at[i,'Critic_Score']
        critic_score_list.append(sum)

    plt.bar(genre_list, critic_score_list, width=0.5)
    plt.show()

def sales_world():

    #Creating a List of total sales per genre
    total_sales_list = []
    for j in genre_list:
        sum = 0
        for i in range(no_of_rows):
            if j == vg_df.at[i,'Genre']:
                num = round((vg_df.at[i,'Total_Sales']),2)
                sum += num
        total_sales_list.append(sum)
    
    while True:
        print('=============================================================')
        print('1. Display Data in the form of a line graph')
        print('2. Display Data in the form of a bar graph')
        print('3. Display Data in the form of a pie chart')
        print('4. Display all the graphs at once')
        print('5. Return to main program')
        print('=============================================================')
        choice = eval(input('choose option: '))
        print('=============================================================')

        if choice == 1:
            plt.plot(genre_list,total_sales_list)
            plt.show()
        elif choice == 2:
            plt.bar(genre_list, total_sales_list, width=0.5)
            plt.show()
        elif choice == 3:
            sum = 0
            percent_list = []
            for i in total_sales_list:
                sum += i
            for i in total_sales_list:
                value = 0
                value = round((i*100/sum), 2)
                percent_list.append(value)
            
            plt.pie(total_sales_list, startangle=90)
            plt.show()
        elif choice == 5:
            return
        else: 
            pass

def sales_NA():
    #Creating a List of sales in north america per genre
    NA_sales_list = []
    for j in genre_list:
        sum = 0
        for i in range(no_of_rows):
            if j == vg_df.at[i,'Genre']:
                num = round((vg_df.at[i,'NA_Sales']),2)
                sum += num
        NA_sales_list.append(sum)

    plt.bar(genre_list,NA_sales_list, width=0.5)
    plt.show()

def sales_JP():
    #Creating a List of sales in japan per genre
    JP_sales_list = []
    for j in genre_list:
        sum = 0
        for i in range(no_of_rows):
            if j == vg_df.at[i,'Genre']:
                num = round((vg_df.at[i,'JP_Sales']),2)
                sum += num
        JP_sales_list.append(sum)

    plt.bar(genre_list,JP_sales_list, width=0.5)
    plt.show()

def sales_PAL():
#Creating a List of sales in europe and africa per genre
    PAL_sales_list = []
    for j in genre_list:
        sum = 0
        for i in range(no_of_rows):
            if j == vg_df.at[i,'Genre']:
                num = round((vg_df.at[i,'PAL_Sales']),2)
                sum += num
        PAL_sales_list.append(sum)

    plt.bar(genre_list,PAL_sales_list, width=0.5)
    plt.show()

def sales_other():
    #Creating a list of sales in other parts of the world per genre
    other_sales_list = []
    for j in genre_list:
        sum = 0
        for i in range(no_of_rows):
            if j == vg_df.at[i,'Genre']:
                num = round((vg_df.at[i,'Other_Sales']),2)
                sum += num
        other_sales_list.append(sum)
    
    plt.bar(genre_list, other_sales_list, width=0.5)
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
    print('9. Quit the program')
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