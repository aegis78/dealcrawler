# coding=UTF-8

# parser.py
import requests

# HTTP GET Request
req = requests.get('https://beomi.github.io/beomi.github.io_old/')

# html 생성
html = req.text

header = req.headers
status = req.status_code
is_ok = req.ok