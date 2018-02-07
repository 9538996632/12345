import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('jaisurya190@gmail.com','xxxxxx')

msg="your message"
server.sendmail("jaisurya190@gmail.com","vijayshiva258@gmail.com",msg)
server.quit()

