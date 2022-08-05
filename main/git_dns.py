#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   git_dns.py
@Time    :   2022/05/29 23:21:02
@Author  :   Donjae 
@Version :   1.0
@Contact :   dr_wangdj@outlook.com
'''


import os
import platform
import re
import requests as req
from lxml import etree
from tqdm import tqdm


class GetDNS:
    def __init__(self, domain_name_list = None):
        '''
        default:github ip address
        '''
        self.pwd_path = os.getcwd()
        if not domain_name_list:
            domain_name_list = ['github.githubassets.com', 'camo.githubusercontent.com',
                                'github.map.fastly.net', 'github.global.ssl.fastly.net',
                                'github.com', 'api.github.com', 'raw.githubusercontent.com',
                                'user-images.githubusercontent.com', 'favicons.githubusercontent.com',
                                'avatars5.githubusercontent.com', 'avatars4.githubusercontent.com',
                                'avatars3.githubusercontent.com', 'avatars2.githubusercontent.com',
                                'avatars1.githubusercontent.com', 'avatars0.githubusercontent.com']

        p = r'[httpHTTPs]{,6}://'
        self.domain_name_list = [re.sub(p, '', url)
                                 for url in domain_name_list]
        self.ip_domain = ''
        self.pd_bar = tqdm(total=len(self.domain_name_list))
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
            'referer': 'https://www.ipaddress.com/',
            }


    def get_ip(self, domain_name):
        url = "https://ipaddress.com/website"
        if domain_name.endswith('/'):
            domain_name = domain_name[:-1]
        if domain_name.startswith('http'):
            domain_name = domain_name.split('//')[1]
        url = '/'.join([url, domain_name])

        resp = req.get(url, headers=self.headers)
        if resp.status_code < 400:
            text = resp.text

            tree = etree.HTML(text=text)
            ip_list = tree.xpath(
                '/html/body/div[1]/main//section/table/tbody/tr[6]/td/ul/li/text()')
            if ip_list:
                if len(ip_list) > 1:
                    list_ = []
                    for ip in ip_list:
                        if ':' in ip:
                            continue
                        ip_domain_name = '   '.join([ip, domain_name])
                        list_.append(ip_domain_name)
                    
                    domain_hosts = '\n'.join(list(set(list_)))
                else:
                    ip_list.append(domain_name)
                    domain_hosts = '   '.join(ip_list)
            self.pd_bar.update(1)
            return domain_hosts
        else:
            return f'{domain_name}: {resp.status_code} not found!'


    def main(self):
        
        if not os.path.exists('./GetDNS'):
            os.mkdir('./GetDNS')

        os.chdir(r'./GetDNS')
        with open(os.path.join(self.pwd_path, 'GetDNS', 'git_hosts.txt'), 'w', encoding='utf-8') as f:
            f.write('\n'.join(list(map(self.get_ip, [domain_name for domain_name in self.domain_name_list]))))

        if platform.system().lower() == 'windows':
            os.system("start explorer .\GetDNS\git_hosts.txt")
            os.system('start explorer C:\WINDOWS\system32\drivers\etc')
            input('请打开目录下的git_hosts.txt，并修改hosts，改好之后点回车。')
            os.system('ipconfig /flushdns')

        else:
            input('请打开GetDNS目录下的git_hosts.txt，并修改hosts')

if __name__ == '__main__':
    # url_input = input('请输入需要查询的域名(分隔by:" "(空格 Space))：')
    if ' ' in url_input:
        url_name_list = url_input.split(' ')
    else:
        url_name_list = url_input

    g = GetDNS(url_name_list)
    g.main()
