
'''
解法都是以自己參考書本「深入淺出Python（第二版）」所學到的方式完成
＊ reverse_1 
採用的書上學來的範例，應用於考題，可參考我自己的程式筆記
https://s9522333.medium.com/%E7%AC%AC%E4%BA%8C%E7%AB%A0-list%E7%B7%B4%E7%BF%92-3c9e061ffdaa
＊ reverse_2
採用書本的切片說明完成，可參考我自己的程式筆記
https://s9522333.medium.com/%E4%B8%B2%E5%88%97-%E7%B4%A2%E5%BC%95%E4%BD%8D%E7%BD%AEindex-492c19a3fd08
'''

def reverse_1() :
    # 讓使用者輸入文字
    input_phrase = input( "[第一小題] 請輸入想要反轉的文字 : " )
    # 把輸入的文字轉成字串
    plist = list(input_phrase)
    # 計算輸入字串的長度
    count_phrase = len(input_phrase)

    # 使用回圈將字串從最後一個彈出再插入字串，直到所有字串都彈出完畢
    for num in range(count_phrase):
        plist.insert(num,plist.pop())
    # 合併字串與輸出結果
    new_phrase = ''.join(plist)
    print(new_phrase)

def reverse_2():
    # 讓使用者輸入文字，當遇到空白鍵會自動拆分
    input_phrase = input( "[第二小題] 請輸入想要反轉但字序不變的文字 : " ).split()
     # 把拆分後的文字轉成字串
    plist = list(input_phrase)
    # print("輸入字串分開",input_phrase)
    # 使用回圈依照位置分開反轉
    for num in range(len(input_phrase)):
        n_plist = plist[num]
        print(n_plist[::-1],end = " ")
        

reverse_1()

reverse_2()
