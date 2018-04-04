import RPi.GPIO as GPIO
import smtplib
import time

GPIO.setmode(GPIO.BCM)

# init list with pin numbers

c=21

# loop through pins and set mode and state to 'high'
GPIO.setup(c,GPIO.IN)
GPIO.setup(20, GPIO.OUT) 
GPIO.output(20, GPIO.HIGH)

# time to sleep between operations in the main loop

SleepTimeS = 2
v=GPIO.input(c)
print(v)
def rk():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('jaisurya190@gmail.com','11111aaaaa11111')

    msg="soil is dry"
    server.sendmail("jaisurya190@gmail.com","srrajesh113@gmail.com",msg)
    print("success")
    server.quit()
def sr():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('jaisurya190@gmail.com','11111aaaaa11111')

    msg="soil is wet"
    server.sendmail("jaisurya190@gmail.com","srrajesh113@gmail.com",msg)
    print("fail")
    server.quit()

while True:
    v=GPIO.input(c)
        
    if(v == 1): #mud is dry soil moisture sensor will detect and supply water to the plant 
        GPIO.output(20, GPIO.HIGH)#it will check again after 10 seconds
        time.sleep(SleepTimeS);
        rk()
    else:       #mud is wet soil moisture sensor will detect and does not supply water to the plant            
        GPIO.output(20, GPIO.LOW)
        time.sleep(SleepTimeS);
        sr()
        
        
            
