import pandas as pd

file = 'california_housing_train.csv'

df = pd.read_csv(file)

# Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population)

mean_price = df.loc[df['population'] <= 500]['median_house_value'].mean()

# Узнать какая максимальная households в зоне минимального значения population.
# Минимальное значение популяции - меньше или равно 25%, или 790 человек. Узнать можно так
# df['population'].describe()


max_households = df.loc[df['population'] <= 790]['households'].max()

# для более красивой статистики можно так

new_df = df.loc[df['population'] <= 790]
new_df['households'].describe()
