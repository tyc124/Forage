#The CSV fules contain transaction data for Soul Food's entire morsel line.
#Each row indicates the quantity of a given type of morsel sold in a given region at a given price on a given day.

import pandas as pd

salesZero = pd.read_csv('daily_sales_data_0.csv')
salesOne = pd.read_csv('daily_sales_data_1.csv')
salesTwo = pd.read_csv('daily_sales_data_2.csv')

#print(salesZero.head())

#interested in total sales. total sales = quantity * price for a given day
listZero = []
listOne = []
listTwo = []

for i, row in salesZero.iterrows():
    result = float(row['quantity']) * float(row['price'][1:])
    listZero.append(result)

for i, row in salesOne.iterrows():
    result = float(row['quantity']) * float(row['price'][1:])
    listOne.append(result)

for i, row in salesTwo.iterrows():
    result = float(row['quantity']) * float(row['price'][1:])
    listTwo.append(result)

salesZero['sales']  = listZero
salesOne['sales'] = listOne
salesTwo['sales'] = listTwo

#remain date field and region field untouched
#product: only interested in pink morsel
salesZero = salesZero[salesZero['product'] == 'pink morsel']
salesOne = salesOne[salesOne['product'] == 'pink morsel']
salesTwo = salesTwo[salesTwo['product'] == 'pink morsel']

#output csv files: sales, date, region
salesZero = salesZero[['sales', 'date', 'region']]
salesOne = salesOne[['sales', 'date', 'region']]
salesTwo = salesTwo[['sales', 'date', 'region']]

salesZero.merge(salesOne).merge(salesTwo)
salesZero.to_csv('cleaned.csv')
