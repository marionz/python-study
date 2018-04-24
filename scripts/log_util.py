import platform
import os
import logging


def setup_log_and_return_log_file():
    _log_file = ''
    platform_str = platform.platform()
    if platform_str.startswith('Linux'):
        _log_file = os.path.join('/media/leizhang/Data/workspace/', 'logs', 'my_log.log')

    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s:    %(levelname)s:  %(message)s',
        filename=_log_file,
        filemode='+a',
    )
    logging.info('The log is written to:' + _log_file)
    return _log_file


if __name__ == '__main__':
    logging.debug('this is a debug mode')
    logging.warning('Some problem may happen here')
    logging.error('A fatal error happened here')
