from app import  db
from models import AdminMessage
from test_Homepage import MyTest

class UserListTest(MyTest):
    def test_add_Message_Admin_db(self):
        message = AdminMessage(title = 'testitleAdmin', description = 'testdescription')
        db.session.add(message)
        db.session.commit() 
        assert message in db.session

    def test_delete_Message_Admin_db(self):
        message = AdminMessage(title = 'testitleAdmin', description = 'testdescription')
        db.session.add(message)
        db.session.commit() 
        message = AdminMessage.query.filter_by(id=1).first()
        db.session.delete(message)
        db.session.commit()
        assert message not in db.session

    def test_add_Message_All_Admin(self):
        tester = self.app.test_client(self)  
        response = tester.post('/messageSenderFromAdminToAll', data={'title': 'test', 'description': 'test'})
        self.assertRedirects(response, 'http://localhost:3000/adminpage')

    def test_delete_Message_Admin(self):
        new_message = AdminMessage(title='title', description='description')
        db.session.add(new_message)
        db.session.commit()
        tester = self.app.test_client(self)  
        response = tester.post('/messageDeleterAdmin', data={'id': '1'})
        self.assertRedirects(response, 'http://127.0.0.1:5000/')