import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import plotly.express as px

sns.set_theme(style="whitegrid")

ds = pd.read_csv('file:///Users/ilyasuchkov/Desktop/big_five_stocks.csv')
ds.columns = ['Date', 'Name', 'Open', 'Close', 'High', 'Low', 'Volume']
ds.head(6)

# I've changed the names of coloumns for more usability, because the first coloumn was unnamed. 
# Now I tried to count the mean value of four parametrs: 
# Open prices, Close prices, The highest price and The lowest one.
# For the comvinience I did round the output means.

print('Mean Open:',round(ds.Open.mean(), 2))

print('Mean Close:', round(ds.Close.mean(), 2))

print('Mean High:', round(ds.High.mean(), 1))

print('Mean Low:', round(ds.Low.mean(),1))

# Here I've defined the medians for the same parameters.
# Initially, I had to sort all this parameters to execute this in a right way.
# For the comvinience I did round the output medians. 

ds.sort_values(by=['Open'])
print('Median Open:', round(ds.Open.median(), 1))

ds.sort_values(by=['Close'])
print('Median Close:', round(ds.Close.median(), 1))

ds.sort_values(by=['High'])
print('Median High:', round(ds.High.median(), 1))

ds.sort_values(by=['Low'])
print('Median Low:', round(ds.Low.median(), 1))


print('Deviation Open:',round(ds.Open.std(), 2))

print('Deviation Close:', round(ds.Close.std(), 2))

print('Deviation High:', round(ds.High.std(), 1))

print('Deviation Low:', round(ds.Low.std(),1))

#Now, lets illustarte prices of all stocks on NY Market at the Opening of a day.
# Here, I've illustated prices of "Nasdaq" at closing in the same manner.
# The market saw an upward trand at 2000, closing at the prive 5,060.
# Starting from 2010 the NY Market started to go up and up 
# and broke the record of 2000, being at 2019 near 8,325 bucks for closing.

import pandas as pd
import plotly.express as px

fig = px.line(ds, x = 'Date' , y = 'Open', title='Prices of Big Five Stocks on Nasdaq at Openening')
fig.show()

# Here, I've illustated prices of "Nasdaq" at closing in the same manner.
# At the closing market behave quite simillar, but ther are a few diferences:
# The highest point at 2000 was 5,048 bucks in total,
# The highest closing for whole period was in July of 2019 - 8,330 dollars. 

fig = px.line(ds, x = 'Date' , y = 'Close', title='Prices of Big Five Stocks on Nasdaq at Closing')
fig.show() 

# These two graph are quite simillar, but the third one is different.
# I did try to show how many stocks there were traded for the whole period of time: from 1971 to 2019.
# As we can see the amount of trades on April 2006 and May 2012 are enormous. 
# It was near 600M trades in those monthes.

import plotly.express as px

fig = px.line(ds, x='Date', y="Volume")
fig.show()

# Now I can illustrate the approximate number of dates counted from company's IPO.
# We can see that the first Company that had IPO was Apple and the latest IPO of Big Five was made pe Facebook. 
# We do not count ^IXIC, because it is the NY Market index.

plt.bar(ds.Name.value_counts().index, ds.Name.value_counts().values)
