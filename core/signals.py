from venv import create
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail, EmailMultiAlternatives
from .models import CourseRegistrations, Mails, User
from itadis.settings import EMAIL_HOST_USER
from django.utils.safestring import mark_safe
from django.db import transaction


def on_transaction_commit(func):
    def inner(*args, **kwargs):
        transaction.on_commit(lambda: func(*args, **kwargs))
    return inner


@receiver(post_save, sender=CourseRegistrations)
def post_save_courses_reg(instance, created, **kwargs):
    if created:
        subject = f'{instance.full_name} - {instance.phone_number}'
        from_email = EMAIL_HOST_USER
        to = [user.email for user in User.objects.filter(is_superuser=True)]
        text_content = f'<h3>{instance.full_name} - {instance.phone_number}</h3>'+f'<h3>{instance.course.title} - {instance.course_time.title}</h3>'+f'<h4>{instance.email}:</h4> {instance.personal_info}'
        html_content =  f'<h3>{instance.full_name} - {instance.phone_number}</h3>'+f'<h3>{instance.course.title} - {instance.course_time.title}</h3>'+f'<h4>{instance.email}:</h4> {instance.personal_info}'
        msg = EmailMultiAlternatives(subject, text_content, from_email, to)
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        # mail = send_mail(
        #     f'{instance.full_name} - {instance.phone_number}',
        #     mark_safe(f'<h3>{instance.full_name} - {instance.phone_number}</h3>'+
        #     f'<h3>{instance.course.title} - {instance.course_time.title}</h3>'+
        #     f'<h4>{instance.email}:</h4> {instance.personal_info}'),
        #     ,
        #     [user.email for user in User.objects.filter(is_superuser=True)],
        #     fail_silently=False,
        # )

@receiver(post_save, sender=Mails)
@on_transaction_commit
def post_save_mails(instance, created, **kwargs):
    if created:
        subject = f'{instance.subject}'
        from_email = EMAIL_HOST_USER
        to = [person.email for person in instance.send_to.all()]
        text_content = f'{instance.message}'
        html_content =  f'{instance.message}'
        msg = EmailMultiAlternatives(subject, text_content, from_email, to)
        msg.attach_alternative(html_content, "text/html")
        msg.send()
       



