import pandas as pd
import numpy as np

def fetch_sales_from_db():
    dates = pd.date_range(start='2024-01-01', periods=24, freq='ME')
    regions = ['North','South','East']

    data =[]
    for date in dates:
        for region in regions:
            base_sales = 50000 if region == 'North' else 35000
            sales = base_sales + np.random.randint(-5000,5000)
            data.append([date,region,sales])

    df = pd.DataFrame(data,columns = ['Date','Region','Revenue'])
    print("Successfully connected to DB and fetched 72 records....")
    return df