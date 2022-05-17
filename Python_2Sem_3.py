import pandas
import matplotlib.pyplot as plt
import seaborn

data = pandas.read_csv('practice.csv', index_col=0)

seaborn.barplot(x=data['week_number'], y=data['installs'])
plt.show()

seaborn.barplot(x=data['week_number'], y=data['ad_campaign'])
plt.show()

seaborn.barplot(x=data['week_number'], y=data['payments'])
plt.show()

conversions = [0] * 15
for vdl in range(len(data['payments'])):
  conversions[vdl] = data['payments'][vdl] / data['installs'][vdl]
print(conversions[vdl])
seaborn.barplot(x=conversions, y=data['week_number'])
plt.show()
