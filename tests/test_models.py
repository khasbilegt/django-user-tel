from django.db.utils import IntegrityError
from django.test import TransactionTestCase

from user_tel.factory import User, UserFactory


class UserManagerTestCase(TransactionTestCase):
    fields = ("is_active", "is_staff", "is_superuser")

    def test_create_user(self):
        for case in (None, False, True):
            with self.subTest(case=case):
                extra_fields = {"is_active": case, "is_staff": case, "is_superuser": case} if type(case) is bool else {}
                instance = UserFactory.build(**extra_fields)
                user = User.objects.create_user(instance.tel, instance.name, "password", **extra_fields)

                self.assertEqual(user.tel, instance.tel)
                self.assertEqual(user.name, instance.name)
                for field in self.fields:
                    self.assertEqual(getattr(user, field), bool(case))

    def test_create_superuser(self):
        for case in (None, True):
            with self.subTest(case=case):
                extra_fields = {"is_active": True, "is_staff": True, "is_superuser": True}
                instance = UserFactory.build(**extra_fields)
                user = User.objects.create_superuser(
                    instance.tel, instance.name, "password", **extra_fields if case else {}
                )

                self.assertEqual(user.name, instance.name)
                self.assertEqual(user.tel, instance.tel)
                for field in self.fields:
                    self.assertEqual(getattr(user, field), True)

    def test_create_superuser_with_false_fields(self):
        for field in self.fields:
            with self.subTest(field=field):
                self.assertRaises(
                    ValueError,
                    lambda _: User.objects.create_superuser(
                        "John Doe",
                        "99112233",
                        "password",
                        **{_field: field != _field for _field in self.fields},  # noqa
                    ),
                    f"Superuser must have {field}=True.",
                )

    def test_user_unique_constraint(self):
        user = UserFactory()

        with self.assertRaises(IntegrityError):
            User.objects.create_user(user.tel, user.name, "password", **{field: True for field in self.fields})

    def test_user_tel_validator(self):
        for tel in ("asdfd", "8811109", "823892839829", "89xx8299"):
            with self.subTest(tel=tel), self.assertRaises(IntegrityError):
                User.objects.create_user(tel, "John Doe", "password", **{field: True for field in self.fields})
