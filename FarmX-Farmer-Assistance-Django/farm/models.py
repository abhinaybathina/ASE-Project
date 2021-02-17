from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

state_choices = [

    ("AP", "Andhra Pradesh"), ("AR", "Arunachal Pradesh"), ("AS", "Assam"), ("BR", "Bihar"),
    ("CG", "Chandigarh"), ("CH", "Chhattisgarh"),
    ("DN", "Dadra and Nagar Haveli"), ("DL", "Delhi"), ("GJ", "Gujarat"), ("HR", "Haryana"),
    ("HP", "Himachal Pradesh"), ("JK", "Jammu and Kashmir"), ("JH", "Jharkhand"), ("KA", "Karnataka"),
    ("KL", "Kerala"), ("LD", "Lakshadweep"), ("MP", "Madhya Pradesh"), ("MH", "Maharashtra"),
    ("MN", "Manipur"), ("ML", "Meghalaya"), ("MZ", "Mizoram"),
    ("NL", "Nagaland"), ("OR", "Odisha"), ("PB", "Punjab"), ("SK", "Sikkim"),
    ("TN", "Tamil Nadu"), ("TS", "Telangana"),
    ("UP", "Uttar Pradesh"), ("UK", "Uttarakhand"), ("WB", "West Bengal")
]

crop_choices = [
    ('Food Crops', (
        ('Wheat', 'Wheat'),
        ('Rice', 'Rice'),
        ('Dal', 'Dal'),
        ('Maize', 'Maize'),
        ('Pulses', 'Pulses'),
        ('Millets', 'Millets')
    )
     ),
    ('Cash Crops', (
        ('Sugarcane', 'Sugarcane'),
        ('Tobacco', 'Tobacco'),
        ('Cotton', 'Cotton'),
    )
     ),
    ('Plantation Crops', (
        ('Coffee', 'Coffee'),
        ('Coconut', 'Coconut'),
        ('Tea', 'Tea')
    )
     )

]

water_sources = [
    ('River', 'River'),
    ('Drilled Well', 'Drilled Well'),
    ('Drainage ponds', 'Drainage ponds'),
    ('Rain Water', 'Rain Water')
]


# Create your models here.
class Farm(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    state = models.CharField(choices=state_choices, max_length=200, verbose_name='State')
    village = models.CharField(max_length=100, verbose_name='Village')
    total_land_available = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Total land owned',
                                               help_text='In Acres')
    land_cultivating = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Land planning to cultivate',
                                           help_text='In Acres')
    crop = models.CharField(choices=crop_choices, max_length=200, verbose_name='Crop')
    expecting_yield = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Yield Expecting',
                                          help_text='In Quintal', null=True)
    water_source = models.CharField(choices=water_sources, max_length=100, verbose_name='Water Source', default='Rain Water')

    class Meta:
        ordering = ['-total_land_available']

    def __str__(self):
        return f'{self.owner.username}\'s Farm in {self.village}'
