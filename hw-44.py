# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()

import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
# с помощью get_dummies:
print(pd.get_dummies(data['whoAmI']))
print('-----------------------------------')
# с помощью цикла for и условий if:
print(' ', ' human', ' robot')
for i, value in enumerate(data['whoAmI']):
    if value == 'robot':
        print(f'{i}  {False}   {True}')        
    elif value == 'human':
        print(f'{i}  {True}   {False}')
