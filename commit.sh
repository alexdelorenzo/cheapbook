#!/bin/bash

msg=$1
commit_files=("base.py" "check_apple.py" "parse.py" "commit.sh" "requirements.txt" "send.py")
private_info=("EMAIL_USERNAME" "EMAIL" "EMAIL_PASSWORD" "RECEIVER_EMAIL" "SMTP_SERVER")
private_file="base.py"
backup_file="old.py"


replace_with_nullstring() {
  vars=$1
  filename=$2

  for var in "${private_info[@]}"
  do
    sed -i 's/\('$var' \=\) .*$/\1 ""/' $filename
  done
}

replace_and_backup_private_info() {
    cp $private_file $backup_file
    replace_with_nullstring private_info $private_file
    sed -i 's/\(SEND_EMAIL \=\) .*$/\1 False/' $private_file
}

check_if_sufficient() {
    cat base.py
    echo -n "Sufficiently sanitized names and personal info? [y/N]: "
    read sufficient

    case $sufficient in
        [y|Y|yes|Yes|YES])
            commit
            ;;
        *)
            echo "Dropped changes, did not add or commit changes."
            ;;
    esac
}

commit() {
    for var in "${commit_files[@]}"
    do
        git add $var
    done
    git commit -m "$msg"
}

restore () {
    mv $backup_file $private_file
}

main() {
    replace_and_backup_private_info
    check_if_sufficient
    restore
}

main


