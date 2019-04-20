from boogie.apps.users.models import UserManager as BaseUserManager, UserQuerySet as BaseUserQuerySet


class UserQuerySet(BaseUserQuerySet):
    """
    User queryset.
    """


class UserManager(BaseUserManager.from_queryset(UserQuerySet)):
    def get_by_email(self, value):
        """
        Return a user with the given e-mail.
        """
        return self.get(email=value)

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user