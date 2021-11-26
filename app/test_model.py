from app import db,app,ma
from  models import Member,Circular,CircularItem
from  models import  MemberSchema,CircularSchema,CircularItemSchema
import sys
import unittest
from pprint import pprint 

class BasicTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        #print("----setUp--------------")
        pass   

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
        self.assertEqual(sch[0]['name'],'小野')

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
            Circular(title="new-01 circular",detail="new 01 detail"),
            Circular(title="new-02 circular",detail="new 02 detail")
        ]
        db.session.add_all(c_list)
        db.session.commit()
        self.assertGreater(len(Circular.query.all()),2)

    def test_delete_circular(self):

        #--- circular 1件目を削除　-----
        member = Member.query.filter(Member.id==3).delete()
        db.session.commit()

        member = Member.query.filter(Member.id==3).all()
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
        pprint(CircularItemSchema().dump(circularItem))
        circularItem.memo = "update memo"
        db.session.commit()
        circularItem = CircularItem.query.filter(CircularItem.circularId==new_id and memberId==1).first()
        self.assertEqual("update memo", circularItem.memo)


if __name__ == '__main__':
    unittest.main()
