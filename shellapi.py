import os
from flask import Flask, jsonify, request


from flask_cors import CORS
 
 
app = Flask(__name__)
CORS(app)

@app.route('/name', methods=['POST'])
def method():


   templatename = request.args.get('templatename')
   resource_group_name =request.args.get('resource_group_name')
   os.system('/bin/bash --rcfile sh shell.sh '+ str(resource_group_name) + ' ' + str(templatename))
   return (
     '{\n'
     '   "status" : 200 \n'
     '}\n'
   )

if __name__=='__main__':   
    app.run(port=9000, host='0.0.0.0')