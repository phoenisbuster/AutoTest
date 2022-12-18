from main import test

webAddress = 'https://visualgo.net/en/bst?slide=1'
####create
itemCreate = [
    ['click', "id=gdpr-accept"],
    ['click', "xpath=//div[@class='electure-end']"],
    ['click', "id=create"],
    ['click', "id=create-example1"],
    ['click', "id=create"],
    ['click', "id=create-example2"],
    ['click', "id=create"],
    ['click', "id=create-random"],
    ['click', "id=create"],
    ['click', "id=create-skewed-left"],
    ['click', "id=create"],
    ['click', "id=create-skewed-right"],
    ['click', "id=create"],
    ['click', "id=create-empty"],
    ['click', "id=go-to-end"],
]
target = ['get', "id=create-err"]
sheet_name = 'BST_Create'
delay_time = 1

test(webAddress, itemCreate, target, sheet_name, delay_time)
###insert application
itemCreate = [
    ['click', "id=gdpr-accept"],
    ['click', "xpath=//div[@class='electure-end']"],
    ['click', "id=create"],
    ['click', "id=create-empty"],
    ['click', "id=insert"],
    ['type', "id=v-insert"],
    ['click', "id=insert-go"],
    ['click', "id=go-to-end"],
]
target = ['get', "id=insert-err"]
sheet_name = 'BST_Insert'
delay_time = 1

test(webAddress, itemCreate, target, sheet_name, delay_time)

#Search application
itemCreate = [
    ['click', "id=gdpr-accept"],
    ['click', "xpath=//div[@class='electure-end']"],
    ['click', "id=search"],
    ['type', "id=v-search"],
    ['click', "id=search-go"],
    ['click', "id=go-to-end"],
]
target = ['get', "id=status"]
sheet_name = 'BST_Search'
delay_time = 1

test(webAddress, itemCreate, target, sheet_name, delay_time)

###Remove application
itemCreate = [
    ['click', "id=gdpr-accept"],
    ['click', "xpath=//div[@class='electure-end']"],
    ['click', "id=remove"],
    ['type', "id=v-remove"],
    ['click', "id=remove-go"],
    ['click', "id=go-to-end"],
]
target = ['get', "id=remove-err"]
sheet_name = 'BST_Remove'
delay_time = 1

test(webAddress, itemCreate, target, sheet_name, delay_time)
