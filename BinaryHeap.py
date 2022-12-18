from main import test

webAddress = 'https://visualgo.net/en/heap?slide=1'
##create
itemCreate = [
    ['click', "id=gdpr-accept"],
    ['click', "xpath=//div[@class='electure-end']"],
    ['click', "id=createNlogN"],
    ['type', "id=arrv1"],
    ['click', "id=createNlogN-go"],
    ['click', "id=go-to-end"],
]
target = ['get', "id=status"]
sheet_name = 'BinaryHeap_Create'
delay_time = 1

test(webAddress, itemCreate, target, sheet_name, delay_time)

###insert application
itemCreate = [
    ['click', "id=gdpr-accept"],
    ['click', "xpath=//div[@class='electure-end']"],
    ['click', "id=insert"],
    ['type', "id=v"],
    ['click', "id=insert-go"],
    ['click', "id=go-to-end"],
]
target = ['get', "id=insert-err"]
sheet_name = 'BinaryHeap_Insert'
delay_time = 1

test(webAddress, itemCreate, target, sheet_name, delay_time)



#Update application
itemCreate = [
    ['click', "id=gdpr-accept"],
    ['click', "xpath=//div[@class='electure-end']"],
    ['click', "id=updateKey"],
    ['type', "id=newv"],
    ['click', "id=updateKey-go"],
    ['click', "id=go-to-end"],
]
target = ['get', "id=updateKey-err"]
sheet_name = 'BinaryHeap_Update'
delay_time = 1

test(webAddress, itemCreate, target, sheet_name, delay_time)

##Delete application
itemCreate = [
    ['click', "id=gdpr-accept"],
    ['click', "xpath=//div[@class='electure-end']"],
    ['click', "id=delete"],
    ['type', "id=del_i"],
    ['click', "id=delete-go"],
    ['click', "id=go-to-end"],
]
target = ['get', "id=delete-err"]
sheet_name = 'BinaryHeap_Delete'
delay_time = 1

test(webAddress, itemCreate, target, sheet_name, delay_time)
