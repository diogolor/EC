from django.test import TestCase
from ecweb.models import (
    ClassRoom,
    User,
    Student,
    Teacher,
    MyUserManager
)


class ClassRoomModelTest(TestCase):
    def setUp(self):
        self.classroom = ClassRoom.objects.create(
            number_class='01',
            nivel="upper"
        )
        self.user = User.objects.create(
            email="test@ec.com",
            first_name="TestName",
            last_name="TestLastName",
            cod=1,
        )

    def test_create(self):
        self.assertTrue(ClassRoom.objects.exists())

    def test_int_number_class(self):
        number = 1
        self.assertEqual(number, int(self.classroom.number_class))

    def test_str_nivel(self):
        self.assertEqual('upper', str(self.classroom.nivel))

    def test_student_forengkey(self):
        self.student = Student.objects.create(
            user=self.user,
            classroom=self.classroom
        )
        self.assertTrue(Student.objects.exists())

    def test_teacher_forengkey(self):
        self.teacher = Teacher.objects.create(
            user=self.user,
            classroom=self.classroom
        )
        self.assertTrue(Teacher.objects.exists())


class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="test@ec.com",
            password="abcd1234ec",
            first_name="TestName",
            last_name="TestLastName",
            cod=1,
            type_of_course="6-month"
        )

    def test_create(self):
        self.assertTrue(User.objects.exists())

    def test_is_istance_manager(self):
        self.assertIsInstance(User.objects, MyUserManager)

    def test_is_instance_of_user(self):
        self.assertIsInstance(self.user, User)

    def test_str_method(self):
        object_name = '{} {}'.format(
            self.user.first_name,
            self.user.last_name
        )
        self.assertEqual(object_name, str(self.user))

    def test_if_login_pass(self):
        login = self.client.login(
            username=self.user.email,
            password="abcd1234ec"
        )
        self.assertTrue(login)

    def test_default_image_profile(self):
        avatar_image_url = self.user.avatar
        self.assertEqual('avatars/user_default.png', avatar_image_url)
