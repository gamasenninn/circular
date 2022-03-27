from app import app
from models import db,Member,Circular,CircularItem


def seeder():
    models = [Member,Circular,CircularItem]

    for model in models:
        db.session.query(model).delete()
        db.session.commit()

    #------ Member ------
    #print("Seed for Member")
    members = [
        Member( id=1, name= "小野", telNumber="000-0000-0001" ,department="Web"  ,email="1111@email.xx",memo="memo01"),
        Member( id=2, name= "佐藤", telNumber="000-0000-0002" ,department="Web"  ,email="2222@email.xx",memo="memo02"),
        Member( id=3, name= "田中", telNumber="000-0000-0003" ,department="Web"  ,email="3333@email.xx",memo="memo03"),
        Member( id=4, name= "渡辺", telNumber="000-0000-0004" ,department="shop" ,email="4444@email.xx",memo="memo04"),
        Member( id=5, name= "小林", telNumber="000-0000-0005" ,department="shop" ,email="5555@email.xx",memo="memo05"),
    ]
    db.session.add_all(members)
    db.session.commit()

    #members = Member.query.all()
    #for member in members:
    #    print(member,member.createdAt)

    #------ Circular ------
    #print("\nSeed for Circular")
    circulars = [
        Circular( id=1, title= "全体会議", detail="全体会議なので全員出席希望です"  ),
        Circular( id=2, title= "企画プレゼン", detail="新企画のプレゼン参加希望者欠をとります"  ),
    ]
    db.session.add_all(circulars)
    db.session.commit()

    #circulars = Circular.query.all()
    #for circular in circulars:
    #    print(circular)


    #------ CircularItems ------
    #print("\nSeed for CircularItem")
    circularItems = [
        CircularItem( id=1, circularId=1, memberId=1, person = '小野', department="web", confirm=True, memo="OK 参加します"  ),
        CircularItem( id=2, circularId=1, memberId=2, person = '佐藤', department="web", confirm=True, memo="気分しだい"  ),
        CircularItem( id=3, circularId=1, memberId=2, person = '田中', department="shop", confirm=False, memo="体調不良のため"  ),
        CircularItem( id=4, circularId=2, memberId=1, person = '小野', department="shop", confirm=False, memo="法事のため不参加"  ),
    ]
    db.session.add_all(circularItems)
    db.session.commit()

    circularItems = CircularItem.query.all()
    #for circularItem in circularItems:
    #    print(circularItem)

if __name__ == '__main__':
    seeder()



