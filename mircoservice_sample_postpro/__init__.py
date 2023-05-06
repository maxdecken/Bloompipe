import os
from flask import Flask, jsonify, request
import PostPro
import json

# for server deploy change to:  from main.common
from datetime import datetime


app = Flask(__name__)


@app.route('/api/postpro/getvideo', methods=['POST', 'GET'])
def getVideo():
    print("Hallo")
    if request.method == 'POST':
        input = request.json
        PostPro.convertImgSeqToH264(input["inPath"], input["outPath"], input["frameRate"])
        return "STATUS - VIDEO CONVERTED"



if __name__ == "__main__":
    app.run()
