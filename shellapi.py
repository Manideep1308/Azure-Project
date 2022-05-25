import os
from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route('/name', methods=['POST'])
def method():


   templatename = request.args.get('templatename')
   resource_group_name =request.args.get('resource_group_name')
   os.system('/bin/bash --rcfile sh shell.sh '+ str(resource_group_name) + ' ' + str(templatename))
   return 'do deployement'

if __name__=='__main__':   
    app.run(port=9000, host='0.0.0.0')