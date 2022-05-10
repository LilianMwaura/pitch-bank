import unittest
from app.models import Users, Pitch, Comment

class UserModelTest(unittest.TestCase):
    
    def setUp(self):
        self.new_user = Users(password = 'banana')

    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)

    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('banana'))

class PitchModelTest(unittest.TestCase):
        '''
        Test class to test the behavior of the Pitch class
        '''

        def setUp(self):
            '''
            Set up method that will run before every Test
            '''
            self.new_pitch = Pitch(1, 1,' pitch', 'pitch','pitch')

        def test_instance(self):
            '''
            '''
            self.assertTrue(isinstance(self.new_pitch, Pitch))

        def test_to_check_instance_variables(self):
            '''
            '''
            self.assertEquals(self.new_pitch.id, 1)
            self.assertEquals(self.new_pitch.owner_id, 1)
            self.assertEquals(self.new_pitch.description, 'pitch')
            self.assertEquals(self.new_pitch.title, 'pitch')
            self.assertEquals(self.new_pitch.category, 'business')
            
class CommentModelTest(unittest.TestCase):
        '''
        Test class to test the behavior of the Comment class
        '''

        def setUp(self):
            '''
            Set up method that will run before every Test
            '''
            self.new_comment = Comment(1, 1,' comment')

        def test_instance(self):
            '''
            '''
            self.assertTrue(isinstance(self.new_comment, Comment))

        def test_to_check_instance_variables(self):
            '''
            '''
            self.assertEquals(self.new_pitch.id, 1)
            self.assertEquals(self.new_comment.owner_id, 1)
            self.assertEquals(self.new_comment.content, 'comment')
            
if __name__ == '__main__':
    unittest.main()