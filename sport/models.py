from django.db import models
from django.utils import timezone

sport_choice = {
    ('Baseball', 'Baseball'),
    ('Basketball', 'Basketball'),
    ('Golf', 'Golf'),
    ('Hiking', 'Hiking'),
    ('Riding', 'Riding'),
    ('Running', 'Running'),
    ('Soccer', 'Soccer'),
    ('Swimming', 'Swimming'),
    ('Tennis', 'Tennis'),
    ('Other sports', 'Other sports')
}

duration_choice = {
    ('30 min', '30 min'),
    ('1 hour', '1 hour'),
    ('1 hour 30 min', '1 hour 30 min'),
    ('2 hours', '2 hours'),
    ('longer than 2 hours', 'longer than 2 hours') 
}

feedback_choice = {
    ('excellent', 'excellent'),
    ('good', 'good'),
    ('average', 'average')
}


class Sports(models.Model):
    sport = models.CharField(max_length=100, choices=sport_choice)
    duration = models.CharField(max_length=100, choices=duration_choice)
    date = models.DateTimeField(default=timezone.now)
    feedback = models.CharField(max_length=100, choices=feedback_choice)

    def __str__(self):
        return self.sport