import sys
from make_config import make_config_file
try:
    from config import config
except ImportError:
    make_config_file()
    sys.exit()
from post_text import post_text


if __name__ == '__main__':
    post_text()
