from data import *
from __init__ import db, app
from flask import request, jsonify

adv = {"todo":"inprogress", "inprogress":"done", "done":"done"}


def formatBoard(b):
    ele = Element.query.filter(Element.id.in_(b['board_elements'])).all()
    b['todo'] = []
    b['inprogress'] = []
    b['done'] = []
    for e in ele:
        l = element_schema.dump(e).data
        l['board_id'] = e.board_id
        b[e.category] += [l]
    del b['board_elements']
    b['tags'] = []
    return b

def formatBoard2(b):
    ele = Element.query.filter(Element.id.in_(b['board_elements'])).all()
    b['todo_count'] = 0
    b['inprogress_count'] = 0
    b['done_count'] = 0
    for e in ele:
        b[e.category + '_count'] += 1
    del b['board_elements']
    b['tags'] = []
    return b


  
@app.route("/kanban/boards", methods=['POST'])
def makeBoard():
    board = Board(**request.args)
    db.session.add(board)
    db.session.commit()
    r = {"success": True, "data": {'board': board_schema.dump(board).data}} 
    return jsonify(r)


@app.route("/kanban/boards", methods=['DELETE'])
def deleteBoard():

    b = Board.query.filter_by(id=int(request.args['id'])).first()
    db.session.delete(b)

    db.session.commit()
    return jsonify({"success":True})
    


@app.route("/kanban/boards", methods=['GET'])
def getBoards():
    r = {"success":True}
    l = []
    for i in Board.query.all():
        l += [formatBoard2(board_schema.dump(i).data)]

    r["data"] = {"boards": l}

    return jsonify(r)

@app.route("/kanban/boards/<board_id>", methods=['GET'])
def getBoard(board_id):
    b = Board.query.filter_by(id=board_id).first()
    r = {"success": True}
    r["data"] = {"board": formatBoard(board_schema.dump(b).data)}
    return jsonify(r)



@app.route("/kanban/board_elements", methods = ["GET"])
def getElement():
    #e = Element(**request.form)
    #db.session.add(e)
    #db.session.commit()
    e = Element.query.all()
    l = []
    for i in e:
        l += [element_schema.dump(i).data]
    r = {"success": True}
    r['data'] = l
    #r["data"] = element_schema.dump(e).data
    return jsonify(r)

@app.route("/kanban/board_elements", methods = ["POST"])
def makeElement():
    e = Element(**request.args)
    db.session.add(e)
    db.session.commit()
    r = {"success": True}
    l = element_schema.dump(e).data
    l['board_id'] = e.board_id
    r["data"] = {'board_element': l}
    return jsonify(r)


@app.route("/kanban/board_elements", methods=['DELETE'])
def deleteElement():
    e = Element.query.filter_by(id=int(request.args['board_element_id'])).first()
    db.session.delete(e)
    db.session.commit()
    return jsonify({"success": True})
    
@app.route("/kanban/board_elements/advance", methods=["POST"])
def advance():
    e = Element.query.filter_by(id=int(request.args['id'])).first()
    e.category = adv[e.category]
    db.session.add(e)
    db.session.commit()
    return jsonify({"success": True})
