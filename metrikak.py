import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import r2_score, mean_squared_error


np.random.seed(42)
n_samples = 150
azalera = np.random.uniform(40, 200, n_samples)
prezioa = azalera * np.random.uniform(1500, 3500, n_samples)

logelak = np.round(azalera / 40 + np.random.normal(0, 0.5, n_samples))
logelak = np.clip(logelak, 1, 5).astype(int)

df = pd.DataFrame({'Prezioa': prezioa, 'Azalera': azalera, 'Logelak': logelak})

X = df[['Prezioa', 'Azalera']].values
y = df['Logelak'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

emaitzak = []
for k in range(1, 7):
    knn = KNeighborsRegressor(n_neighbors=k)
    knn.fit(X_train_scaled, y_train)
    

    y_train_pred = knn.predict(X_train_scaled)
    y_test_pred = knn.predict(X_test_scaled)
    
 
    r2_train = r2_score(y_train, y_train_pred)
    r2_test = r2_score(y_test, y_test_pred)
    mse_train = mean_squared_error(y_train, y_train_pred)
    mse_test = mean_squared_error(y_test, y_test_pred)
    
    emaitzak.append({
        'K': k,
        'R2 Train': r2_train,
        'R2 Test': r2_test,
        'MSE Train': mse_train,
        'MSE Test': mse_test
    })


emaitzen_df = pd.DataFrame(emaitzak)
print(emaitzen_df.to_string(index=False))
