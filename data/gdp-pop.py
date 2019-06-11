import json
import msgpack
import matplotlib.pyplot as plt
from scipy.optimize import leastsq
import numpy as np
import math

def func(p,x):
	k,b=p
	return k*x+b

def error(p,x,y):
	return func(p,x)-y

def func2(p,x):
	k1,b1=p
	return np.array([k1 * math.log(x[i] + 6.3) + b1 for i in range(x.shape[0])])

def error2(p,x,y):
	return func2(p,x)-y

data = json.load(open('data.json', 'r', encoding='utf8'))

tags = ['2017urbanpop', '2016urbanpop', '2017urbangdp', '2016urbangdp']

data_tmp = []

for city in data.keys():
	flag = 1
	for t in tags:
		if t in data[city]:
			continue
		else:
			flag = 0

	if flag > 0:
		tmp = [city] + [data[city][t] for t in tags]
		k = tmp[1] / tmp[2]
		if k > 1.25 or k < 0.7:
			continue

		k = tmp[3] / tmp[4]
		if k > 1.25 or k < 0.7:
			continue
		data_tmp.append(tmp)

print(sum([i[1] for i in data_tmp]), sum([i[2] for i in data_tmp]))
print(sum([i[3] for i in data_tmp]), sum([i[4] for i in data_tmp]))

ave_pop = (sum([i[1] for i in data_tmp]) / sum([i[2] for i in data_tmp]) - 1.0) * 100
ave_gdp = (sum([i[3] for i in data_tmp]) / sum([i[4] for i in data_tmp]) - 1.0) * 100

print(ave_gdp, ave_pop)
print(len(data_tmp))

data_tmp = [[i[0], (i[1]/i[2]-1.0)*100, (i[3]/i[4]-1.0)*100] for i in data_tmp]

print(min([i[1] for i in data_tmp]), min([i[2] for i in data_tmp]))

plt.axis([-8, 10, -10, 20])

plt.plot([-100, 100], [ave_gdp, ave_gdp], 'r:', linewidth=1)
plt.plot([ave_pop, ave_pop], [-100, 100], 'r:', linewidth=1)

k, b = leastsq(error, [-1, -100], args=(np.array([i[1] for i in data_tmp]), np.array([i[2] for i in data_tmp])))[0]

x = np.arange(-11, 11, 0.01)
plt.plot(x, k*x+b, 'b-', linewidth=1)

k, b = leastsq(error2, [1000, 1000], args=(np.array([i[1] for i in data_tmp]), np.array([i[2] for i in data_tmp])))[0]

x = np.arange(-6.29, 11, 0.01)
y = np.array([k * math.log(x[i] + 6.3) + b for i in range(x.shape[0])])
plt.plot(x, y, 'g-.', linewidth=1)

cc = []
for i in data_tmp:
	if data[i[0]]['loc'] == 1:
		cc.append(i[1])
	plt.plot(i[1], i[2], 'k.', linewidth=5)

plt.title('The Relation between the Change of GDP and Popu.')
plt.xlabel('The Increase of Population(%)')
plt.ylabel('The Increase of GDP(%)')

plt.savefig('gdp-pop.png')

plt.show()

print(sum(cc) / len(cc))
print(cc)

c = ['k', 'b', 'r', 'g']
l = ['(Coastal)', '(Middle)', '(West)', '(North-East)']

for j in range(1, 5):
	plt.plot([-100, 100], [ave_gdp, ave_gdp], 'k:', linewidth=1)
	plt.plot([ave_pop, ave_pop], [-100, 100], 'k:', linewidth=1)
	plt.plot([1.43715, 1.43715], [-100, 100], 'r:', linewidth=1)
	for i in data_tmp:
		k = data[i[0]]['loc']
		if k == j:
			plt.plot(i[1], i[2], c[j-1] + '.', linewidth=1)

	plt.axis([-8, 10, -10, 20])
	plt.title('The Relation between the Change of GDP and Popu.' + l[j-1])
	plt.xlabel('The Increase of Population(%)')
	plt.ylabel('The Increase of GDP(%)')

	plt.savefig('gdp-pop' + str(j+1) + '.png')

	plt.show()

plt.plot([-100, 100], [ave_gdp, ave_gdp], 'k:', linewidth=1)
plt.plot([ave_pop, ave_pop], [-100, 100], 'k:', linewidth=1)
for i in data_tmp:
	j = int(data[i[0]]['loc'])
	plt.plot(i[1], i[2], c[j-1] + '.', linewidth=1)

plt.axis([-8, 10, -10, 20])
plt.title('The Relation between the Change of GDP and Popu.(Total)')
plt.xlabel('The Increase of Population(%)')
plt.ylabel('The Increase of GDP(%)')

plt.savefig('gdp-pop' + '6' + '.png')

plt.show()

