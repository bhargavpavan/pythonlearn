# prog: to print number in words

n = int(input('enter n value less than 999: '))

words_less_than19 = ['','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','ninteen']
words_with_tens = ['','','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninty']
words_with_hundreds = ['','one hundred and','two hundred and ','three hundred and','four hundred and','five hundred and','six hundred and','seven hundred and','eight hundred and','nine hundred and']

if(n == 0):
    output = 'zero'
elif(n <= 19):
    output = words_less_than19[n]
elif(n <= 99):
    output = words_with_tens[n//10] + ' ' + words_less_than19
elif(n <= 999):
    output = words_with_hundreds[n//100] + ' ' + words_with_tens[(n//10)%10] + ' ' + words_less_than19[(n%100)%10]
else:
    output = 'number is out of range'
print(output)
