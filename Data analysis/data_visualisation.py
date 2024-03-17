import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Sample plots describing variety of some data

data = "onlinefoods.csv"
df = pd.read_csv(data)

# Variety of age of customers
df['Age'].plot(kind='hist')
plt.show()
# Most of customers are between 22-25 yo


# Which Gender is more frequent?
sex_counts = df['Gender'].value_counts()

plt.bar(sex_counts.index, sex_counts.values)
plt.xlabel('Gender')
plt.ylabel('Count')
plt.title('Frequency of Each Gender')

plt.show()
# As we can see there are more Males than Females


# Is Gender correlated with feedback?
feedback_counts_by_gender = df.groupby('Gender')['Feedback'].value_counts(normalize=True).unstack()

feedback_counts_by_gender.plot(kind='bar', stacked=True)
plt.xlabel('Gender')
plt.ylabel('Count')
plt.title('Count of Positive and Negative Feedback by Gender')
plt.xticks(rotation=0)
plt.legend(title='Feedback', bbox_to_anchor=(1.05, 1), loc='upper right')
plt.show()
# There are a little bit more Negative feedback from Males

