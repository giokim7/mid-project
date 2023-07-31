#!/usr/bin/env python
# coding: utf-8

# In[1]:


def create_scatterplot(x, y):
    #scatterplot
    df.plot.scatter(x=x, y=y)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(x + ' vs ' + y)
    plt.show()


# In[2]:


def create_collinearity(x, y):
    plt.figure(figsize=(10, 8))
    subset_df = df[[x, y]]
    correlation_matrix = subset_df.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
    plt.title("Correlation Heatmap")
    plt.show()


# In[ ]:




