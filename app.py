from flask import Flask, render_template, jsonify

#Object class of the Flask
app = Flask(__name__) 

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Pune, India',
    'salary': '10 LPA'
  },
  {
    'id': 2,
    'title': 'DevOps Engineer',
    'location': 'Banglore, India',
    'salary': '12 LPA'
  },
  {
    'id': 3,
    'title': 'Frontend Developer',
    'location': 'Delhi, India',
    'salary': '5 LPA'
  },
  {
    'id': 4,
    'title': 'Backend Developer',
    'location': 'Hydrabad, India',
    'salary': '8 LPA'
  },
  {
    'id': 5,
    'title': 'FullStack Developer',
    'location': 'Gurgaon, India'
  }
]
@app.route('/')
def hello_world():
  return render_template('home.html', jobs=JOBS)

@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(debug=True)

