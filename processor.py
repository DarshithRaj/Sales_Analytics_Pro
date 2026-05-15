from database import fetch_sales_from_db
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import pandas as pd

def prepare_and_train():
    df = fetch_sales_from_db()
    df = df.sort_values(['Region','Date'])
    df['Last_Month_Sales']=df.groupby('Region')['Revenue'].shift(1)
    df['3_Month_Trend']=df.groupby('Region')['Revenue'].transform(lambda x: x.rolling(window=3).mean())
    df=df.dropna()

    X=df[['Last_Month_Sales','3_Month_Trend']]
    y=df['Revenue']

    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,shuffle=False)
    model = RandomForestRegressor(n_estimators=100,random_state=42)
    model.fit(X_train,y_train)

    accuracy = model.score(X_test,y_test)
    print(f"---Processing Complete---")
    print(f"Model Accuracy (R2 Score):{accuracy:.2f}")

    return model,df
if __name__=="__main__":
    prepare_and_train()