from bs4 import BeautifulSoup as xe
from requests_html import HTMLSession
import os

akun = [
    "0x58C9Fe4170FDb3DDCC82dBC2470c120846643198",
    "0xe53897541C3d2C38Dc3faACe03FeBf8afdE28b64",
    "0xe7E4E5eB8641D7a72a2E5697c8C87723BDDA828b",
    "0xbf0A9161c8627E52240Ca4636Fe73fBCe4df44d5",
    "0x534384c75F8DC31821AcC7aBD00788B934535393",
    "0x574EdCbe3145Fd00eEEF255AbD8E08564d1cfE1A",
    "0xB18ecc1A79c355C0992E45455E12e9e343249FD4",
    "0x354d295CaB6Fcf4E68EA17A01872715e1B42656f",
    "0x5f6A0403359F01Fb89873FE94030aaCd12E5F64e",
    "0xa836DC87A1be5A658a6F256bD64469424A81C3F6",
    "0xBB4173985fdf519Ee1137186aCBC07aeEFc80981",
    "0xc57b24231Ce9357C8dA8bBe6d9ab0603fe8015E6",
    "0xA65A6bc7258245B6E828e0211Cc2BfC5ea52c403"
]

def main(__url__,Choose):
    for looping in range(len(akun)):
        session = HTMLSession()
        page = session.get(url=__url__+akun[looping])
        soup = xe(page.content, 'html.parser')
        addressHeader = soup.find("span", class_="text-size-address text-secondary text-break mr-1").text
        address = soup.findAll("a", class_="link-hover d-flex justify-content-between align-items-center", href=True)
        values = soup.findAll("div", class_='col-md-8')
        est = values[0].text
        try:
            JumlahToken = soup.find("span", class_="badge badge-primary mx-1").text
            IsiToken = soup.findAll("span", class_="list-amount link-hover__item hash-tag hash-tag--md text-truncate")
            print("\nAddress ke-{} -> {}".format(looping,addressHeader))
            print("Token:")
            if Choose in [1,3,4,5]:
                for i in range(int(JumlahToken)):
                    print("   [{}] {} Sc -> {}".format(i,IsiToken[i].text,address[i]["href"].replace('?a='+akun[looping],"").replace('/token/', '')))
            elif Choose == 2:
                for i in range(int(JumlahToken)):
                    print("   [{}] {} Sc -> {}".format(i,IsiToken[i].text,address[i]["href"].replace('?a='+akun[looping].lower(),"").replace('/token/', '')))
            print("\nEstimasi: {}".format(est))
            print("-"*70)
        except AttributeError:
            try:
                print("\n\nAddress ke-{} -> {}\n [!] Tidak ada token".format(looping,addressHeader))
                print("-"*70)
            except:
                error_handle = soup.find("h1", class_="h4 mb-0").text.strip()
                print(error_handle+": "+akun[looping])

def menu():
    os.system('cls')
    print('[1] BSC\n[2] ETH\n[3] POLYGON\n[4] HECO Chain\n[5] FANTOM')
    a = int(input(">:"))
    if a == 1:
        os.system('cls')
        print("\n --- Binance Chain -- ")
        main('https://bscscan.com/address/',Choose=1) 
    elif a == 2:
        os.system('cls')
        print("\n --- Ethereum -- ")
        main('https://etherscan.com/address/',Choose=2)
    elif a == 3:
        os.system('cls')
        print("\n --- Polygon Matic -- ")
        main('https://polygonscan.com/address/',Choose=3)
    elif a == 4:
        os.system('cls')
        print("\n --- Houbi ECO Chain -- ")
        main('https://hecoinfo.com/address/',Choose=4)
    elif a == 5:
        os.system('cls')
        print("\n --- Fantom -- ")
        main('https://ftmscan.com/address/',Choose=5)
    else:
        print('[!] Wrong')

    i = input("Back? (y/t)")
    if i in ['y','ya','Y']:
        menu()


if __name__ == '__main__':
    menu()
