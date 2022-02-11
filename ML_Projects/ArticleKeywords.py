import pandas as pd
import numpy as np
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
import matplotlib.pyplot as plt

# For Google Colab
# from google.colab import files
# import io

'''
Preprocessing Description:
The preprocessing stage of this project was difficult because cleaning the data was mainly dependent
upon missing fields in the dataset. In order to get around this, I sampled 30 articles from the dataset
so that when dropping empty cells, I would still have >= 20 articles to work with. Similarly, when reading
from the csv file, pandas struggled with the varying lengths of fields, so ignoring bad lines was necessary
for getting useful data from the dataset of articles. This preprocessing stage would be much more difficult
with hundreds or thousands of articles to parse through, especially if it is important to use all of the data
available (i.e. not dropping/skipping any rows). Cleaning this dataset on a large scale could potentially cause
issues with the amount of useable data.
'''

# upload = files.upload()
# data =  pd.read_csv(io.BytesIO(upload['IEEE_Articles.csv']), error_bad_lines=False).sample(30)

# Sample 30 articles from database so that we have >= 20 after preprocessing
data = pd.read_csv('IEEE_Articles.csv', error_bad_lines=False).sample(30)

# Extract keywords from article and create baskets
keywords = data[['Author Keywords']].dropna(how='all')
baskets = []
for each in keywords.values:
    baskets.append(each[0].split(';'))
   
# Create Transaction Encoder and fit keyword baskets to create encoded dataframe
te = TransactionEncoder()
te_ary = te.fit(baskets).transform(baskets)
df = pd.DataFrame(te_ary, columns=te.columns_)

# Create Histogram of the distribution of the support counts for 1-itemsets
frequent_itemsets = apriori(df, min_support=.01, use_colnames=True, max_len=1)
frequent_itemsets['support'] = frequent_itemsets['support']*len(baskets)
plt.hist(frequent_itemsets['support'])
plt.title("IEEE Article Keyword Frequency")
plt.xlabel("Support Count")
plt.ylabel("Frequency")
plt.show()

# Create dictionary of itemsets mapped to support counts. This is used to find Top 10 itemsets.
datadict = {}
for key in frequent_itemsets[['support', 'itemsets']].values:
    datadict[list(key[1])[0]] = key[0]
# Iterate over the sorted datadict and display top 10 itemsets with largest support counts
count = 0
print("===========================================================\nTop 10 Keywords\n===========================================================")
for key,value in sorted(datadict.items(), key=lambda k:k[1], reverse=True):
    print(key, value)
    count += 1
    if count == 10:
        break

# Run Apriori with each of the relative support thresholds
support_thresholds = [.05, .1, .15, .2, .25]
for sup in support_thresholds:
    # List of Frequent Item-sets and their support counts
    print("\nRelative Support Threshold: %s"%sup)
    frequent_itemsets = apriori(df, min_support=sup, use_colnames=True)
    frequent_itemsets['length'] = frequent_itemsets['itemsets'].apply(lambda x:len(x))
    print(frequent_itemsets)
    # Running Time of Apriori Algorithm
    print("\nApriori Running Time: O(2^%s)"%len(frequent_itemsets['itemsets']))
    print('-------------------------------------------------------')
    
