from collections import namedtuple

# Match Terms
#  A tuple of EXACT case-sensitive terms you know
#  will be in your listing
#
#  IMPORTANT: visit the refurb section on apple.com
#   and copy and paste the phrases you see there
#   exactly as you see them
FIND_TERMS = \
    "8GB of", \
    "256GB", \
    "March 2015", \
    "13.3", \

BASE_URL = "http://www.apple.com/"

# Model Refurb URL
#  Append the URL suffix to BASE_URL for the model of Mac you're looking for
MODEL_REFURB_URL = \
    BASE_URL + "shop/browse/home/specialdeals/mac/macbook_air/13"

# Email information
SEND_EMAIL = False
RECEIVER_EMAIL = ""

# Login information to send an email
SENDER_EMAIL = ""
EMAIL_USERNAME = ""
EMAIL_PASSWORD = ""

# This assumes your SMTP server uses SSL
SMTP_SERVER = ""
SMTP_PORT = 587

# Check apple.com every WAIT_SECONDS seconds
WAIT_SECONDS = 60.0 * 3

# Number of threads to keep in our email thread pool
THREADS = 2

LRU_CACHE_SIZE = 1


class MacBook(namedtuple("MacBook", "title link price specs")):
    def __str__(self):
        return "<[%s] '%s' (%s)>" % (self.price, self.title, self.link)
