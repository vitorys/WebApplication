# -*- coding: utf-8 -*-
import argparse
import requests
import dill
import computers as pcs
from sklearn.metrics import accuracy_score


# Manda uma requisição para todas as máquinas para verificar
# disponibilidade

def checkGPUs():
	pcs_dict = pcs.computer

	for key in pcs_dict:
		ip = pcs_dict.get(key)
		print ip

		avaliable = requests.get(ip + 'gpu_usage').text
		
		if avaliable == '1':
			print "Requisitando máquina " + str(key)
			return ip

def main():
	ip = checkGPUs()
	train_characteristics = ''
	train_labels = ''

	test_characteristics = ''
	test_labels = ''
	
	with open('train_characteristics.txt', 'r') as characts:
		train_characteristics = characts.read()
		
	with open('train_labels.txt', 'r') as labels:
		train_labels = labels.read()

	with open('test_labels.txt', 'r') as testlabels:
		test_labels = testlabels.read()

	with open('test_characteristics.txt', 'r') as testcharacteristics:
		test_characteristics = testcharacteristics.read()

		test_labels = eval(test_labels)
		test_characteristics = eval(test_characteristics)

	payload = {'TrainCharacteristics': str(train_characteristics), 'TrainLabels' : str(train_labels), 'gamma': 0.0001, 'c':1 }
	
	r = requests.post(ip, data=payload)
	print r.content


if __name__ == '__main__':

	main()