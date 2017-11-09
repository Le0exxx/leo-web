from flask import render_template, request, flash, redirect, url_for
from app import app
from pypresto import PrestoConnection

host = 'http://labs-puck-prestocoordinator-lv-101.labs.marinsw.net'
user = 'lli'
catalog = 'hive'
port = '8080'
schema = 'func03'

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title='Home')

@app.route('/query', methods=['POST'])
def query():
    if request.form['query']:
        #flash('Query is: %s' % request.form['query'])
            conn = PrestoConnection(host, user, catalog, port, schema)
            result = conn.run_query(request.form['query'])
            flash('Result: %s' % result)
        #except:
        #    flash('Query failed with error: %s', result)
            return redirect(url_for('index'))
