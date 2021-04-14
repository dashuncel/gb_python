# работает из консоли

import util
import sys

params = sys.argv[1:]
for elem in params:
    print(util.currency_rates(elem))


