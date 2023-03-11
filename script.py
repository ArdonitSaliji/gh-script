import os
import datetime
import time

def add_message_to_file(file_path, message):
    with open(file_path, 'a') as file:
        file.write(message + '\n')

def push_to_github(repo_path, file_path, start_date):
    os.chdir(repo_path)
    os.system('git add .')

    for i in range(5): # How many days to add squares 5 will add 5 green squares
        date = start_date + datetime.timedelta(days=i)
        date_string = date.strftime("%Y-%m-%d")
        message = f'Added message #{i+1} on {date_string}'
        add_message_to_file(file_path, message)
        os.system('git add .')
        os.system(f'git commit --date "{date_string}" -m "{message}"')
        time.sleep(3)
        print(f'git commit --date "{date_string}" -m "{message}"')



if __name__ == '__main__':
    file_path = './file.txt'
    repo_path = '/home/ardonit/Desktop/Github/c-lang' # Your repo dir to add the commits
    start_date = datetime.datetime(2022, 3, 4) # Edit this line from where to start adding green squares
    push_to_github(repo_path, file_path, start_date)


