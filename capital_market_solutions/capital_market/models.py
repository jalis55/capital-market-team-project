from django.db import models

# Create your models here.


class Applications(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name


class Teams(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name


class TeamMembers(models.Model):
    positions = (
        ('Manager', 'Manager'),
        ('Sr.Software Engineer', 'Sr.Software Engineer'),
        ('Software Engineer', 'Software Engineer'),
        ('Jr.Software Engineer', 'Jr.Software Engineer'),
        ('Intern', 'Intern')
    )
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    whatsapp = models.CharField(max_length=20)
    position = models.CharField(max_length=30, choices=positions)
    is_teamleader = models.BooleanField(default=False)
    application = models.ForeignKey(
        Teams, null=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.name


class Clients(models.Model):
    name = models.CharField(max_length=200)
    primary_email = models.CharField(max_length=20, null=True)
    secondary_email = models.CharField(max_length=200, null=True)
    primary_phone = models.CharField(max_length=20, null=True)
    secondary_phone = models.CharField(max_length=20, null=True)
    primary_cont_person = models.ForeignKey(
        TeamMembers, null=True, on_delete=models.SET_NULL, related_name="primary_cont_person")
    secondary_cont_person = models.ForeignKey(
        TeamMembers, null=True, on_delete=models.SET_NULL, related_name="secondary_cont_person")
    application = models.ForeignKey(Applications, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
