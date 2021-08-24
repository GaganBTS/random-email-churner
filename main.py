import argparse
import random
import itertools

import pywebio
from pywebio.input import  TEXT,input,radio
from pywebio.output import put_html,put_text,put_error

def generate_email():
    pywebio.session.set_env(title='EMAIL CHURNER')
    whole_list = []

    email = ''
    fname = input('Enter your first name')
    lname = input('Enter your last name')

    service = radio('Choose service name',options=['Gmail','Hotmail','Yahoo','Outlook','Other'])
    if service == 'Other':
        service = input('Enter the service name')
    number = radio('Do you want numbers in your email',options=['Yes','No'])
    length = input('What do you prefer to be the length of your email,min:3')
    if int(length) <3:
        put_error("Sorry! Can't proceed")
    else:
     if number == 'Yes':
        numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        n_length = input('how many numbers you prefer: ')
        for i in fname:
            whole_list.append(i)
        for j in lname:
            whole_list.append(j)
        leng = int(length)-int(n_length)
        if leng <0:
            put_error('Length of numbers wanted exceeded the length of whole email, try again')
        else:
         for i in range(0,leng):
            email += random.choice(whole_list)
         for j in range(0,int(n_length)):
              email+= str(random.choice(numbers))

         put_html(f'<h1>Random generated email is:  <span style ="color:#3D087B">{email}@{service}.com</span></h1>\n<h3>Did not like the email? Generate again.</h3>')



     else:
         for i in fname:
             whole_list.append(i)
         for j in lname:
             whole_list.append(j)

         for i in range(0, int(length)):
           email += random.choice(whole_list)
         put_html(f'<h1>Random generated email is:  <span style ="color:#3D087B">{email}@{service}.com</span></h1>\n<h3>Did not like the email? Generate again.</h3>')








if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p","--port",type=int,default=7700)
    args =parser.parse_args()
    pywebio.start_server(generate_email,port=args.port)
