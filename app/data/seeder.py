import sys,os
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
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
        Member( id=1, name= "大岡敦", telNumber="" ,department="アグリ"  ,email="",memo="渉外部長"),
        Member( id=2, name= "草野真一", telNumber="" ,department="アグリ"  ,email="",memo="営業部長"),
        Member( id=3, name= "稲葉大地", telNumber="" ,department="アグリ"  ,email="",memo="販売係長"),
        Member( id=4, name= "保坂俊一", telNumber="" ,department="アグリ"  ,email="",memo=""),
        Member( id=5, name= "蒲喜美雄", telNumber="" ,department="アグリ"  ,email="",memo="販売課長"),
        Member( id=6, name= "山崎雅俊", telNumber="" ,department="アグリ"  ,email="",memo="整備課長"),
        Member( id=7, name= "五月女直樹", telNumber="" ,department="アグリ"  ,email="",memo=""),
        Member( id=8, name= "清野哲夫", telNumber="" ,department="アグリ"  ,email="",memo=""),
        Member( id=9, name= "篠崎理恵", telNumber="" ,department="アグリ"  ,email="",memo=""),
        Member( id=10, name= "黒瀬勤", telNumber="" ,department="アグリ"  ,email="",memo=""),
        Member( id=11, name= "中美香", telNumber="" ,department="アグリ"  ,email="",memo=""),
        Member( id=12, name= "小川朱美", telNumber="" ,department="アグリ"  ,email="",memo=""),
        Member( id=13, name= "小谷野正幸", telNumber="" ,department="アグリ"  ,email="",memo=""),
        Member( id=14, name= "三瓶博康", telNumber="" ,department="アグリ"  ,email="",memo=""),
        Member( id=15, name= "石川耕一", telNumber="" ,department="アグリ"  ,email="",memo=""),
        Member( id=16, name= "神山秀行", telNumber="" ,department="アグリ"  ,email="",memo=""),
        Member( id=17, name= "日原拓美", telNumber="" ,department="アグリ"  ,email="",memo=""),
        Member( id=18, name= "森龍樹", telNumber="" ,department="アグリ"  ,email="",memo=""),
        Member( id=19, name= "出井功一", telNumber="" ,department="アグリ"  ,email="",memo=""),
        Member( id=20, name= "大塚菊雄", telNumber="" ,department="ファーム"  ,email="",memo=""),
        Member( id=21, name= "高山唯人", telNumber="" ,department="ファーム"  ,email="",memo=""),
        Member( id=22, name= "白川ゆい", telNumber="" ,department="ファーム"  ,email="",memo=""),
        Member( id=23, name= "宮川和男", telNumber="" ,department="ファーム"  ,email="",memo=""),
        Member( id=24, name= "桶田貞子", telNumber="" ,department="物産店"  ,email="",memo=""),
        Member( id=25, name= "狐塚恵子", telNumber="" ,department="物産店"  ,email="",memo=""),
        Member( id=26, name= "鈴木悦子", telNumber="" ,department="物産店"  ,email="",memo=""),
        Member( id=27, name= "高瀬美知子", telNumber="" ,department="鶴田"  ,email="",memo=""),
        Member( id=28, name= "坂田恵", telNumber="" ,department="鶴田"  ,email="",memo=""),
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



