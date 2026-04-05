import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

base_path = "/Users/chan050714/f1_simulation"

results_path = os.path.join(base_path, 'results.csv')
races_path = os.path.join(base_path, 'races.csv')
qualifying_path = os.path.join(base_path, 'qualifying.csv')

try:
    results = pd.read_csv(results_path)
    races = pd.read_csv(races_path)
    qualifying = pd.read_csv(qualifying_path)
except FileNotFoundError as e:
    print(f"❌ 파일을 찾을 수 없습니다. 경로를 다시 확인해주세요: {e}")
    exit()

df_results = results[['raceId', 'driverId', 'constructorId', 'grid', 'positionOrder']]

df_races = races[['raceId', 'year', 'circuitId']]

df = pd.merge(df_results, df_races, on='raceId', how='left')

df = df[df['year'] >= 2010].dropna()

X = df[['grid', 'driverId', 'constructorId', 'circuitId', 'year']]
y = df['positionOrder']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)
print(f"(평균적으로 실제 등수와 약 {mae:.2f}등 정도 차이\n")

sample_race = pd.DataFrame({
    'grid': [3],             
    'driverId': [1],          
    'constructorId': [131],    
    'circuitId': [14],        
    'year': [2024]             
})

predicted_position = model.predict(sample_race)[0]
print(f"▶ 예상 최종 순위: [{predicted_position:.1f}위]")
