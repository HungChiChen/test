def reverse_1() :

    input_phrase = input( "請輸入文字 : " )

    plist = list(input_phrase)
    count_phrase = len(input_phrase)

    for num in range(count_phrase):
        plist.insert(num,plist.pop())

    new_phrase = ''.join(plist)
    print(new_phrase)

def reverse_2() :
    




# reverse_1()
