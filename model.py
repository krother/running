
import pandas as pd
from sklearn.linear_model import LinearRegression


df = pd.read_csv('data.csv')

X = df[['distance [km]']]
y = df['time [min]']

m = LinearRegression(fit_intercept=False)
m.fit(X, y)

val_time = round(m.predict([[10.0]])[0], 2)
ham_time = round(m.predict([[21.1]])[0], 2)

print(f"Valentinslauf: {val_time} min")
print(f"Halfmarathon : {ham_time} min")
