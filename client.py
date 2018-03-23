# -*- coding: utf-8 -*-

import requests
import dill

def main():
	
	tc = ''
	tl = ''
	
	with open('train_characteristics_test.txt', 'r') as characts:
		tc = characts.read()
		print tc

	with open('train_labels_test.txt', 'r') as labels:
		tl = labels.read()

	payload = {'TrainCharacteristcs': str(tc), 'TrainLabels' : str(tl), 'gamma': 0.0001, 'c':1 }

	r = requests.post("http://localhost:8080", data=payload)

	clf = dill.loads(r.text)


if __name__ == '__main__':
	main()