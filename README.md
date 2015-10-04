# cheapbook
Send email/SMS notifications about Apple's refurb stock. Also an excuse to play with Python 3.5's `typing` module.

Python 3.5+ only

## Installation
- Clone the repository
- Install dependencies `pip install -r requirements.txt`

## Configuration
Open `base.py` with a text editor. Read the comments before each variable and then configure. Save the file.

Unless you are looking for the same MacBook as I am, you will want to change the two following variables:
- `FIND_TERMS` -> a tuple of exact phrases to match in the listing
- `MODEL_REFURB_URL` -> url of the page to check

### Email
Email is disabled by default. You must supply your e-mail details and enable it.
It is assumed your SMTP server uses SSL/TLS.

To enable, open `base.py` and set `SEND_EMAIL` to `True`. You must configure the variables that follow to successfully send an email.

- `SEND_EMAIL` -> default is False, if True you must set the e-mail configuration variables: `RECEIVER_EMAIL`, `SENDER_EMAIL`, `EMAIL_USERNAME`, `EMAIL_PASSWORD`, `SMTP_SERVER` and `SMTP_PORT` must not be an empty string `""`


## Usage
- Run the program `python3.5 check_apple.py`


```
(pyfinal) alex@mba:~/Projects/cheapbook$ python3.5 check_apple.py 
Listing: <[$849.00] 'Refurbished 13.3-inch MacBook Air 1.6GHz Dual-core Intel Core i5' (http://www.apple.com//shop/product/FJVE2LL/A/refurbished-133-inch-macbook-air-16ghz-dual-core-intel-core-i5)> 

-> Sending <[$849.00] 'Refurbished 13.3-inch MacBook Air 1.6GHz Dual-core Intel Core i5' (http://www.apple.com//shop/product/FJVE2LL/A/refurbished-133-inch-macbook-air-16ghz-dual-core-intel-core-i5)>
Listing: <[$929.00] 'Refurbished 13.3-inch MacBook Air 1.4GHz Dual-core Intel Core i5' (http://www.apple.com//shop/product/GD761LL/B/refurbished-macbook-air-14ghz-dual-core-intel-core-i5)> 

-> Sending <[$929.00] 'Refurbished 13.3-inch MacBook Air 1.4GHz Dual-core Intel Core i5' (http://www.apple.com//shop/product/GD761LL/B/refurbished-macbook-air-14ghz-dual-core-intel-core-i5)>
Listing: <[$1,019.00] 'Refurbished 13.3-inch MacBook Air 1.6GHz Dual-core Intel Core i5' (http://www.apple.com//shop/product/FJVG2LL/A/refurbished-133-inch-macbook-air-16ghz-dual-core-intel-core-i5)> 

Seen: 3 @ Mon Sep 28 15:08:06 2015 Sleep: 180.0

-> Sent <[$849.00] 'Refurbished 13.3-inch MacBook Air 1.6GHz Dual-core Intel Core i5' (http://www.apple.com//shop/product/FJVE2LL/A/refurbished-133-inch-macbook-air-16ghz-dual-core-intel-core-i5)>
-> Sending <[$1,019.00] 'Refurbished 13.3-inch MacBook Air 1.6GHz Dual-core Intel Core i5' (http://www.apple.com//shop/product/FJVG2LL/A/refurbished-133-inch-macbook-air-16ghz-dual-core-intel-core-i5)>
-> Sent <[$929.00] 'Refurbished 13.3-inch MacBook Air 1.4GHz Dual-core Intel Core i5' (http://www.apple.com//shop/product/GD761LL/B/refurbished-macbook-air-14ghz-dual-core-intel-core-i5)>
-> Sent <[$1,019.00] 'Refurbished 13.3-inch MacBook Air 1.6GHz Dual-core Intel Core i5' (http://www.apple.com//shop/product/FJVG2LL/A/refurbished-133-inch-macbook-air-16ghz-dual-core-intel-core-i5)>
Seen: 3 @ Mon Sep 28 15:11:07 2015 Sleep: 180.0
Seen: 3 @ Mon Sep 28 15:14:07 2015 Sleep: 180.0
```

## License
See `LICENSE`
