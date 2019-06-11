import json
import msgpack
import matplotlib.pyplot

name = []
name = name + [['2017pop', [(2, '2017pop', 1.0), (3, '2017urbanpop', 1.0), (6, '2017dpop', 0.1), (7, '2017dupop', 0.1)]]]
name = name + [['2017lab', [(2, '2017emp', 1e-4), (3, '2017urbanemp', 1e-4), (6, '2017unemp', 1e-4), (7, '2017urbanunemp', 1e-4)]]]
name = name + [['2017area', [(2, '2017urbanarea', 1.0), (3, '2017living', 1.0), (4, '2017urbanratio', 1.0)]]]
name = name + [['2017gdp', [(2, '2017gdp', 1.0), (3, '2017urbangdp', 1.0)]]]
name = name + [['2017gdpr', [(2, '2017gdpr1', 1.0), (3, '2017urbangdpr1', 1.0), \
	(4, '2017gdpr2', 1.0), (5, '2017urbangdpr2', 1.0), (6, '2017gdpr3', 1.0), (7, '2017urbangdpr3', 1.0)]]]
name = name + [['2017univ', [(2, '2017high', 1e-4), (4, '2017sec', 1e-4)]]]
name = name + [['2017fin', [(2, '2017s', 1.0), (4, '2017urbans', 1.0)]]]
name = name + [['2017tra', [(2, '2017trans', 1.0)]]]
name = name + [['2017labr', [(2, '2017l1', 1.0), (3, '2017urbanl1', 1.0), \
	(4, '2017l2', 1.0), (5, '2017urbanl2', 1.0), \
	(6, '2017l3', 1.0), (7, '2017urbanl3', 1.0)]]]

name = name + [['2016pop', [(2, '2016pop', 1.0), (3, '2016urbanpop', 1.0), (6, '2016dpop', 0.1), (7, '2016dupop', 0.1)]]]
name = name + [['2016lab', [(2, '2016emp', 1e-4), (3, '2016urbanemp', 1e-4), (6, '2016unemp', 1e-4), (7, '2016urbanunemp', 1e-4)]]]
name = name + [['2016area', [(2, '2016urbanarea', 1.0), (3, '2016living', 1.0), (4, '2016urbanratio', 1.0)]]]
name = name + [['2016gdp', [(2, '2016gdp', 1.0), (3, '2016urbangdp', 1.0)]]]
name = name + [['2016gdpr', [(2, '2016gdpr1', 1.0), (3, '2016urbangdpr1', 1.0), \
	(4, '2016gdpr2', 1.0), (5, '2016urbangdpr2', 1.0), (6, '2016gdpr3', 1.0), (7, '2016urbangdpr3', 1.0)]]]
name = name + [['2016univ', [(2, '2016high', 1e-4), (4, '2016sec', 1e-4)]]]
name = name + [['2016fin', [(2, '2016s', 1.0), (4, '2016urbans', 1.0)]]]
name = name + [['2016tra', [(2, '2016trans', 1.0)]]]
name = name + [['2016labr', [(2, '2016l1', 1.0), (3, '2016urbanl1', 1.0), \
	(4, '2016l2', 1.0), (5, '2016urbanl2', 1.0), \
	(6, '2016l3', 1.0), (7, '2016urbanl3', 1.0)]]]

name = name + [['2015pop', [(2, '2015pop', 1.0), (3, '2015urbanpop', 1.0), (6, '2015dpop', 0.1), (7, '2015dupop', 0.1)]]]
name = name + [['2015lab', [(2, '2015emp', 1e-4), (3, '2015urbanemp', 1e-4), (6, '2015unemp', 1e-4), (7, '2015urbanunemp', 1e-4)]]]
name = name + [['2015area', [(2, '2015urbanarea', 1.0), (3, '2015living', 1.0), (4, '2015urbanratio', 1.0)]]]
name = name + [['2015gdp', [(2, '2015gdp', 1.0), (3, '2015urbangdp', 1.0)]]]
name = name + [['2015gdpr', [(2, '2015gdpr1', 1.0), (3, '2015urbangdpr1', 1.0), \
	(4, '2015gdpr2', 1.0), (5, '2015urbangdpr2', 1.0), (6, '2015gdpr3', 1.0), (7, '2015urbangdpr3', 1.0)]]]
name = name + [['2015univ', [(2, '2015high', 1e-4), (4, '2015sec', 1e-4)]]]
name = name + [['2015fin', [(2, '2015s', 1.0), (4, '2015urbans', 1.0)]]]
name = name + [['2015tra', [(2, '2015trans', 1.0)]]]
name = name + [['2015labr', [(2, '2015l1', 1.0), (3, '2015urbanl1', 1.0), \
	(4, '2015l2', 1.0), (5, '2015urbanl2', 1.0), \
	(6, '2015l3', 1.0), (7, '2015urbanl3', 1.0)]]]

name = name + [['2014pop', [(2, '2014pop', 1.0), (3, '2014urbanpop', 1.0), (6, '2014dpop', 0.1), (7, '2014dupop', 0.1)]]]
name = name + [['2014lab', [(2, '2014emp', 1e-4), (3, '2014urbanemp', 1e-4), (6, '2014unemp', 1e-4), (7, '2014urbanunemp', 1e-4)]]]
name = name + [['2014area', [(2, '2014urbanarea', 1.0), (3, '2014living', 1.0), (4, '2014urbanratio', 1.0)]]]
name = name + [['2014gdp', [(2, '2014gdp', 1.0), (3, '2014urbangdp', 1.0)]]]
name = name + [['2014gdpr', [(2, '2014gdpr1', 1.0), (3, '2014urbangdpr1', 1.0), \
	(4, '2014gdpr2', 1.0), (5, '2014urbangdpr2', 1.0), (6, '2014gdpr3', 1.0), (7, '2014urbangdpr3', 1.0)]]]
name = name + [['2014univ', [(2, '2014high', 1e-4), (4, '2014sec', 1e-4)]]]
name = name + [['2014fin', [(2, '2014s', 1.0), (4, '2014urbans', 1.0)]]]
name = name + [['2014tra', [(2, '2014trans', 1.0)]]]

print(name)

data = {}
prov = ''
eprov = ''

for tag in name:
	filename = tag[0] + '.csv'
	with open(filename, 'r', encoding='utf8') as f:
		flines = f.readlines()

	for lid in range(len(flines)):
		ldata = flines[lid].split(',')
		if ldata[0][0] == ' ':
			city = ldata[1].strip() + r'-' + eprov
			if (city in data) is False:
				data[city] = {}
				data[city]['name'] = ldata[0].strip() + '-' + prov

			for j in range(len(tag[1])):
				try:
					data[city][tag[1][j][1]] = float(ldata[tag[1][j][0]]) * tag[1][j][2]
				except ValueError:
					continue

		else:
			prov = ldata[0].strip()
			eprov = ldata[1].strip()
			if len(ldata[2]) < 1:
				continue

			city = ldata[1].strip() + r'-' + eprov
			if (city in data) is False:
				data[city] = {}
				data[city]['name'] = ldata[0].strip() + '-' + prov

			for j in range(len(tag[1])):
				try:
					data[city][tag[1][j][1]] = float(ldata[tag[1][j][0]]) * tag[1][j][2]
				except ValueError:
					continue

with open('policy.csv', 'r', encoding='utf8') as f:
	ff = f.readlines()
	for i in ff:
		j = i.split(',')
		data[j[0].strip()]['attr'] = float(j[1])
		data[j[0].strip()]['loc'] = float(j[2])

for i in data.keys():
	print(i)

json.dump(data, open('data.json', 'w', encoding='utf8'), indent=1)