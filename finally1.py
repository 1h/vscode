import sys
import logging


def for_each_line(file, do_action):
    try:
        for line in file:
            do_action(line)
    except:
        logger = logging.getLogger(__name__)
        logger.exception('未處理的例外')
        raise
    finally:
        file.close()


try:
    file = open(sys.argv[1], 'r')
    for_each_line(file, lambda line: print(int(line) + 10, end=''))
except IndexError:
    print('請提供檔案名稱')
    print('範例：')
    print('    python3.5 read.py your_file')
except FileNotFoundError:
    print('找不到檔案 {0}'.format(sys.argv[1]))
except ValueError:
    print('檔案中每一行，必須是代表整數的字串')
