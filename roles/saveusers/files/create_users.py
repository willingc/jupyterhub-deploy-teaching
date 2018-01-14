"""Create users with same username, uid, and home dir as saved_users.txt."""
import pwd
import os, sys
from subprocess import check_call
import json


fname = './saved_users.txt'

if not os.path.isfile(fname):
    print('No saved users file found')
    sys.exit()

with open(fname, 'r') as f:
    users = json.load(f)

for username, uid in users:
    home_dir = os.path.abspath(os.path.join('.', username))
    try:
        user_data = pwd.getpwnam(username)
    except KeyError:
        cmd = ['adduser', '-q', '--uid', str(uid),
               '--no-create-home', '--home', home_dir,
               '--gecos', '""', '--disabled-password', username]
        if os.path.isdir(home_dir):
            cmd.append('--no-create-home')
        print('Creating user: {}'.format(' '.join(cmd)))
        try:
            check_call(cmd)
        except CalledProcessError:
            print('Error in creating user: {}'.format(' '.join(cmd)))
    else:
        if user_data.pw_uid == uid and user_data.pw_dir == home_dir:
            print('User already exists: {}'.format(username))
        else:
            print("User exists, but uid or home dir don't match", uid,
                  user_data.pw_uid, home_dir, user_data.pw_dir)
