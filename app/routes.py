from flask import Flask , render_template , request
 
app = Flask(__name__)      
 
@app.route('/')
def home():
	return "hello world!!!"
  #return render_template('home.html')

@app.route('/add/<int:num1>/<int:num2>')
def add(num1,num2):
	return '{}+{}={}'.format(num1,num2,num1+num2)

@app.route('/mult/<int:num1>/<int:num2>')
def mult(num1,num2):
	return '{}*{}={}'.format(num1,num2,num1*num2)


@app.route('/input') 
def fill_form():
	return render_template('my_form.html')

@app.route('/input',methods=['POST'])
def conv_upper():
	return request.form['text'].upper()

if __name__ == '__main__':
  app.run(host='0.0.0.0')