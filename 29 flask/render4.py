from flask import Flask, render_template
app = Flask(__name__)

@app.route('/result')
def result():
	data = {'phy':67, 'chem':78, 'maths':59}
	return render_template('result1.html', result=data)

if __name__ == '__main__':
   app.run(debug = True)
