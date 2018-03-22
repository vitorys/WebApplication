import web
from web import form
from sklearn import svm
import dill

render = web.template.render('templates/')

urls = ('/', 'index')
app = web.application(urls, globals())

myform = form.Form( 
	form.Textbox("TrainCharacteristcs"), 
	form.Textbox("TrainLabels"),
	form.Textbox("gamma"),
	form.Textbox("c"))

class index: 
	def GET(self): 
		form = myform()
		return render.formtest(form)

	def POST(self): 
		form = myform() 
		if not form.validates(): 
			return render.formtest(form)
		else:
			
			train_characteristics = eval(form['TrainCharacteristcs'].value)
			train_labels = eval(form['TrainLabels'].value)
			
			gamma = float(form['gamma'].value)
			c = float(form['c'].value)
			
			classifier = Classifier()

			return classifier.svm_classifier(train_characteristics, train_labels, gamma, c)
			
class Classifier:
	def svm_classifier(self, train_characteristics, train_labels, gamma, c):
		
		clf = svm.SVC(gamma=gamma, C=c, kernel='rbf')
		clf.fit(train_characteristics, train_labels)
		
		return dill.dumps(clf)

if __name__=="__main__":
	web.internalerror = web.debugerror
	app.run()