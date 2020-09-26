from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.dispatch import receiver

from .models import Customer


@receiver(post_save, sender=User)
def customer_profile(sender, instance, created,  **kwargs):
    if created:
        group = Group.objects.filter(name='customer').first()
        instance.groups.add(group)
        Customer.objects.create(
            user=instance,
            name=instance.username,
            )
        print('profile created')


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.customer.save()


post_save.connect(customer_profile, sender=User)