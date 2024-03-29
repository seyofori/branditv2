from django.db import models
from . import contest
from . import categories
import datetime
from django.contrib.auth.models import User
from django.utils.timezone import now

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.client.id, filename)


class Contest(models.Model):
    # the client who creates the contest
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    is_draft = models.BooleanField(default=True)
    title = models.CharField(max_length=50, blank=True, null=True)  # the title of the contest
    about = models.TextField(blank=True, null=True)  # more detailed information on the contest
    # the prize brandlancer gets for winning the contest for the contest
    prize = models.PositiveIntegerField(blank=True, null=True)
    # the end date of the contest
    end_date = models.DateField(default=datetime.date.today)
    is_verified = models.BooleanField(default=False)
    # whether the client has paid for the contest
    is_paid_for = models.BooleanField(default=False)
    payment_token = models.CharField(max_length=100, blank=True, null=True)
    # category to which the contest belongs
    category = models.ForeignKey(
        'Category', on_delete=models.SET_NULL, null=True)
    is_top = models.BooleanField(default=False)
    is_hidden = models.BooleanField(default=False)
    is_nda = models.BooleanField(default=False)
    is_sealed = models.BooleanField(default=False)
    cost = models.PositiveSmallIntegerField(
        blank=True, null=True)  # the cost for the contest
    # files associated with contest
    files = models.FileField(
        upload_to=user_directory_path, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    preferred_style = models.TextField(blank=True, null=True)
    preferred_colors = models.CharField(max_length=50, blank=True, null=True)
    target_audience = models.TextField(blank=True, null=True)
    design_details = models.TextField(blank=True, null=True)
    would_like_to_print = models.BooleanField()
    logo = models.FileField(
        upload_to=user_directory_path, blank=True, null=True)
    sketch = models.FileField(
        upload_to=user_directory_path, blank=True, null=True)
    is_closed = models.BooleanField(default=False)
    is_touched = models.BooleanField(default=False) #indicates if admin has 'touched' this record or not



    def __str__(self):
        return self.title


    def touch(self):
        self.is_touched = True


def get_num_new_contests():
    return Contest.objects.filter(is_touched=False).count()