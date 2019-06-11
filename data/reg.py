import numpy as np 
import json
from sklearn.linear_model import LinearRegression
import math
from scipy.stats import norm

def ln(x):
	return math.log(x)

year = ['2017', '2016', '2015', '2014']
tag = ['pop', 'urbanpop', 'emp', 'urbanemp', 'urbanarea', 'gdp', 'urbangdp', 'urbanl2', 'urbanl3', 'urbangdpr2', 'urbangdpr3', \
	'high', 's', 'urbans', 'trans']

data = json.load(open('data.json', 'r', encoding='utf8'))

tags = [[(str(y)+t, t) for t in tag] for y in year]

data_tmp = []

for city in data:
	for y in tags:
		flag = 1
		for t in y:
			if t[0] in data[city]:
				continue
			else:
				flag = 0

		if flag == 0:
			continue

		dic_tmp = {'name': city}
		for t in y:
			dic_tmp[t[1]] = data[city][t[0]]

		dic_tmp['attr'] = data[city]['attr']

		data_tmp.append(dic_tmp)

print(len(data_tmp))
n = len(data_tmp)

for i in data_tmp[50].keys():
	print({i: data_tmp[50][i]})

x = [[ \
	ln(i['s'] / i['pop']), \
	ln(i['urbanpop']), \
	(ln(i['urbanpop'])) ** 2, \
	#i['attr'] * ln(i['urbanpop']) * i['urbanl3'] / i['urbanl2'], \
	i['urbanl3'] / i['urbanl2'], \
	ln(i['urbanpop']) * i['urbanl3'] / i['urbanl2'], \
	ln(i['trans'] / i['pop']), \
	i['urbanemp'] / i['urbanpop'], \
	ln(i['high'] / i['urbanpop']), \
	ln(i['urbanarea'] / i['urbanpop'])
	] for i in data_tmp]

y = [ln(i['gdp'] / i['pop']) for i in data_tmp]

x = np.array(x)
y = np.array(y)

print(x.shape, y.shape)

reg = LinearRegression().fit(x, y)

print(reg.score(x, y))

print(reg.coef_)

x_mean = x.mean(0)

u = []
for i in range(x.shape[0]):
	yh = reg.intercept_
	for j in range(x.shape[1]):
		yh = yh + reg.coef_[j] * x[i][j]
	u.append(y[i] - yh)

u = np.array(u)
u2 = u ** 2

print('')

print(x_mean)
print(reg.predict([x_mean]))
print(y.mean())

print('')

for i in range(x.shape[1]):
	xi = np.array([x[j][i] for j in range(x.shape[0])])
	xi = xi - x_mean[i]
	xi2 = xi ** 2
	
	si = u2 * xi2

	#print(u2.mean())

	sei = si.sum() / (n - 2.0) / (xi2.sum() / n)

	b = reg.coef_[i] / sei
	if b < 0:
		p = norm.cdf(b, 0, 1)
	else:
		p = norm.sf(b, 0, 1)
	print('%.6f\t%.6f\t%.6f\t%.3f' % (reg.coef_[i], sei, b, p))

#for i in range(x.shape[0]):
#	print('%.6f\t%.6f\t%.6f' % (y[i], reg.predict([x[i]])[0], y[i] - reg.predict([x[i]])[0]))