from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'ASecretKey'

@app.route('/')
def home():
	if 'activities_text' in session:
		pass
	else:
		session['activities_text'] = ''
	if 'gold' in session:
		pass
	else:
		session['gold'] = 0
	return render_template('index.html', gold = session['gold'], activities_text = session['activities_text'])

@app.route('/process_money', methods=['POST'])
def process():
	if request.form['building']=='farm':
		temp = random.randrange(10,21)
		session['gold'] += temp
	if request.form['building']=='cave':
		temp = random.randrange(5,11)
		session['gold'] += temp
	if request.form['building']=='house':
		temp = random.randrange(2,6)
		session['gold'] += temp
	if request.form['building']=='casino':
		temp = random.randrange(-50,51)
		session['gold'] += temp
		if temp > 0:
			session['activities_text'] += '\nWon ' + str(temp) + ' gold at the casino!'
			return redirect('/')
		if temp < 0:
			session['activities_text'] += '\nLost ' + str(abs(temp)) + ' gold at the casino... Ouch.'
			return redirect('/')
		if temp == 0:
			session['activities_text'] += '\nBroke even at the casino.'
			return redirect('/')
	session['activities_text'] += '\nEarned ' + str(temp) + ' gold at the ' + request.form['building']
	return redirect('/')

@app.route('/reset')
def reset():
	session['gold'] = 0
	session['activities_text'] = 'Your gold was reset.'
	return redirect('/')
	
app.run(debug=True)

