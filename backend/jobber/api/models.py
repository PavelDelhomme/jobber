from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    skills = models.TextField(blank=True, null=True)
    experience = models.TextField(blank=True, null=True)
    hobbies = models.TextField(blank=True, null=True)
    education = models.TextField(blank=True, null=True)
    job_preferences = models.TextField(blank=True, null=True)

    # Ajout des related_name pour éviter les conflits
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions'
    )

    def __str__(self):
        return self.username


class Entreprise(models.Model):
    name = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True, null=True)
    contact_info = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Candidature(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    status = models.ForeignKey('EtatCandidature', on_delete=models.SET_NULL, null=True)
    date_applied = models.DateField()
    salary_expectation = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    job_description = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} at {self.company.name}"

class EtatCandidature(models.Model):
    status = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.status


class HistoriqueCandidature(models.Model):
    candidature = models.ForeignKey(Candidature, on_delete=models.CASCADE)
    previous_status = models.ForeignKey(EtatCandidature, on_delete=models.SET_NULL, null=True, related_name='previous_status')
    new_status = models.ForeignKey(EtatCandidature, on_delete=models.SET_NULL, null=True, related_name='new_status')
    date_changed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Historique of {self.candidature.title} on {self.date_changed}"


class Document(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    document_type = models.CharField(max_length=100)
    file_url = models.URLField()
    date_uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Document {self.document_type} for {self.user.username}"



class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    read = models.BooleanField(default=False)
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username} - {self.message[:20]}"
