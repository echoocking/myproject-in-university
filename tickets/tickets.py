# coding: utf-8

"""
train tickets

Usage:
    tickets [-gdtkz] <from> <to> <date>

Options:
    -h 	显示帮助
    -g 	高铁
    -d  动车
    -t  特快
    -k  快速
    -z  直达

Example:
    tickets 南京 北京 2016-07-01
    tickets -dg 南京 北京 2016-07-01
"""

from docopt import docopt
from stations import stations_list
import requests
from prettytable import PrettyTable
#定义一个接收数据的对象


def cli():
    arguments = docopt(__doc__)
    from_station = stations_list.get(arguments['<from>'])
    to_station = stations_list.get(arguments['<to>'])
    date = arguments['<date>']
    url = 'https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate={}&from_station={}&to_station={}'.format\
        (
            date, from_station, to_station
        )
    r = requests.get(url, verify=False)
    # print(r.json()['data'])
    print(r.json()['data'])
    rows = r.json()['data']['datas']

    header = '车次 车站 时间 历时 商务 一等 二等 软卧 硬卧 软座 硬座 无座 其他'.split()
    detil_Dis = PrettyTable(header)
    detil_Dis.align['车次'] = 1
    detil_Dis.padding_width = 1
    #匹配 单引号之间的内容这样写  \'([^\']*)\'   哈哈哈哈哈ßß~~
    for row in rows:
        print(row)
        train = [
            row.get('station_train_code'),
            '\n'.join([row.get("from_station_name"),
                       row.get("to_station_name")
                       ]),
            '\n'.join([row.get("start_time"),
                       row.get("arrive_time")
                       ]),#这里是将出发站到目的站的信息通过列表储存,然后通过join转换为str并且在在两个数据之间加入换行符
        # Column: '历时'
            row.get("lishi"),
            # Column: '商务'
            row.get('swz_num'),
            # Column: '一等'
            row.get('zy_num'),
            # Column: '二等'
            row.get('ze_num'),
            # Column: '软卧'
            row.get('rw_num'),
            # Column: '硬卧'
            row.get('yw_num'),
            # Column: '软座'
            row.get('rz_num'),
            # Column: '硬座'
            row.get('yz_num'),
            # Column: '无座'
            row.get('wz_num'),
            # 其他
            row.get("qt_num"),
        ]
        detil_Dis.add_row(train)
        # ifreObj = re.compile('\'rw_num\': \'(无|--|[0-9]+)\', \'zy_num\': \'(无|--|[0-9]+)\', \'to_station_name\': \'([\u4e00-\u9fa5]+)\', \'qt_num\': \'(无|--|[0-9]+)\', \'yz_num\': \'(无|--|[0-9]+)\', \'yb_num\': \'(无|--|[0-9]+)\', \'sale_time\': \'([0-9]+)\', \'end_station_name\': \'([\u4e00-\u9fa5]+)\', \'swz_num\': \'(无|--|[0-9]+)\', \'station_train_code\': \'Z108\', \'from_station_name\': \'([\u4e00-\u9fa5]+)\', \'lishi\': \'([0-9]+:[0-9]+)\', \'tz_num\': \'(无|--|[0-9]+)\',  \'ze_num\': \'(无|--|[0-9]+)\', \'arrive_time\': \'([0-9]+:[0-9]+)\', \'yw_num\': \'(无|--|[0-9]+)\',  \'wz_num\': \'(无|--|[0-9]+)\', \'rz_num\': \'(无|--|[0-9]+)\', \'start_time\': \'([0-9]+:[0-9]+)\'')
    print(detil_Dis)
        # reObj.findall()
    # reObj.findall(rows)

if __name__ == '__main__':
    cli()

    '''
(tickets)╭─echoocking@localhost /Volumes/DEV/tickets
╰─➤  python3 tickets.py 北京 赣州 2016-12-5
/Volumes/DEV/tickets/lib/python3.4/site-packages/requests/packages/urllib3/connectionpool.py:843: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
  InsecureRequestWarning)
Traceback (most recent call last):
  File "tickets.py", line 83, in <module>
    cli()
  File "tickets.py", line 40, in cli
    rows = r.json()['data']['datas']
TypeError: 'int' object is not subscriptable

这里的错误是因为没有构造好数据  12-5的数据不被解析 所以返回的 值是 错误信息 所以导致  datas的值为空或者其他 反正就不是正常的值了
    python3 tickets.py 北京 赣州 2016-12-05   这个是正确的方案
        '''