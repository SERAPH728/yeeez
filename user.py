import os , requests , random 
from rich.panel import Panel as r_pl
from rich.console import Console
cons = Console()
#---------الالوان--------------
AB_A="\033[1;97m" # ابيض خط عربض
RS='\033[30m' #رصاصي
AH_F='\033[31m'   #احمر فاتح
AKH_F='\033[32m' #اخضر فاتح
AS_T='\033[33m'#اصفر طوخ
SM='\033[34m'  #سمائي
BN='\033[35m'#بنفسجي
AZ_T='\033[36m'  #ازرك طوخ
AB_KH='\033[37m' #ابيض خط خفيف
AH_T='\033[91m'  #احمر طوخ
AKH_T='\033[92m'#اخضر طوخ
AS_F='\033[93m'    #اصفر فاتح
WR='\033[95m'      #وردي
BR = '\x1b[38;5;208m' #برتقالي
AH2 = '\x1b[38;5;204m' 
AS2 = '\x1b[38;5;220m'
MJ = '\x1b[38;5;193m'
MJ2 = '\x1b[38;5;216m'
MJ3 = '\x1b[38;5;190m'
MJ4 = '\x1b[38;5;106m'
#---------/الالوان--------------
ce = '%s( ? )%s '%(AH2,AB_KH)
class sufiTool:
    def __init__(self):
        self.good = 0 
        self.bad = 0
        self.block = 0
        self.Rq_S = requests.Session()
    def sufiGO(self):
        self.Logosufi()
        self.TB = input(
            ce+
            '%sEnter %syour Token bot > %s'%(AKH_F,AB_KH,WR)
        )
        self.IT = input(
            ce+
            '%sEnter %syour ID telegram > %s'%(AKH_F,AB_KH,WR)
        )
        while True:
            self.run_tool()
    def ch_api(self,usernm):
        rAeg2 = requests.Session()
        rs3 = rAeg2.get('https://www.instagram.com/accounts/login/')
        ctk = rs3.text.replace("\\", "").split('csrf_token\":\"')[1].split('"')[0]
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50",
            "x-csrftoken": ctk,
            "x-ig-www-claim": "0",
        }
        rs3 = rAeg2.post(
            "https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/",
            headers=headers,
            data={
                'email': '',
                'first_name': '',
                'username': usernm,
                'opt_into_one_tap': 'false'
            }
        )
        headers.update({"x-ig-set-www-claim": rs3.headers["x-ig-set-www-claim"]})
        headers.update({"x-csrftoken": rs3.cookies.get("csrftoken")})
        try:
            if rs3.json()['errors']['username'][0]['code']=="username_is_taken":
                return {'result':'BAD'}
        except KeyError:
            rAeg2 = requests.Session()
            rs3 = rAeg2.get('https://www.instagram.com/accounts/login/')
            ctk = rs3.text.replace("\\", "").split('csrf_token\":\"')[1].split('"')[0]
            headers = {
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50",
                "x-csrftoken": ctk,
                "x-ig-www-claim": "0",
            }
            rs3 = rAeg2.post(
                "https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/",
                headers=headers,
                data={
                    'email': '',
                    'first_name': '',
                    'username': usernm,
                    'opt_into_one_tap': 'false'
                }
            )
            headers.update({"x-ig-set-www-claim": rs3.headers["x-ig-set-www-claim"]})
            headers.update({"x-csrftoken": rs3.cookies.get("csrftoken")})
            if '{"message":"","spam":true,"status":"fail"}' in rs3.text:
                return {'result':'BLOCK'}
            else:
                return {'result':'OK'}
    def clr(self):
        return os.system('clear')
    def run_tool(self):
        all_us = self.Get_user()
        for us in all_us:
            us = us['user']
            api_ch = self.ch_api(us)
            if api_ch['result']=='OK':
                DV = ' Developer : @M02MM'
                lt = ' - Username (Instagram) : {}'.format(us)
                tet2 = DV + '\n ' + lt
                requests.post(f'https://api.telegram.org/bot{self.TB}/sendMessage?chat_id={self.IT}&text={tet2}')
                self.good += 1
            elif api_ch['result']=='BLOCK':
                self.block += 1
            elif api_ch['result']=='BAD':
                self.bad += 1
            self.clr()
            print(f' {BR}[sufi:@M02MM] {AB_KH}- {AS2}{self.bad+self.block+self.good} ( {us} ){BR} | {WR} BAD : {AH_F}{self.bad} {BR}, {WR} BLOCK : {AH_F}{self.block} {BR}, {AKH_F}Available : {AKH_T}{self.good}{AB_KH}')
    def Logosufi(self):
        ia = '[bold yellow] [u]Developer[/u][/bold yellow]'
        ne = '[bold red]My telegram [red]: [bold black]@M02MM[/bold black]'
        fss = '[bold red]My telegram channel [red]: [bold black]@vvvvvfvv[/bold black]'
        fgg = '[bold red]Tool [red]: [bold black]Check usernames in Instagram[/bold black]'
        infoacc = '%s\n%s\n%s'%(ne,fss,fgg)
        cons.print(r_pl(infoacc,title=ia,style='cyan'))
    def Get_user(self):
        list_user = []
        __ = 'qwertyuiopasdfghjklzxcvbnm'
        for ___ in range(50):
            _1 = ''.join(random.choice(__) for _0 in range(1))
            _2 = ''.join(random.choice(__) for _0 in range(1))
            _3 = ''.join(random.choice(__) for _0 in range(1))
            _t = '.'
            _t2 = '_'
            usernames= [_1+_t+_2+_t2+_3,_1+_t2+_2+_t+_3]
            username = random.choice(usernames)
            list_user.append({'user':username})
        return list_user
if __name__ == '__main__':
    sufiTool().sufiGO()
