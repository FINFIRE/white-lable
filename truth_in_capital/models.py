from django.db import models
from django.contrib.auth.models import User
from Algorithm.models import capitalTypes,CapitalType
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class TruthCapitalType(models.Model):
    class Meta:
        verbose_name = "A. Capital Type"
        verbose_name_plural = "A. Capital Types"
        # Ensure unique capital types per user
        unique_together = [['user', 'capital_type']]

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    CAPITAL_TYPE_CHOICES = [
        ("Accelerator", "Accelerator"),
        ("Bonds", "Bonds"),
        ("Bootstrapped", "Bootstrapped"),
        ("Commercial Banking", "Commercial Banking"),
        ("Cryptocurrency", "Cryptocurrency"),
        ("Factoring", "Factoring"),
        ("Grants", "Grants"),
        ("Hedge Funds", "Hedge Funds"),
        ("Incubator", "Incubator"),
        ("Investment Banking", "Investment Banking"),
        ("Private Debt", "Private Debt"),
        ("Private Equity Securities", "Private Equity Securities"),
        ("Royalty Financing", "Royalty Financing"),
        ("Small Business Administration (SBA)", "Small Business Administration (SBA)"),
        ("Third Party Corporate Credit", "Third Party Corporate Credit"),
        ("Tokenization", "Tokenization"),
        ("Venture Capital", "Venture Capital"),
    ]

    capital_type = models.CharField(max_length=200, choices=CAPITAL_TYPE_CHOICES, blank=False)
    def __str__(self):
        return f"{self.user} : {self.capital_type}"

class Task(models.Model):
    class Meta:
        verbose_name = "B. Task"
        verbose_name_plural = "B. Task"
        ordering = ['task_precedence']

    capital_type = models.ForeignKey(
        TruthCapitalType,
        on_delete=models.CASCADE,
        related_name='tasks'
    )

    CAPITAL_TASK_TYPE_CHOICES = [
        ("FINFIRE Staff Review & Scope of Work", "FINFIREStaff Review & Scope of Work"),
        ("Intermediary Services Scope of Work", "Intermediary Services Scope of Work"),
    ]
    task_name = models.CharField(max_length=200)
    task_max_hour = models.PositiveIntegerField(validators=[MinValueValidator(0),MaxValueValidator(32)])
    task_type = models.CharField(max_length=200,choices=CAPITAL_TASK_TYPE_CHOICES,blank=False)
    #task_rating = models.PositiveIntegerField(null=True, blank=True)
    task_precedence = models.PositiveSmallIntegerField(default=0)  # Allow same precedence for different tasks

    @property
    def user(self):
        return self.capital_type.user

    def __str__(self):
        return f"{self.capital_type} and his task : {self.task_name} with (Precedence: {self.task_precedence})"

class time(models.Model):
    class Meta:
        verbose_name = "C. Time"
        verbose_name_plural = "C. Time"

    capital_type = models.OneToOneField(
        TruthCapitalType,
        on_delete=models.CASCADE,
        related_name='time'
    )
    start_date = models.DateField()
    #duration_capital_weeks = models.DurationField()

class rating(models.Model):
    class Meta:
        verbose_name = "D. rating"
        verbose_name_plural = "D. ratings"

    task = models.OneToOneField(
        Task,
        on_delete=models.CASCADE,
        related_name='rating'
    )
    rating = models.PositiveIntegerField(validators=[
        MinValueValidator(0),
        MaxValueValidator(10),
    ])


