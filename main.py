import os

import pytest
import sys
#запускает все тесты и записывает результат прохождения в фаил report.xml в корне проекта
pytest.main('--junitxml={path}/report.xml'.format(path=os.path.dirname(os.path.realpath(__file__))))
sys.exit(0)
