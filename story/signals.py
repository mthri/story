from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.conf import settings

from .models import Story
from utils.telegram import send_message_to_telegram_channel


story_message = '''<strong>{title}</strong>

{preview}

<a href="{link}">🌐 ادامه داستان</a>'''



@receiver(pre_save, sender=Story)
def story_pre_save(sender, instance, **kwargs):
    if not instance.created_at:
        send_message_to_telegram_channel('⚠️ ' + story_message.format(
            title=instance.title,
            preview=instance.preview,
            link=f'{settings.MAIN_HOST}{instance.url}'
        ), channel_id=settings.TLG_ADMIN_CHANNEL_ID)


@receiver(post_save, sender=Story)
def story_post_save(sender, update_fields, instance: Story, created: bool, **kwargs):
    if update_fields and not created and 'accept' in update_fields and instance.accept:
        send_message_to_telegram_channel(story_message.format(
            title=instance.title,
            preview=instance.preview,
            link=f'{settings.MAIN_HOST}{instance.url}'
        ), channel_id=settings.TLG_PUBLIC_CHANNEL_ID)