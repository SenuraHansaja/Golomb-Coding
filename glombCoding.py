import math

def golombFunction(Xval,mVal):
    b =  math.ceil(math.log(mVal,2))
    q = math.floor(Xval/mVal)
    r = Xval - q*mVal
    
    qstring = ""
    rbinary = ""
    if (r < 2**b - mVal):
        for _ in range (b-2):
            qstring += '1'
        qstring += '0'
        rbinary = "0"
        rbinary  += format(r,'b')
    elif (r >= 2**b - mVal):
        rint = r + 2**b - mVal
        qstring = '0'
        rbinary = format(rint,'b')
    
    return qstring, rbinary


print(golombFunction(4,5))