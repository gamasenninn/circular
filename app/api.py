from app import app
from models import db,Member,Circular,CircularItem
from flask import jsonify,request
import json

@app.route('/')
def root():
    return "Hello World!"

@app.route('/r/members',methods=['GET'])
def get_members():
    return jsonify(
       [ member.to_dict() for member in Member.query.all()]
    )

@app.route('/r/member/<id>',methods=['GET'])
def get_member(id):
    row_count = Member.query.filter(Member.id==id).count()
    app.logger.info(row_count)
    if row_count:
        return  jsonify(Member.query.filter(Member.id==id).first().to_dict())
    else:
        return jsonify([])
    #return jsonify( Member.query.filter(Member.id==id).one().to_dict() )

@app.route('/r/member',methods=['POST'])
def create_member():
    d = request.json
    app.logger.info(d)
    newMember = Member(
        name = d['name'],
        category = d['category'],
        telNumber = d['telNumber'],
        memo = d['memo'],
        email = d['email'],
    )
    db.session.add(newMember)
    db.session.commit()
    id = newMember.id

    return jsonify({"result": "OK", "id": id, "data": d})

@app.route('/r/member/<id>',methods=['PUT'])
def update_member(id):
    d = request.json
    app.logger.info(d)
    member = Member.query.filter(Member.id==id).one()

    member.name = d['name']
    member.category = d['category']
    member.telNumber = d['telNumber']
    member.memo = d['memo']
    member.email = d['email']

    db.session.commit()

    return jsonify({"result": "OK", "id": id, "data": d})

@app.route('/r/member/<id>',methods=['DELETE'])
def delete_member(id):
    #d = request.json
    #app.logger.info(d)
    member = Member.query.filter(Member.id==id).delete()
    db.session.commit()

    return jsonify({"result": "OK", "id": id, "data": ''})



if __name__ == '__main__':

    app.run(host='0.0.0.0',port=5010)
