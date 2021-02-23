import requests
from bs4 import BeautifulSoup as bs
from aiogram import Bot, Dispatcher,executor, types
import time


bot = Bot(token = '1615536899:AAFqmZFOUFRu26vl7lVNoH1-4hSSvGOU3Zo')

dp = Dispatcher(bot)




async def Cra_pars():

        links = [
            'https://turbo.az/autos?utf8=✓&q%5Bmake%5D%5B%5D=&q%5Bmake%5D%5B%5D=4&q%5Bregion%5D%5B%5D=&q%5Bmodel%5D%5B%5D=&q%5Bmodel%5D%5B%5D=149&q%5Bfuel_type%5D%5B%5D=&q%5Bfuel_type%5D%5B%5D=1&q%5Bcategory%5D%5B%5D=&q%5Bgear%5D%5B%5D=&q%5Bcolor%5D%5B%5D=&q%5Btransmission%5D%5B%5D=&q%5Btransmission%5D%5B%5D=2&q%5Bmileage_from%5D=&q%5Bmileage_to%5D=&q%5Byear_from%5D=1996&q%5Byear_to%5D=2000&q%5Bprice_from%5D=&q%5Bprice_to%5D=&q%5Bcurrency%5D=azn&q%5Bengine_volume_from%5D=0&q%5Bengine_volume_to%5D=&q%5Bloan%5D=0&q%5Bbarter%5D=0&q%5Bextras%5D%5B%5D=&q%5Bsort%5D=created_at&q%5Bused%5D=&button=',
            'https://turbo.az/autos?utf8=✓&q%5Bmake%5D%5B%5D=&q%5Bmake%5D%5B%5D=4&q%5Bregion%5D%5B%5D=&q%5Bmodel%5D%5B%5D=&q%5Bmodel%5D%5B%5D=150&q%5Bfuel_type%5D%5B%5D=&q%5Bfuel_type%5D%5B%5D=1&q%5Bcategory%5D%5B%5D=&q%5Bgear%5D%5B%5D=&q%5Bcolor%5D%5B%5D=&q%5Btransmission%5D%5B%5D=&q%5Btransmission%5D%5B%5D=2&q%5Bmileage_from%5D=&q%5Bmileage_to%5D=&q%5Byear_from%5D=1996&q%5Byear_to%5D=2000&q%5Bprice_from%5D=&q%5Bprice_to%5D=&q%5Bcurrency%5D=azn&q%5Bengine_volume_from%5D=0&q%5Bengine_volume_to%5D=&q%5Bloan%5D=0&q%5Bbarter%5D=0&q%5Bextras%5D%5B%5D=&q%5Bsort%5D=created_at&q%5Bused%5D=&button=',
            'https://turbo.az/autos?utf8=✓&q%5Bmake%5D%5B%5D=&q%5Bmake%5D%5B%5D=4&q%5Bregion%5D%5B%5D=&q%5Bmodel%5D%5B%5D=&q%5Bmodel%5D%5B%5D=172&q%5Bfuel_type%5D%5B%5D=&q%5Bfuel_type%5D%5B%5D=1&q%5Bcategory%5D%5B%5D=&q%5Bgear%5D%5B%5D=&q%5Bcolor%5D%5B%5D=&q%5Btransmission%5D%5B%5D=&q%5Btransmission%5D%5B%5D=2&q%5Bmileage_from%5D=&q%5Bmileage_to%5D=&q%5Byear_from%5D=1997&q%5Byear_to%5D=2000&q%5Bprice_from%5D=&q%5Bprice_to%5D=&q%5Bcurrency%5D=azn&q%5Bengine_volume_from%5D=0&q%5Bengine_volume_to%5D=&q%5Bloan%5D=0&q%5Bbarter%5D=0&q%5Bextras%5D%5B%5D=&q%5Bsort%5D=created_at&q%5Bused%5D=&button=',
            'https://turbo.az/autos?utf8=✓&q%5Bmake%5D%5B%5D=&q%5Bmake%5D%5B%5D=4&q%5Bregion%5D%5B%5D=&q%5Bmodel%5D%5B%5D=&q%5Bmodel%5D%5B%5D=173&q%5Bfuel_type%5D%5B%5D=&q%5Bfuel_type%5D%5B%5D=1&q%5Bcategory%5D%5B%5D=&q%5Bgear%5D%5B%5D=&q%5Bcolor%5D%5B%5D=&q%5Btransmission%5D%5B%5D=&q%5Btransmission%5D%5B%5D=2&q%5Bmileage_from%5D=&q%5Bmileage_to%5D=&q%5Byear_from%5D=1997&q%5Byear_to%5D=2000&q%5Bprice_from%5D=&q%5Bprice_to%5D=&q%5Bcurrency%5D=azn&q%5Bengine_volume_from%5D=0&q%5Bengine_volume_to%5D=&q%5Bloan%5D=0&q%5Bbarter%5D=0&q%5Bextras%5D%5B%5D=&q%5Bsort%5D=created_at&q%5Bused%5D=&button=',
            'https://turbo.az/autos?utf8=✓&q%5Bmake%5D%5B%5D=&q%5Bmake%5D%5B%5D=4&q%5Bregion%5D%5B%5D=&q%5Bmodel%5D%5B%5D=&q%5Bmodel%5D%5B%5D=174&q%5Bfuel_type%5D%5B%5D=&q%5Bfuel_type%5D%5B%5D=1&q%5Bcategory%5D%5B%5D=&q%5Bgear%5D%5B%5D=&q%5Bcolor%5D%5B%5D=&q%5Btransmission%5D%5B%5D=&q%5Btransmission%5D%5B%5D=2&q%5Bmileage_from%5D=&q%5Bmileage_to%5D=&q%5Byear_from%5D=1997&q%5Byear_to%5D=2000&q%5Bprice_from%5D=&q%5Bprice_to%5D=&q%5Bcurrency%5D=azn&q%5Bengine_volume_from%5D=0&q%5Bengine_volume_to%5D=&q%5Bloan%5D=0&q%5Bbarter%5D=0&q%5Bextras%5D%5B%5D=&q%5Bsort%5D=created_at&q%5Bused%5D=&button='

        ]
        for link in links:




            r = requests.get(link,timeout=120)
            soup = bs(r.content, 'lxml')
            fin = soup.find('a',attrs={'class':'products-i-link'})['href']
            with open('cars.txt', 'r')as r:
                with open('cars.txt', 'a')as f:
                    if fin not in r.read():
                        f.write(fin + '\n')
                        await bot.send_message(1482645558, 'https://turbo.az' + str(fin))




@dp.message_handler(chat_id=484026432)
async def qwe(message):
    while True:
        await Cra_pars()


        time.sleep(600)











if __name__ =='__main__':
    executor.start_polling(dp, skip_updates=True)
















