'''
2. * (вместо 1) Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) для получения информации вида:
(<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>, <response_size>), например:

raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')
'''
import re

with open('nginx_logs.txt') as f:
    data = []
    TEST_LINE = re.compile(r'(?P<IP>(\d{,3}\.){3}\d{,3}) - - .(?P<data>\d{,2}/\w+/\d{4}(:\d{2}){3}).+(?P<req>GET|PUT|POST|DELETE)\s+'
                           r'(?P<address>(/\w+){,4})\sHTTP/1\.1\" (?P<port>(\d){,4})'
                          )
    for line in f:
        tested_line = TEST_LINE.match(line)
        if tested_line:
            itog_str = f'{tested_line.group("IP")}, {tested_line.group("data")}, {tested_line.group("req")}, ' \
                       f'{tested_line.group("address")}, {tested_line.group("port")}'
            print(itog_str)



