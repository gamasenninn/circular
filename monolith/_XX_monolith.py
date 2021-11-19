#from app import app,db


from models import db,Member


if __name__ == '__main__':

    mem = Member.query.get(1)
    print(mem)
    mem.name = "xxfffff"
    print(mem)
    db.session.commit()


    mems = Member.query.all()
    for mem in mems:
        print(mem)




