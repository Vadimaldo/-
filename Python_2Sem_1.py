import pandas
import seaborn
data = pandas.read_csv('practice.csv', index_column = 'Список адресов')
data ['Неделя 14'] = data ['Неделя 14'] * 100
seaborn.heatmap(data)
