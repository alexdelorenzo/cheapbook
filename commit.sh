#!/bin/bash

###
### ./commit.sh "Your commit message goes here"
###


commit_msg=$1

commit_files=("__init__.py" "base.py" "check_apple.py" "parse.py" "commit.sh" "requirements.txt" "send.py" "README")
private_info=("EMAIL_USERNAME" "EMAIL" "EMAIL_PASSWORD" "RECEIVER_EMAIL" "SMTP_SERVER")
private_file="base.py"


replace_with_nullstring() {
  vars=$1
  filename=$2

  for var in "${private_info[@]}"
  do
    sed -i 's/\('${var}' \=\).*$/\1 ""/' ${filename}
  done
}

replace_and_backup_private_info() {
    cp ${private_file} ${private_file}.bak
    replace_with_nullstring private_info ${private_file}
    sed -i 's/\(SEND_EMAIL \=\).*$/\1 False  # if True, fill out info below/' ${private_file}
}

check_if_sufficient() {
    cat ${private_file}

    echo -n "Sufficiently sanitized names and personal info? [y/N]: "
    read sufficient

    case ${sufficient} in
        [y|Y|yes|Yes|YES|y])
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
        git add "$var"
    done

    git commit -m "$commit_msg"
}

restore () {
    mv ${private_file}.bak ${private_file}
}

main() {
    replace_and_backup_private_info
    check_if_sufficient
    restore
}

main


