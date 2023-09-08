import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
df = pd.DataFrame(lst, columns=['whoami'])
df.head()

# | В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша
# задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

# проще некуда, конечно. Такая интересная тема, и такие задания, ну прям совсем слабо

df.loc[df['whoami'] == 'robot', 'robot'] = 1
df.loc[df['whoami'] == 'human', 'human'] = 1

# либо так

df['robot'] = (df['whoami'] == 'robot').astype(int)
df['human'] = (df['whoami'] == 'human').astype(int)

# либо так

df['robot'] = df['whoami'].apply(lambda x: 1 if x == 'robot' else 0)
df['human'] = df['whoami'].apply(lambda x: 1 if x == 'human' else 0)

# либо создаем новый словарь

df_new = pd.DataFrame({
    'robot': [1 if who == 'robot' else 0 for who in df['whoami']],
    'human': [1 if who == 'human' else 0 for who in df['whoami']]
})

df.drop('whoami', axis=1, inplace=True)  # удаляем столбец whoami
