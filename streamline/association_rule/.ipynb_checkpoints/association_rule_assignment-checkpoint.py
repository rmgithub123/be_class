import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

def distribution_plot(x,y,name=None,xaxis=None,yaxis=None):
    fig = go.Figure([
        go.Bar(x=x, y=y)
    ])

    fig.update_layout(
        title_text=name,
        xaxis_title=xaxis,
        yaxis_title=yaxis
    )
    fig.show()

def encode_units(x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1
# Create a title and description
st.title("Association Rule Assignment")
st.write("Upload a CSV file to check the data types of its columns.")

# File upload
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])
#uploaded_file = 1

if uploaded_file is not None:
    # Read CSV file into a DataFrame
    df = pd.read_csv(uploaded_file)
    #df = pd.read_csv("/home/madhuri/Downloads/online_retail/Online_Retail.csv")
        # Display DataFrame
    st.write("Preview of the uploaded data:")
    st.write(df.head())

    # Get column data types
    data_types = df.dtypes

    # Display column data types
    st.write("Data types of columns:")
    st.write(data_types)

    all_products = df['Description'].unique()

    x = df['Description'].value_counts()
    x = x.sort_values(ascending = False)
    x = x[0:10]
    x
    #st.write(x)
    distribution_plot(x=x.index, y= x.values,yaxis='Count',xaxis="Products")

    df['Description'] = df['Description'].str.strip()

    #df 

    df.dropna(axis=0, subset=['InvoiceNo'], inplace=True)

    df['InvoiceNo'] = df['InvoiceNo'].astype('str')

    df = df[~df['InvoiceNo'].str.contains('C')]
    
    df

    basket = (df[df['Country'] =="France"]
          .groupby(['InvoiceNo', 'Description'])['Quantity']
          .sum().unstack().reset_index().fillna(0)
          .set_index('InvoiceNo'))
    st.write("Basket Data Before Encoding")
    basket
    st.write("Encoding: Replace value < 0 to ) and >1 to 1")
    basket_sets = basket.applymap(encode_units)
    basket_sets.drop('POSTAGE', inplace=True, axis=1)
    basket_sets

    frequent_itemsets = apriori(basket_sets, min_support=0.07, use_colnames=True)
    st.write("Applly apriori algorithm with min_support 0.07")
    st.write(frequent_itemsets)

    st.write("Apply association rules with min_threshold 1")
    rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
    st.write(rules.head())

    st.write("Sort value and display top 10 Items having lift value >=6 and confidence >=0.8")
    rules.sort_values('lift',ascending=False)
    st.write(rules[ (rules['lift'] >= 6) & (rules['confidence'] >= 0.8) ][0:10])





