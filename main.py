from flask import Flask, render_template
from flask import url_for, escape, abort
from flask import jsonify
from flask_cors import CORS
from app.sql.Mongo import myMongo
from app.sql.Redis import myRedis
from flask import request
import base64
app = Flask(__name__)
CORS(app)

app.config['JSON_AS_ASCII'] =False
@app.route('/')
@app.route('/index')
def index():
    if request.args.get('page') is None:
        data = myRedis.findMany(12*(1-1)+0)
    else:
        page = int(request.args.get('page'))
        data = myRedis.findMany(12*(page-1)+0)
    return render_template('index.html',data=data)


@app.route('/info/api/v1.0/', methods=['GET'])
def get_api():
    return jsonify({
        "discounts": "http://[hostname]/info/api/v1.0/discounts",
        "tickets": "http://[hostname]/info/api/v1.0/tickets",
        # "ticket": "http://[hostname]/info/api/v1.0/tickets?id="
    })

@app.route('/info/api/v1.0/discounts', methods=['GET'])
def get_discounts():
    # return jsonify(myRedis.findOne(0))
    page = int(request.args.get('page'))
    return jsonify({
        "code": 200,
        "page": str(page),
        "msg": "OK",
        "data": myRedis.findMany(12*(page-1)+0)
    })

@app.route('/info/api/v1.0/tickets', methods=['GET'])
def get_tickets():
    if request.args.get('page') is None:
        data = []
        items = myMongo.findAll("games")
        for item in items:
            data.append({
                 "id":item["id"],
                "info":item["info"],
                "img": str(base64.b64encode(item["img"])),
                "download": item["download"]
            })
        return jsonify({
            "code": 200,
            "kind": 'ALL',
            "msg": "OK",
            "data": data
        })
    else:
        page = int(request.args.get('page'))
        data = []
        items = myMongo.findMany("games",page)
        for item in items:
            data.append({
                 "id":item["id"],
                "info":item["info"],
                "img": str(base64.b64encode(item["img"])),
                "download": item["download"]
            })
        return jsonify({
            "code": 200,
            "kind": 'Page'+str(page),
            "msg": "OK",
            "data": data
        })
    




if __name__=="__main__":
    app.run(debug=True)