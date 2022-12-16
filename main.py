import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd
from openpyxl import load_workbook

filename = './TestCase.xlsx'
result_path = os.path.realpath(filename)

driver = webdriver.Chrome(ChromeDriverManager().install())

def test(webAddress, item, target, sheet_name, delay_time):
    input = pd.read_excel(filename, sheet_name=sheet_name, engine='openpyxl')
    for inp in range(len(input)):
        data = str(input["Input"][inp]).split("#")
        if data[0] == 'nan':
            data[0] = ''
        driver = webdriver.Chrome(executable_path="chromedriver.exe")
        driver.get(webAddress)
        driver.maximize_window()
        time.sleep(delay_time)

        for i in item:
            if i[0] == 'sleep':
                time.sleep(i[1])
                continue

            index = i[1].find('=')
            type = i[1][:index]
            adr = i[1][index + 1:]

            if i[0] == 'click':
                driver.find_element(type, adr).click()
            elif i[0] == 'type':
                input_field = driver.find_element(type, adr)
                driver.execute_script("arguments[0].value = ''", input_field)
                print("Input: " + data[0])
                input_field.send_keys(data[0])
                data = data[1:]


            time.sleep(delay_time)

        index = target[1].find('=')
        type = target[1][:index]
        adr = target[1][index + 1:]
        result = driver.find_element(type, adr).text
        print("Got: ", str(result))
        input["Got"][inp] = str(result)
        if(input['Got'][inp] == input['Expect'][inp] or result == "" and input['Expect'][inp] == "Test Passed"):
            input['Result'][inp] = "Passed"
        else:
            input['Result'][inp] = "Failed"
        # time.sleep(5)
        driver.quit()

    book = load_workbook(result_path)
    writer = pd.ExcelWriter(result_path, engine = 'openpyxl')
    writer.book = book

    input.to_excel(writer, sheet_name+"_Result", index=False)
    writer.close()


# create
# webAddress = 'https://visualgo.net/en/sorting?slide=1'

# item = [
#     ['click', "id=gdpr-accept"],
#     ['click', "xpath=//div[@id='overlay']/div[2]"],
#     ['click', "id=create"],
#     ['click', "id=userdefined-input"],
#     ['type', "id=userdefined-input"],
#     ['click', "xpath=//div[@id='create-userdefined-go']/p"],
# ]
# target = ['get', "id=create-err"]
# sheet_name = 'Sort'
# delay_time = 0

# test(webAddress, item, target, sheet_name)
