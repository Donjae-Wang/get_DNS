import requests as req
from lxml import etree
import os, platform
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


        self.domain_name_list = domain_name_list
        self.ip_domain = ''
        self.pd_bar = tqdm(total=len(self.domain_name_list))


    def get_ip(self, domain_name):

        url = "https://ipaddress.com/website"

        url = '/'.join([url, domain_name])
        resp = req.get(url)
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
    url_input = input('请输入需要查询的域名(分隔by:" "(空格 Space))：')
    if ' ' in url_input:
        url_name_list = url_input.split(' ')
    else:
        url_name_list = url_input

    g = GetDNS(url_name_list)
    g.main()