import csv
import time
import requests
from bs4 import BeautifulSoup
firstPage = 2
csv_file = open('carinfo.csv' , 'w' , newline='\n')
obj = csv.writer(csv_file)
obj.writerow(['Title' , 'Mileage' , 'Year' , 'Engine' , 'Location' , ])
while firstPage <7:

    url = f'https://www.beforward.jp/stocklist/client_wishes_id=/description=/make=106/model=/fuel=/fob_price_from=9000/fob_price_to=/veh_type=/steering=Left/mission=/mfg_year_from=2010/mfg_month_from=/mfg_year_to=2023/mfg_month_to=/mileage_from=/mileage_to=/cc_from=/cc_to=/showmore=/drive_type=/color=/stock_country=/area=/seats_from=/seats_to=/max_load_min=/max_load_max=/veh_type_sub=/view_cnt=50/page={str(firstPage)}/sortkey=n/sar=/from_stocklist=1/keyword=/kmode=and/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text , 'html.parser')
    car_page = soup.find('table' , class_='stocklist-row-wrap')
    car_blocks = car_page.findAll('td' , class_='stocklist-col description-col')
    price = car_page.findAll('td', class_='stocklist-col price-col')



    for each in car_blocks:

        car_link = each.find('p' , class_='make-model')
        car_name = car_link.find('a' , class_='vehicle-url-link').text
        car_name = car_name.split()
        title = (car_name[1] + ' ' + car_name[2])
        # print(title)

    # ავტომობილის დასახელება


    # ავტომობილის გარბენი

        miles = each.find('p' , class_='val').text
        miles = miles.split()[0]
        # print(miles)

    # ავტომობილის გამოშვების წელი

        car_year = each.find('td' , class_= 'basic-spec-col basic-spec-col-bordered year')
        car_year_close = car_year.find('p' , class_= 'val').text
        car_year_close = car_year_close.split()[0]
        # print(car_year_close)

    # ავტომობილის ძრავი

        engine = each.find('td' , 'basic-spec-col basic-spec-col-bordered engine')
        engine_res = engine.find('p' , 'val').text
        engine_res = engine_res.split()[0]
        # print(engine_res)

    #ავტომობილის მდებარეობა

        place = each.find('p' , class_='val stock-area')
        country = place.find('span').text
        country = country.split()[0]
        # print(country)

        obj.writerow([title, miles, car_year_close, engine_res, country, ])

    firstPage += 1
    time.sleep(18)

