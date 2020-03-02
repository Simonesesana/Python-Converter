#Binario - Decimale
def btd(x):
    x = str(x)

    l = (len(x))*-1                         #Number length
    i = -1                                  #Counter
    i2 = 0                                  #2nd Counter
    t = ""                                  #Temp var
    dec = 0                                 #Return value

    while (i>=l):
        t = x[i]
        i = i - 1

        if (t == "0"):
            i2 = i2 + 1
        elif (t == "1"):
            dec = dec + (2**i2)
            i2 = i2 + 1
        else:
            return("Error")

    return(dec)


#Ottale - Decimale
def otd(x):
    l = (len(str(x)))*-1                       #String length * -1
    x2 = str(x)
    i = -1                                     #Counter
    i2 = 0                                     #Second counter
    dec = 0                                    #Return value

    while i>=l:
        if(int(x2[i])>7):
            return("Error")

        dec = dec + (int(x2[i]) * (8**i2))
        i = i - 1
        i2 = i2 + 1

    return(dec)


#Esadecimale - Decimale
def etd(x):
    x = str(x)
    l = (len(x))*-1                             #String length *-1
    i = -1                                      #Counter
    i2 = 0                                      #Second counter
    t = ""                                      #Temp var
    dec = 0                                     #Output

    while(i >= l):
        t = x[i]

        try:
            t = int(t)
            dec = dec + (t*(16**i2))

            i = i - 1
            i2 = i2 + 1

        except:
            if(t == "A"):
                dec = dec + (10*(16**i2))
            elif(t =="B"):
                dec = dec + (11*(16**i2))
            elif(t =="C"):
                dec = dec + (12*(16**i2))
            elif(t =="D"):
                dec = dec + (13*(16**i2))
            elif(t =="E"):
                dec = dec + (14*(16**i2))
            elif(t =="F"):
                dec = dec + (15*(16**i2))
            else:
                return("Error")

            i = i - 1
            i2 = i2 + 1

    return(dec)

################################################################################

#Decimale - binario
def dtb(x):
    bin = ""                                #Output

    while (x > 0):
        bin = bin + str(x%2)
        x = x//2

    return(inv(bin))


#Decimale - ottale
def dto(x):
    ott = ""                                #Output

    while (x>0):
        ott = ott + str(x%8)
        x = x//8

    return(inv(ott))


#Decimale - esadecimale
def dte(x):
    esa = ""                                #Output
    t = 0                                   #Temp var

    while (x>0):
        t = x%16

        if(t < 9):
            esa = esa + str(t)
        elif(t == 10):
            esa = esa + "A"
        elif(t == 11):
            esa = esa + "B"
        elif(t == 12):
            esa = esa + "C"
        elif(t == 13):
            esa = esa + "D"
        elif(t == 14):
            esa = esa + "E"
        elif(t == 15):
            esa = esa + "F"

        x = x//16

    return(inv(esa))




#Inversione stringa
def inv(stg):
    l = (len(stg))*-1                       #String length
    i = -1                                  #Counter
    t = ""                                  #Temp var
    stg2 = ""                               #Output string

    while(i>=l):
        t = stg[i]
        stg2 = stg2 + t
        i = i - 1

    return(stg2)
