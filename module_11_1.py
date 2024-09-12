import requests
import pandas
import matplotlib.pyplot as plt

from pprint import pprint

URL = 'https://www.cbr-xml-daily.ru/daily_json.js'


r = requests.get(URL)
json_flag = False
if r.ok:
    try:
        r = r.json()
    except requests.exceptions.JSONDecodeError as e:
        print('Содержимое ответа не в формате json.', 'От источника был получен следующий ответ:',
              r, sep='\n')
    else:
        json_flag = True
pprint(r['Valute'])



if json_flag:
    field_list = ['CharCode', 'NumCode', 'Name', 'Nominal', 'Value']
    val_list = []
    for i in r['Valute']:
        line_ = []
        for j in field_list:
            line_.append(r['Valute'][i][j])
        val_list.append(line_)

    val_list.sort(key=lambda x: -x[3])
    pprint(val_list)


    df1 = pandas.DataFrame(val_list, columns=field_list)
    with pandas.ExcelWriter(f"val_{r['Date'][0:10]}.xlsx") as writer:
        df1.to_excel(writer, sheet_name=str(r['Date'][0:10]))



if json_flag:
    chart_data = pandas.read_excel(f"val_{r['Date'][0:10]}.xlsx")
    pprint(chart_data)
    fig, ax = plt.subplots()

    ax.set_title('Курсы валют')
    ax.set_xlabel('Коды валют')
    ax.set_ylabel('Курс')
    ax.scatter(chart_data['NumCode'], chart_data['Value'], c=chart_data['Nominal'], s=chart_data['Nominal'])
    plt.show()