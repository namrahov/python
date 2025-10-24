
import smtplib

from db.Database import Base, engine

Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    print("Hello World")
    conn = smtplib.SMTP("smtp.gmail.com", 587)
    conn.starttls()

    conn.login('amrahovnurlan@gmail.com', 'asa')
    conn.sendmail('amrahovnurlan@gmail.com', 'nurlan.amrahov@naic.az', 'Test mail/n Hello World')


    conn.quit()



