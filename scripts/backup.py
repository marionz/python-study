import os
import time

source_folder = '/home/leizhang/data/important'
source_files = ('firefox.py', 'for.py', 'function_study.py')
target_location = '/home/leizhang/data/backup'
current_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
target_name = 'important_files_backup_{}.tar.gz'.format(current_time)


if not os.path.isdir(target_location):
    os.makedirs(target_location)

target_file = target_location + os.sep + target_name
command = 'cd {} && tar -czvf {} {}'.\
    format(source_folder, target_file, ' '.join(source_files))
os.system(command)
