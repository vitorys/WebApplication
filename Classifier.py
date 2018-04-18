# -*- coding: utf-8 -*-

# Classe responsável pelos métodos de classificação
from sklearn import svm
import dill


class Classifier:
	# Método responsável por treinar modelo
	def svm_classifier(self, train_characteristics, train_labels, gamma, c):
		clf = svm.SVC(gamma=gamma, C=c, kernel='rbf')
		clf.fit(train_characteristics, train_labels)
		f_ = dill.dumps(clf)
		return f_

	# Método para realizar o predict
	def predict(self, clfDumped, test_characteristics):
		clf = clfDumped
		clf.predict(test_characteristics)
		return clf