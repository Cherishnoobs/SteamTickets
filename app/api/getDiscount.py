from flask import Flask
from flask.views import MethodView
from  flask import jsonify, request
from app.sql.Redis import myRedis
from main import app


class DiscountAPI(MethodView):
    def get(self):
        if request.args.get('page') is None:
            return jsonify({
            "code": 200,
            "kind": "ALL",
            "msg": "OK",
            "data": myRedis.findAll()
            })
        else:
            page = int(request.args.get('page'))
            return jsonify({
            "code": 200,
            "kind": "page"+ str(page),
            "msg": "OK",
            "data": myRedis.findMany((page-1)*12)
            })

