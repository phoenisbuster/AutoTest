from main import test

webAddress = 'https://visualgo.net/en/list?slide=1'

itemCreate = [
    ['click', "id=gdpr-accept"],
    ['click', "xpath=//div[@class='electure-end']"],
    ['click', "id=create"],
    ['click', "id=create-from-arr"],
    ['type', "id=v-create-arr"],
    ['click', "id=createuserdefined-go"],
    ['click', "id=go-to-end"],
]
target = ['get', "id=create-err"]
sheet_name = 'LinkedList_Create'
delay_time = 1

test(webAddress, itemCreate, target, sheet_name, delay_time)

itemCreate = [
    ['click', "id=gdpr-accept"],
    ['click', "xpath=//div[@class='electure-end']"],
    ['click', "id=insert"],
    ['click', "id=insert-kth"],
    ['type', "id=v-insert-kth"],
    ['click', "id=insertkth-go"],
    ['click', "id=go-to-end"],
]
target = ['get', "id=insert-err"]
sheet_name = 'LinkedList_Insert'
delay_time = 1

test(webAddress, itemCreate, target, sheet_name, delay_time)


itemCreate = [
    ['click', "id=gdpr-accept"],
    ['click', "xpath=//div[@class='electure-end']"],
    ['click', "id=search"],
    ['type', "id=v-search"],
    ['click', "id=search-go"],
    ['click', "id=go-to-end"],
]
target = ['get', "id=status"]
sheet_name = 'LinkedList_Search'
delay_time = 1

test(webAddress, itemCreate, target, sheet_name, delay_time)


itemCreate = [
    ['click', "id=gdpr-accept"],
    ['click', "xpath=//div[@class='electure-end']"],
    ['click', "id=remove"],
    ['click', "id=remove-kth"],
    ['type', "id=v-remove-kth"],
    ['click', "id=removekth-go"],
    ['click', "id=go-to-end"],
]
target = ['get', "id=remove-err"]
sheet_name = 'LinkedList_Remove'
delay_time = 1

test(webAddress, itemCreate, target, sheet_name, delay_time)
