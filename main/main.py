from Ui_UI_simple import *
from git_dns import GetDNS
import sys, os, platform

        
class GetDnsUI(GetDNS):
    def __init__(self, domain_name_list=None):
        super().__init__(domain_name_list=domain_name_list)
        self.pg_bar_value = 1


    def show_UI(self):
        app = QApplication(sys.argv)
        self.ui_app = Ui_MainWindow()
        w = QMainWindow()
        self.ui_app.setupUi(w)
        w.show()

        self.ui_app.get_b.clicked.connect(self.get_ip_domain)
        self.ui_app.flush_dns_b.clicked.connect(
            lambda a: os.system("ipconfig /flushdns"))
        self.ui_app.open_hosts_path_b.clicked.connect(self.open_hosts_path_b_func)


        sys.exit(app.exec_())


    def get_ip(self, domain_name):
        self.ui_app.pg_bar.setValue(self.pg_bar_value)
        self.pg_bar_value += 1
        return super().get_ip(domain_name)


    def open_hosts_path_b_func(self):
        if platform.system().lower() == 'windows':
            os.system('start explorer C:\WINDOWS\system32\drivers\etc')

        elif platform.system().lower() == 'darwin':
            os.system("open /etc/hosts")
        else:
            print('自行Bing查找hosts路径哈')


    def get_ip_domain(self):
        
        self.get_dns_domain_name_list = [i for i in self.ui_app.domain_text.text().split(' ') if i]

        if self.get_dns_domain_name_list:
            self.domain_name_list = self.get_dns_domain_name_list

        self.total = len(self.domain_name_list)
        self.ui_app.pg_bar.setRange(0, self.total)
        
        ip_domain = '\n'.join(
            list(map(self.get_ip, [domain_name for domain_name in self.domain_name_list])))

        self.ui_app.output_text.setPlainText(ip_domain)


    def main(self):
        self.show_UI()


if __name__ == '__main__':
    dns = GetDnsUI()
    dns.main()
