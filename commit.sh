#!/bin/sh

cp base.py old_base.py
sed -i 's/\(EMAIL_USERNAME \=\) .*$/\1 ""/' base.py
sed -i 's/\(EMAIL \=\) .*$/\1 ""/' base.py
sed -i 's/\(EMAIL_PASSWORD \=\) .*$/\1 ""/' base.py
sed -i 's/\(RECEIVER_EMAIL \=\) .*$/\1 ""/' base.py
sed -i 's/\(SMTP_SERVER \=\) .*$/\1 ""/' base.py
sed -i 's/\(SEND_EMAIL \=\) .*$/\1 False/' base.py
cat base.py
git add base.py check_apple.py parse.py commit.sh requirements.txt send.py
git commit -m $1
mv old_base.py base.py


