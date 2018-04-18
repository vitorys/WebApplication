# -*- coding: utf-8 -*-

import web
from web import form
import dill
import tempfile
from Classifier import Classifier

render = web.template.render('templates/')

urls = ('/', 'Index','/gpu_usage', 'Gpu', '/train', 'Train')
app = web.application(urls, globals())

indexForm = form.Form( 
	form.Textbox("TrainCharacteristics"), 
	form.Textbox("TrainLabels"),
	form.Textbox("gamma"),
	form.Textbox("c"))


predictForm = form.Form( 
	form.Textbox("TestCharacteristics"),
	form.Textbox("Model_ID"))


class Train:
	def GET(self):
		form = predictForm()
		return render.formtest(form)


	def POST(self):
		form = predictForm()

		if not form.validates():
			return render.register(f)

		else:
			test_characteristics = eval(form['TestCharacteristics'].value)
			Model_ID = str(form['Model_ID'].value)

			model_path = './models/' + Model_ID
			print model_path
			
			tmp_model = open(model_path, 'r')
			content_tmp_model = tmp_model.read()
			
			model = dill.loads(content_tmp_model)
			return model

			classifier = Classifier()

			# Realiza o predict e retorna o resultado
			return classifier.predict(model, test_characteristics)


class Gpu:
	def GET(self):
		return 1

class Index:
		
	def GET(self): 
		form = indexForm()
		return render.formtest(form)

	# Realiza o treinamento e armazena o modelo em uma lista -> Retorna o ID da máquina
	def POST(self): 
		form = indexForm()

		if not form.validates():
			return render.register(f)

		else:
			train_characteristics = eval(form['TrainCharacteristics'].value)
			train_labels = eval(form['TrainLabels'].value)
			
			gamma = float(form['gamma'].value)
			c = float(form['c'].value)
			
			classifier = Classifier()
			f_ = classifier.svm_classifier(train_characteristics, train_labels, gamma, c)
			
			tmp_file = tempfile.NamedTemporaryFile(dir='./models/', delete=False)
			tmp_file.write( str(f_) )
			tmp_file.close()
			# Separação do caminho absoluto por /
			file_name = tmp_file.name.split('/')
			# Retorna somente o nome
			return file_name[len(file_name)-1]

if __name__=="__main__":
	#web.internalerror = web.debugerror
	app.run()