from flask import Flask, render_template
#from tabulate import tabulate
app = Flask(__name__)
@app.route("/")
def index():
  return render_template('add_user.html')
app.run(debug=True,host='0.0.0.0', port=8000)