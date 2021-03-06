"""
This file contains the common infos to send email
Brazil Data Cube projects
"""
import os

BASE_PATH_TEMPLATES = os.getenv(
    'BASE_PATH_TEMPLATES', '{}/bdc_core/email/templates'.format(os.getcwd()))

SMTP_PORT = os.getenv('SMTP_PORT', '587')
SMTP_HOST = os.getenv('SMTP_HOST', 'smtp.domain.com')

EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS', 'test@domain.com')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD', 'password')
