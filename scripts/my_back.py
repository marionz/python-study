import time
import os


class Backup:
    """
    Used to backup files
    """

    backup_times = 0

    def __init__(self, source_folder, source_files, target_location):
        """
        Used to init Backup class

        :param source_folder: source folder
        :param source_files: source files
        :param target_location: target location, if not exist, create one directly
        """
        self.source_folder = source_folder
        self.source_files = source_files
        self.target_location = target_location

    @classmethod
    def get_file_name(cls):
        timestamp = time.strftime("%Y%m%d%H%M%S", time.localtime())
        file_name = 'important_files_backup_{}.tar.gz'.format(timestamp)
        return file_name

    def backup(self):
        """
        Backup source files in source location, create a tar.gz file and store it in target location
        :return: if success then return True, otherwise return False
        """
        if not os.path.isdir(self.target_location):
            os.makedirs(self.target_location)

        target_file = self.target_location + os.sep + Backup.get_file_name()

        command = 'cd {} && tar -czvf {} {}'. \
            format(self.source_folder, target_file, ' '.join(self.source_files))

        if os.system(command) == 0:
            return True
        else:
            return False

