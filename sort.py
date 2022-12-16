from main import test

webAddress = 'https://visualgo.net/en/sorting?slide=1'

item = [
    ['click', "id=gdpr-accept"],
    ['click', "xpath=//div[@id='overlay']/div[2]"],
    ['click', "id=create"],
    ['click', "id=userdefined-input"],
    ['type', "id=userdefined-input"],
    ['click', "xpath=//div[@id='create-userdefined-go']/p"],
]
target = ['get', "id=create-err"]
sheet_name = 'Sort'
delay_time = 2

test(webAddress, item, target, sheet_name, delay_time)
