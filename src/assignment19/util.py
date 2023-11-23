import re

def is_valid_email(email):
    return bool(re.match(r'^([a-z0-9_\-]+)@([a-z0-9]+)\.([a-z]{1,3})$', email))

def filter_and_sort_emails(emails):
    return sorted(filter(is_valid_email, emails))
