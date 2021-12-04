from typing import ItemsView
from app import app,ma
from models import db,Member,Circular,CircularItem
from models import  MemberSchema,CircularSchema,CircularItemSchema
from flask import jsonify,request
import json
import datetime


@app.route('/r/members',methods=['GET'])
def get_members():
    members = Member.query.all()
    return jsonify(MemberSchema(many=True).dump(members))

@app.route('/r/member/<id>',methods=['GET'])
def get_member(id):
    row_count = Member.query.filter(Member.id==id).count()
    app.logger.info(row_count)
    if row_count:
        member = Member.query.filter(Member.id==id).first()
        return  jsonify(MemberSchema().dump(member))
    else:
        return jsonify([])

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
    member = Member.query.filter(Member.id==id).delete()
    db.session.commit()

    return jsonify({"result": "OK", "id": id, "data": ''})

@app.route('/r/circulars',methods=['GET'])
def get_circulars():
    circulars = Circular.query.all()
    return jsonify(CircularSchema(many=True).dump(circulars))

@app.route('/r/circular/<id>',methods=['GET'])
def get_circular(id):
    row_count = Circular.query.filter(Circular.id==id).count()
    #app.logger.info(row_count)
    if row_count:
        circular = Circular.query.filter(Circular.id==id).first()
        return  jsonify(CircularSchema().dump(circular))
    else:
        return jsonify([])

@app.route('/r/circular',methods=['POST'])
def create_circular():
    d = request.json
    app.logger.info(d)

    if d.get('items'):
        circularItems = [
            CircularItem(
                memberId = item.get('memberId'),
                person = item.get('person'),
                departmentId = item.get('departmentId'),
                confirm = item.get('confirm'),
                memo = item.get('memo'),
            )
            for item in d.get('items')
        ]
        #print("items:",items)
    else:
        circularItems = []

    newCircular = Circular(
        title = d.get('title'),
        detail = d.get('detail'),
        dueDate = datetime.datetime.strptime(d.get('dueDate'), "%Y-%m-%d") if d.get('dueDate') else None,
        items = circularItems,
    )

    db.session.add(newCircular)
    db.session.commit()
    id = newCircular.id

    return jsonify({"result": "OK", "id": id, "data": d})

@app.route('/r/circular/<id>',methods=['PUT'])
def update_circular(id):
    d = request.json
    app.logger.info(d)

    circular  = Circular.query.filter(Circular.id==id).first()
    if not circular:
        return jsonify({"result": "No Data", "id": id, "data": d})

    circular.title = d.get('title')
    circular.detail = d.get('detail')
    circular.dueDate = datetime.datetime.strptime(d.get('dueDate'), "%Y-%m-%d") if d.get('dueDate') else None

    db.session.commit()
    #id = newCircular.id

    return jsonify({"result": "OK", "id": id, "data": d})

@app.route('/r/circular/<id>',methods=['DELETE'])
def delete_circular(id):
    circular = Circular.query.filter(Circular.id==id).first()
    db.session.delete(circular)
    db.session.commit()

    return jsonify({"result": "OK", "id": id, "data": ''})

@app.route('/r/circular-items',methods=['GET'])
def get_circular_items():
    circularItems = CircularItem.query.all()
    return jsonify(CircularItemSchema(many=True).dump(circularItems))

@app.route('/r/circular-items/<hid>',methods=['GET'])
def get_circular_items_by_key(hid):
    circularItems = CircularItem.query.filter(CircularItem.circularId==hid).all()
    return jsonify(CircularItemSchema(many=True).dump(circularItems))

@app.route('/r/circular-item/<id>',methods=['GET'])
def get_circular_item(id):
    circularItem = CircularItem.query.filter(CircularItem.id==id).first()
    return jsonify(CircularItemSchema().dump(circularItem))

@app.route('/r/circular-item',methods=['POST'])
def create_circular_item():
    d = request.json
    app.logger.info(d)

    circularItem = CircularItem(
        memberId = d.get('memberId'),
        person = d.get('person'),
        departmentId = d.get('departmentId'),
        confirm = d.get('confirm'),
        memo = d.get('memo')
    )
    db.session.add(circularItem)
    db.session.commit()
    id = circularItem.id

    return jsonify({"result": "OK", "id": id, "data": d})


@app.route('/r/circular-item/<id>',methods=['PUT'])
def update_circular_item(id):
    d = request.json
    app.logger.info(d)

    circularItem  = CircularItem.query.filter(CircularItem.id==id).first()
    if not circularItem:
        return jsonify({"result": "No Data", "id": id, "data": d})

    circularItem.memberId = d.get('memberId')
    circularItem.person = d.get('person')
    circularItem.departmentId = d.get('departmentId')
    circularItem.confirm = d.get('confirm')
    circularItem.memo = d.get('memo')

    db.session.commit()
    #id = newCircular.id

    return jsonify({"result": "OK", "id": id, "data": d})

@app.route('/r/circular-item/<id>',methods=['DELETE'])
def delete_circular_item(id):
   
    circularItem  = CircularItem.query.filter(CircularItem.id==id).first()
    if not circularItem:
        return jsonify({"result": "No Data", "id": id, "data": ''})

    db.session.delete(circularItem)
    db.session.commit()

    return jsonify({"result": "OK", "id": id, "data": ''})


if __name__ == '__main__':

    app.run(host='0.0.0.0',port=5010)
