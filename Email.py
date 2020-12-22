# Purpose of this script is to implement emailing functionality


# Import core libraries
import os
import smtplib
import threading

def LoginServer(thread, logger):
    # Punch in waiting info into logger
    # Wait in loop until global is set
    print("test")

def main():
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    username = os.environ['PATRICK_EMAIL']
    password = os.environ['PATRICK_PASSWORD']
    test_email = os.environ['PATRICK_TEST_EMAIL']

    username = username.strip()
    password = password.strip()
    test_email = test_email.strip()

    server.login(username, password)
    server.sendmail(username, test_email, 'whats up nerd')
    server.close()



if __name__ == '__main__':
    main()
