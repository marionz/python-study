from my_python.my_back import Backup

source_folder = '/home/leizhang/data/important'
source_files = ('firefox.py', 'for.py', 'function_study.py')
target_location = '/home/leizhang/data/backup'

my_object = Backup(source_folder, source_files, target_location)
my_object.backup()
my_object.get_file_name()

my_object1 = Backup('1', '2', '3')
print(Backup.backup_times)

my_object2 = Backup('3', '4', '5')
Backup.backup_times = 2

print(Backup.backup_times)

print(Backup.__doc__)
print(my_object1.__init__.__doc__)
print(Backup.backup.__doc__)


