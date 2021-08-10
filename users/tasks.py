from celery import shared_task
import requests

from project_bitlab.celery import celery_app


@celery_app.task(name="send_sms",
                 bind=True,
                 default_retry_delay=5,
                 max_retries=1,
                 acks_late=True)
def send_sms(self, phone, otp):
    phone_num = str(phone)
    url = 'https://api.mobizon.kz/service/message/sendsmsmessage?recipient=' + phone_num \
          + '&text=' + otp + '%21&apiKey=kz75ab6a40c2a5bddf8bf5a57ec3310bd10d5323c40b471ea2604b5aab2bc603a3e39b'
    # requests.get(url)
    print('===== SENT SMS ========', phone, otp, '========')