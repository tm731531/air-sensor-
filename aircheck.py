#根據python3的方法 因為python2會讀ascii碼 解析不方便 
#讀取第一個參數設定發送到thingspeak的時間
import serial, requests, time,sys
ser = serial.Serial()
ser.baudrate = 9600
ser.port = '/dev/ttyUSB0'# port<--樹梅派的port

ser.open()
i=0
dataarray=[0]*17
pm1=0
pm25=0
pm10=0
co2=0
formaldehyde=0
temperature=0
humidity=0
delay=int(sys.argv[1])
print(delay)
target_url="thingspeakurl"
while True:

    for line in ser.read():
        dataarray[i%17]=line
        #a.append(line)
        #a.append(str(i%17))
        i=i+1

    pm1=dataarray[2]*255+dataarray[3]
    pm25=dataarray[4]*255+dataarray[5]
    pm10=dataarray[6]*255+dataarray[7]
    formaldehyde=(dataarray[8]*255+dataarray[9])/1000
    co2=dataarray[10]*255+dataarray[11]
    temperature=dataarray[12]
    humidity=dataarray[13]
    if(i%17==0):
        requests.get(target_url %(pm1,pm25,pm10,formaldehyde,co2,temperature,humidity))
        time.sleep(delay)
    print ("%s" %dataarray)
