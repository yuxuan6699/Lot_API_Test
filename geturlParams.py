import urllib.parse
import readExcel
import readConfig as readConfig

readexcel = readExcel.readExcel().read_xls(xls_name='userCase.xlsx', sheet_name='login')
readconfig = readConfig.ReadConfig()

class geturlParams():
    def get_Url(self):
        new_url = readconfig.get_http('scheme') + '://' + readconfig.get_http('baseurl') + ':8888' + readexcel[0][1] + '?'
        return new_url


    def get_data(self):
        params = readexcel[0][2]
        url = "http://www.xxx.com/login?"
        new_url = url+params
        data = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(new_url).query))
        return data

    def get_method(self):
        method = readexcel[0][3]
        return method

if __name__ == '__main__':
    print(geturlParams().get_Url())
    print(geturlParams().get_data())
