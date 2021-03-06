from app import db,app,ma
from  models import Member,Circular,CircularItem
from  models import  MemberSchema,CircularSchema,CircularItemSchema
import sys
import unittest
from pprint import pprint 
from seeder import seeder
import datetime

class BasicTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        #print("----setUp--------------")
        seeder()

    @classmethod
    def tearDownClass(self):
        #print("----tearDown-----------")
        pass

    def test_get_members(self): 
   
        #--- member 全件読み取り　-----
        members = Member.query.all()
        m_count = len(members)
        #for member in members:
        #    print(m_count,member)
        self.assertTrue(m_count)

    def test_get_members_dict(self):    
        #--- member 全件読み取り　-----
        members = Member.query.all()
        m_count = len(members)
        #for member in members:
        #    print(m_count,member)
        #self.assertTrue(m_count)
        sch = MemberSchema(many=True).dump(members)
        #print(sch)
        self.assertTrue(sch)
        #self.assertEqual(sch[0]['name'],'小野')

    def test_get_member_byId(self):

        #--- member 1件読み取り　-----
        member = Member.query.filter(Member.id == 1).first()
        self.assertTrue(member)
        self.assertEqual(member.id,1)

        #print("--- Member1件読込NG --")
        members = Member.query.filter(Member.id == 9999).all()
        self.assertFalse(members)
        self.assertEqual(len(members),0)

    def test_get_member_byId_dict(self):

        #--- member 1件読み取り　-----
        member = Member.query.filter(Member.id == 1).first()
        self.assertTrue(member)
        self.assertEqual(member.id,1)

        sch = MemberSchema().dump(member)
        #pprint(sch)
        self.assertTrue(sch)
        self.assertEqual(sch['name'],'小野')


    def test_get_circulars(self):
        #--- circular 全件読み取り　-----
        circulars = Circular.query.all()
        self.assertTrue(circulars)
        self.assertGreaterEqual(len(circulars),1)

        #--- circular itemsも含めて全件読み取り　-----
        circulars = Circular.query.all()
        item_count = 0
        for circular in circulars:
            #print(circular)
            for item in circular.items:
                #print("   ",item)
                item_count += 1
        self.assertGreaterEqual(item_count,1)

    def test_get_circulars_dict(self):

        #--- circular itemsも含めて全件読み取り　-----
        #print("--- Circular+items全件読込 --")
        circulars = Circular.query.all()
        item_count = 0
        for circular in circulars:
            #print(circular)
            for item in circular.items:
                #print("   ",item)
                item_count += 1
        self.assertGreaterEqual(item_count,1)

        sch = CircularSchema(many=True).dump(circulars)
        #pprint(sch, indent=4)
        self.assertTrue(sch)
        self.assertEqual(sch[0]['title'],'全体会議')
        self.assertGreaterEqual(len(sch[0]['items']),1)
        self.assertEqual(sch[0]['items'][0]['memberId'],1)



    def test_update_circular(self):
  
        #--- circular 1件目を更新　-----
        #print("--- Member更新 --")
        member = Member.query.filter(Member.id==2).first()
        member.email = "xxx"
        db.session.commit()

        member = Member.query.filter(Member.id==2).first()
        self.assertGreaterEqual(member.email,"xxx")

    def test_create_circular(self):
        c_list=[
            Circular(title="new-01 circular",detail="new 01 detail",dueDate=datetime.datetime.strptime("2021/12/01", "%Y/%m/%d")),
            Circular(title="new-02 circular",detail="new 02 detail",dueDate=datetime.datetime.strptime("2021/12/01", "%Y/%m/%d"))
        ]
        db.session.add_all(c_list)
        db.session.commit()
        self.assertGreater(len(Circular.query.all()),2)

    def test_delete_circular(self):
        circular = Circular(title="for delete",detail="new 03 detail")
        db.session.add(circular)    
        db.session.commit()
        new_id = circular.id
        #--- circular 1件目を削除　-----
        member = Member.query.filter(Member.id==new_id).delete()
        db.session.commit()

        member = Member.query.filter(Member.id==new_id).all()
        self.assertGreaterEqual(len(member),0)
        #print("member:", member)

    def test_create_circular_circularItems(self):
        circularItems = [
            CircularItem(memberId=1,memo="memo-1"),
            CircularItem(memberId=2,memo="memo-2"),
            CircularItem(memberId=3,memo="memo-3")
        ]
        new_circular = Circular(title="new-04 circular",detail="new 04 detail",items=circularItems)
        db.session.add(new_circular)
        db.session.commit()
        new_id = new_circular.id
        circular = Circular.query.filter(Circular.id==new_id).first()
        #pprint( CircularSchema().dump(circular))
        self.assertGreaterEqual(len(circular.items),3)

    def test_update_circular_circularItems(self):
        #---　アイテムが3件あるcircularを作成する --
        circularItems = [
            CircularItem(memberId=1,memo="memo-21"),
            CircularItem(memberId=2,memo="memo-22"),
            CircularItem(memberId=3,memo="memo-23")
        ]
        new_circular = Circular(title="new-05 circular",detail="new 05 detail",items=circularItems)
        db.session.add(new_circular)
        db.session.commit()
        new_id = new_circular.id
        circular = Circular.query.filter(Circular.id==new_id).first()
        #pprint( CircularSchema().dump(circular))
        self.assertGreaterEqual(len(circular.items),3)
        #---　データを1件更新する -- 
        circularItem = CircularItem.query.filter(CircularItem.circularId==new_id and memberId==1).first()
        #pprint(CircularItemSchema().dump(circularItem))
        circularItem.memo = "update memo"
        db.session.commit()
        circularItem = CircularItem.query.filter(CircularItem.circularId==new_id and memberId==1).first()
        self.assertEqual("update memo", circularItem.memo)
        #この更新は無理がある。新規idがかくれてしまっている

    def test_delete_circular_cascade(self):
        #---　アイテムが3件あるcircularを作成する --
        circularItems = [
            CircularItem(memberId=1,memo="memo-31"),
            CircularItem(memberId=2,memo="memo-32"),
            CircularItem(memberId=3,memo="memo-33")
        ]
        new_circular = Circular(title="new-05 circular",detail="new 05 detail",items=circularItems)
        db.session.add(new_circular)
        db.session.commit()
        new_id = new_circular.id
        circular = Circular.query.filter(Circular.id==new_id).first()
        #pprint( CircularSchema().dump(circular))
        self.assertGreaterEqual(len(circular.items),3)

        db.session.delete(circular)
        db.session.commit()
        circular = Circular.query.filter(Circular.id==new_id).first()
        self.assertFalse(circular)
        circular = CircularItem.query.filter(CircularItem.circularId==new_id).first()
        self.assertFalse(circular)


    def test_bulk_save_circular(self):
        # bulk_save_objectsが使えるかどうか
        circular = Circular(title="new-bulk_01 circular",detail="new bulk 01 detail",dueDate=datetime.datetime.strptime("2021/12/01", "%Y/%m/%d"))
        db.session.bulk_save_objects([circular])
        db.session.commit()
        self.assertEqual(len(Circular.query.filter(Circular.title.like("%new-bulk_01%")).all()),1)

        # bulk_save_objectsでitemsも登録できるかどうか
        circular = Circular(title="new-bulk_02 circular",detail="new bulk 02 detail",dueDate=datetime.datetime.strptime("2021/12/01", "%Y/%m/%d"))
        db.session.add(circular)
        db.session.commit()
        self.assertEqual(len(Circular.query.filter(Circular.title.like("%new-bulk_02%")).all()),1)
        print("circularId:",circular.id)

        circularItems = [
            CircularItem(id=91,circularId=circular.id,memberId=1,memo="memo-bulk-41"),
            CircularItem(id=92,circularId=circular.id,memberId=1,memo="memo--bulk-42"),
            CircularItem(id=93,circularId=circular.id,memberId=3,memo="memo--bulk-43")
        ]
        db.session.bulk_save_objects(circularItems)
        db.session.commit()

        circularItems = [
            CircularItem(id=92,circularId=circular.id,memberId=9,memo="memo-bulk-41-2").query.filter(CircularItem.id==92).first()
        ]
        db.session.bulk_save_objects(circularItems)
        db.session.commit()

        result =  CircularItem.query.filter(CircularItem.id==92).first()
        self.assertEqual( result.id ,92)

        result =  Circular.query.filter(Circular.id==circular.id).first()
        pprint( CircularSchema().dump(result))




#        print("id:",circularItems[0][].CircularItem.id)
        #print("221 itemId:",itemId)

        result =  CircularItem.query.filter(CircularItem.id==91).first()
        self.assertEqual( result.id ,91)
        #pprint(resultCircular)
        #pprint( CircularSchema().dump(resultCircular))

        # 登録したものから一つを更新してみる
        circularItem =  CircularItem.query.filter(CircularItem.id==91).first()
        circularItem.memberId = 2
        circularItem.memo = "Update by sabe_objects 91"
        db.session.bulk_save_objects([circularItem])
        db.session.commit()
        result =  Circular.query.filter(Circular.id==circular.id).first()
        #pprint( CircularSchema().dump(result))
        self.assertEqual( result.items[0].memberId,2)
        self.assertEqual( result.items[0].memo,"Update by sabe_objects 91")


        #--- circular 1件目を更新　-----
        #print("--- Member更新 --")
        '''
        member = Member.query.filter(Member.id==2).first()
        member.email = "xxx"
        db.session.commit()

        member = Member.query.filter(Member.id==2).first()
        self.assertGreaterEqual(member.email,"xxx")
        '''


if __name__ == '__main__':
    unittest.main()
