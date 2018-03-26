# -*- coding: utf-8 -*-

import web
from web import form
from sklearn import svm
import dill

render = web.template.render('templates/')

urls = ('/', 'index','/gpu_usage', 'gpu')
app = web.application(urls, globals())
myform = form.Form( 
	form.Textbox("TrainCharacteristics"), 
	form.Textbox("TrainLabels"),
	form.Textbox("gamma"),
	form.Textbox("c"))

class gpu:
	def GET(self):
		return self.verifyGPUUsage()

	def verifyGPUUsage(self):
		# A ser implementado

		# Retorna 1 se a máquina estiver ociosa
		# Retorna 0 se a máquina estiver sendo utilizada
		return 1


class index: 
	def GET(self): 
		form = myform()
		return render.formtest(form)

	def POST(self): 
		form = myform()

		if not form.validates():
			return render.register(f)

		else:
			train_characteristics = eval(form['TrainCharacteristics'].value)
			train_labels = eval(form['TrainLabels'].value)
			
			gamma = float(form['gamma'].value)
			c = float(form['c'].value)
			
			classifier = Classifier()
			f_ = classifier.svm_classifier(train_characteristics, train_labels, gamma, c)
			return f_
			
class Classifier:
	def svm_classifier(self, train_characteristics, train_labels, gamma, c):
		
		clf = svm.SVC(gamma=gamma, C=c, kernel='rbf')
		clf.fit(train_characteristics, train_labels)
		f_ = dill.dumps(clf)
		print type(f_)
		return f_

if __name__=="__main__":
	web.internalerror = web.debugerror
	app.run()