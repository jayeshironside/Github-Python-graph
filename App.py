import os
from random import randint
from datetime import datetime, timedelta

# set start and end dates
start_date = datetime(2022, 8, 13)
end_date = datetime.now()

# calculate number of days between start and end dates
days = (end_date - start_date).days

# loop for generating 10 random commits
for i in range(10):

    # generate a random number of days between 0 and the total number of days
    days_ago = randint(0, days)

    # calculate the date for the commit
    commit_date = end_date - timedelta(days=days_ago)

    # format the date string
    date_string = commit_date.strftime('%Y-%m-%d %H:%M:%S')

    # write the commit message to file
    with open('file.txt', 'a') as file:
        file.write(date_string + '\n')

    # add and commit the changes using the date string
    os.system('git add .')
    os.system('git commit --date="' + date_string + '" -m "commit"')

# push the changes to the remote repository
os.system('git push -u origin main')
