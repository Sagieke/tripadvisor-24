from app import  db
from models import FAQ
from test_Homepage import MyTest

class UserListTest(MyTest):
    def test_add_faq_db(self):
        faq = FAQ(question = 'testquestion', answer = 'testanswer')
        db.session.add(faq)
        db.session.commit() 
        assert faq in db.session

    def test_add_faq(self):
        tester = self.app.test_client(self)  
        response = tester.post('/addFAQ', data={'question': 'test', 'answer': 'test'})
        self.assertRedirects(response, 'http://localhost:3000/techSupport')

    def test_delete_faq(self):
        faq = FAQ(question = 'question', answer = 'answer')
        db.session.add(faq)
        db.session.commit()
        tester = self.app.test_client(self)  
        response = tester.post('/deleteFAQ', data={'id': '1'})
        self.assertRedirects(response,'http://localhost:3000/techSupport')

    def test_update_faq(self):
        faq = FAQ(question = 'question', answer = 'answer')
        db.session.add(faq)
        db.session.commit()
        tester = self.app.test_client(self)  
        response = tester.post('/updateFAQ', data={'id':'1','question': 'test', 'answer': 'test'})
        self.assertRedirects(response,'http://localhost:3000/adminpage')