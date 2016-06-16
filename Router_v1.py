# -*- coding:utf8 -*-

# the different operators, use dictionary to store key, value
OperatorA = {
    '1': 0.9,
    '268': 5.1,
    '46': 0.17,
    '4620': 0.0,
    '468': 0.15,
    '4631': 0.15,
    '4673': 0.9,
    '46732': 1.1
}

OperatorB = {
    '1': 0.92,
    '44': 0.5,
    '46': 0.2,
    '467': 1.0,
    '48': 1.2
}

# get cheapest operator: print the result
def getCheapestOperator(telephone_number):
    maxLengthA = 0
    maxLengthB = 0
    priceA = -1
    priceB = -1
    for key, value in OperatorA.items():
        # print key
        if telephone_number.find(key) == 0:
            lengthA = len(key)
            if lengthA > maxLengthA:
                maxLengthA = lengthA
                telephone_prefixA = key
                priceA = value
    # print 'maxLengthA = %d' %maxLengthA
    # print 'telephone_prefixA = %s' %telephone_prefixA
    # print 'priceA = %f' %priceA

    for key, value in OperatorB.items():
        # print key
        if telephone_number.find(key) == 0:
            lengthB = len(key)
            if lengthB > maxLengthB:
                maxLengthB = lengthB
                telephone_prefixB = key
                priceB = value
    # print 'maxLengthB = %d' %maxLengthB
    # print 'telephone_prefixB = %s' %telephone_prefixB
    # print 'priceB = %f' %priceB

    if maxLengthA == 0 and maxLengthB == 0:
        print 'none of the operator deals phone number with this country+area code!'
    else:
        if priceA < priceB and priceA >= 0 and priceB >= 0:
            print 'cheapest operator route is A'
            print 'price is %f' % priceA
        elif priceA > priceB and priceA >= 0 and priceB >= 0:
            print 'cheapest operator route is B'
            print 'price is %f' % priceB
        elif priceA == priceB and priceA >= 0 and priceB >= 0:
            print 'OperatorA and OperatorB are the same price'
            print 'price is %f' % priceA
        elif priceA < 0 and priceB >= 0:
            print 'cheapest operator route is B'
            print 'price is %f' % priceB
        elif priceB < 0 and priceA >= 0:
            print 'cheapest operator route is A'
            print 'price is %f' % priceA
        else:
            pass


if __name__ == '__main__':
    while True:
        telephone_number = raw_input(u'Please input your telephone number: ')
        # number filter
        telephone_number = telephone_number.replace('+', '')
        telephone_number = telephone_number.replace('-', '')
        telephone_number = telephone_number.replace(' ', '')
        # print 'telephone_number = %s' % telephone_number
        getCheapestOperator(telephone_number)

