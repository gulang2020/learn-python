# encoding: utf-8
"""
@author: 
@contact: 
@time: 2020/8/4 14:23
@file: cookie_swap.py
@desc: 
"""

if __name__ == '__main__':
    b = '_ga=GA1.2.1051924338.1596293046; _gid=GA1.2.1111790943.1596293047; __gads=ID=221133d840046023:T=1596293140:S=ALNI_MZL5-P7Qdfcm9nLC9pl96HGFTObpQ; footprints=eyJpdiI6IitDMXhsUFZkMEVXRVhPRHBuVzY5bFE9PSIsInZhbHVlIjoiT3NUT1RxSkVDTERSZmFqY243WmxHY0hZeEc3WmZXQmtYaVd4MWt5Z293bnhteFJzYlhcL0kyRXZBa0ErczFYQkMiLCJtYWMiOiJlOWJhYzFiYjI1MzJmNmYwNDUzYzBlZmY2NTg4MzljZTYxMTAyMWY4YTJiOGVmYTM4YTlkYTQ3MmUwYjgxM2I3In0%3D; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6IjR6MkRNKzdJTEhxTHlcLzI0TG1rMUlnPT0iLCJ2YWx1ZSI6ImdTNDBQS0pRdVlSWDNcL0Q3RmhneVdLRWErdHJJZUVpa1JodGtXUm9CMzF2elZ2c1FwV0RmQ0lUTkc5NFVjVStEZElcL3VJVW8yN3Z4bWZJSGN5YXAyQTFCUUMrTVRZOGJiYlMyQnYrNkhoVlwvWDVRbGhQOFk0OUZkM3dZQ0tReHdYQXlYYXZad1J0ZHhmSFFma2g0bjRrbG95cFgrV09WaGtvRFltOTVGRXdmcz0iLCJtYWMiOiJhOTU4MGRhNjU1Zjc2MjgyNjBkYzdiNzQwYTc4YjBkOWVhY2Y4YTc1MTA4MjQzNDVjNTljYTA4N2ViN2E0ZmU0In0%3D; Hm_lvt_020fbaad6104bcddd1db12d6b78812f6=1596374824,1596374882,1596410690,1596442509; Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6=1596443963; XSRF-TOKEN=eyJpdiI6IkV6b1BHVWVpV0x1c2NCOGFCRlJ4MkE9PSIsInZhbHVlIjoidG5aOVBDR1hpQzFYdVwvSDc5Y09INjFJZjNRdHhGWHhWN2dmRVwvdnZSN04ycVwvMlwvOGxhN0tkVXBIaHA3ZXVsc2UiLCJtYWMiOiIyZjcwYTM0ZWU4NDUwN2YzM2U5MWE5ZDBkYjI2ODBkYmE5ODk1NjhhNDE1ZGEyOWM3YzU0ODExNDhjYmNmNmRhIn0%3D; glidedsky_session=eyJpdiI6ImdsSlRuendHYUcwbUR3VjVicHd2Nmc9PSIsInZhbHVlIjoidmlCWWlFdGpLWHVWMUpRY3V0RmU1d1F0QUhYZHV4d1prS0RrRmswOGpnSUtHbEJoWWhhTEJscGtQMjVHK252RSIsIm1hYyI6IjMwZWMzMGYzZmExYzYwMWNhZmE1ZTg0NDExNjU5MzQ5N2E4ZWMxZWJhNTM3ZDY5NGJiZDI1OGYwNjhkODI4MDQifQ%3D%3D'
    cookie = {}
    for line in b.split(';'):
        key, value = line.split('=', 1)
        cookie[key] = value
    print(cookie)