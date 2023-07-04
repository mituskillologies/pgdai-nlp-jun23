from flask import Flask, request, redirect, url_for
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
   return 'Welcome %s! to Tushar`s computer.' %name
     
@app.route('/login', methods=['GET','POST'])
def login():
	if request.method == 'POST':
	   	user = request.form['nm']
	   	f = open('data.txt','a')
	   	f.write(user+'\n')
	   	f.close()
   		return redirect(url_for('success', name=user))

if __name__ == '__main__':
   app.run(host='192.168.76.137', debug=True)
