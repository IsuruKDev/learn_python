# dictionary data structure - key value pair
http_status = {
    200:'OK',
    201:'Created',
    400:'Bad Request'
}

http_status[404] = 'Not Found'

print(http_status)
print(http_status.keys())
print(http_status.values())
print(http_status[201])

http_status['500'] = ['Internal Server Error','Bad Gateway','Service Unavailable']
print(http_status)

print(http_status.get(12,'No status code found'))

del http_status[200]
print(http_status)

print("\n\n\n")

greeting_dic = {
    "first":["Hello","Hi","How are you"],
    "second":["Bye","Keep in touch"]
}

first_list = greeting_dic['first']
first_list.append("Ayubowan")

print(first_list)
print(greeting_dic)
print(greeting_dic['first'][1], greeting_dic['first'][2])