# -*- coding: utf-8 -*-

import requests
import dill
import computers as pcs

# Manda uma requisição para todas as máquinas para verificar
# disponibilidade

def checkGPUs():
	pcs_dict = pcs.computer

	for key in pcs_dict:
		ip = pcs_dict.get(key)

		avaliable = requests.get(ip + 'gpu_usage').text
		
		if avaliable == '1':
			return ip

def main():
	ip = checkGPUs()
	#ip = 'http://localhost:8080/' 
	tc = ''
	tl = ''
	
	with open('train_characteristics_test.txt', 'r') as characts:
		tc = characts.read()
		
	with open('train_labels_test.txt', 'r') as labels:
		tl = labels.read()

	payload = {'TrainCharacteristics': str(tc), 'TrainLabels' : str(tl), 'gamma': 0.0001, 'c':1 }
	
	r = requests.post(ip, data=payload)
	
	clf = dill.loads(r.text)


if __name__ == '__main__':
	main()