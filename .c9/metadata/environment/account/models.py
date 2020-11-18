{"filter":false,"title":"models.py","tooltip":"/account/models.py","undoManager":{"mark":5,"position":5,"stack":[[{"start":{"row":1,"column":0},"end":{"row":2,"column":29},"action":"insert","lines":["from django.contrib.auth.models import AbstractBaseUser, BaseUserManager","from .utils import ChoiceEnum"],"id":2}],[{"start":{"row":3,"column":26},"end":{"row":4,"column":0},"action":"insert","lines":["",""],"id":3}],[{"start":{"row":4,"column":0},"end":{"row":37,"column":19},"action":"insert","lines":["class MyAccountManager(BaseUserManager):","    def create_user(self, email, username, firstname, lastname, password=None):","        if not email:","            raise ValueError(\"Users must have an email address.\")","        if not username:","            raise ValueError(\"Users must have a username.\")","        if not firstname:","            raise ValueError(\"Users must have a first name.\")","        if not lastname:","            raise ValueError(\"Users must have a last name.\")","            ","        user = self.model(","                email = self.normalize_email(email),","                username = username,","                firstname = firstname,","                lastname = lastname,","            )","        user.set_password(password)","        user.save(using=self._db)","        return user","        ","    def create_superuser(self, email, username, firstname, lastname, password):","        user = self.create_user(","                email = self.normalize_email(email),","                username = username,","                firstname = firstname,","                lastname = lastname,","                password = password","            )","        user.is_admin = True","        user.is_staff = True","        user.is_superuser = True","        user.save(using=self._db)","        return user"],"id":4}],[{"start":{"row":37,"column":19},"end":{"row":38,"column":0},"action":"insert","lines":["",""],"id":5},{"start":{"row":38,"column":0},"end":{"row":38,"column":8},"action":"insert","lines":["        "]},{"start":{"row":38,"column":8},"end":{"row":39,"column":0},"action":"insert","lines":["",""]},{"start":{"row":39,"column":0},"end":{"row":39,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":39,"column":4},"end":{"row":39,"column":8},"action":"remove","lines":["    "],"id":6},{"start":{"row":39,"column":0},"end":{"row":39,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":39,"column":0},"end":{"row":73,"column":29},"action":"insert","lines":["class Account(AbstractBaseUser):","    email           = models.EmailField(verbose_name=\"email\", max_length=60, unique=True)","    username        = models.CharField(max_length=30, unique=True)","    date_joined     = models.DateTimeField(verbose_name=\"date joined\", auto_now_add=True)","    last_login      = models.DateTimeField(verbose_name=\"last login\", auto_now=True)","    is_admin        = models.BooleanField(default=False)","    is_active       = models.BooleanField(default=True)","    is_staff        = models.BooleanField(default=False)","    is_superuser    = models.BooleanField(default=False)","    firstname       = models.CharField(max_length=20)","    lastname        = models.CharField(max_length=20)","    ","    class RosterSide(ChoiceEnum):","    \t\tA = 'A'","    \t\tB = 'B'","    \t\t","    roster_side = models.CharField(max_length=2, choices=RosterSide.choices(), default='None')","    current_leave_total = models.FloatField(default=250.00)","    ","    USERNAME_FIELD = 'email'","    REQUIRED_FIELDS = ['username', 'firstname', 'lastname']","    ","    objects = MyAccountManager()","    ","    def __str__(self):","        return self.firstname + \" \" + self.lastname","        ","    def has_perm(self, perm, obj=None):","        return self.is_admin","        ","    def has_module_perms(self, app_label):","        return True","        ","    def get_short_name(self):","        return self.firstname"],"id":7}]]},"ace":{"folds":[],"scrolltop":413,"scrollleft":0,"selection":{"start":{"row":56,"column":36},"end":{"row":56,"column":36},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":28,"state":"start","mode":"ace/mode/python"}},"timestamp":1605539766145,"hash":"47237febd5d89d8a0d76506ed83c1cec529a61a6"}