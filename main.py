import argparse

import random
import pywebio
from pywebio.input import  TEXT,input,radio
from pywebio.output import put_html,put_text,put_error



def run():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=7700)
    args = parser.parse_args()
    pywebio.start_server(generate_email, port=args.port)
    pywebio.session.hold()


def generate_email():
    pywebio.session.set_env(title='EMAIL-GENERATOR')
    whole_list = []
    email_list =[]


    fname = input('Enter your first name')
    lname = input('Enter your last name')

    service = radio('Choose service name',options=['gmail','hotmail','yahoo','outlook','other'])
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
         m=0
         while m <=5:
          email = ''
          for i in range(0,leng):
            email += random.choice(whole_list)
          for j in range(0,int(n_length)):
              email+= str(random.choice(numbers))
          m += 1
          email_list.append(email)


        put_html('<h1 style="text-align:center">Your randomly generated emails are:</h1>')
        for _ in range(len(email_list)):
            put_html(f'<div style="line-height:1.5"><ul><li style="font-size:20px; color: #3D087B">{email_list[_]}@{service}.com </li></ul><div>')
        pywebio.output.put_html("<h2 style='text-align:center'>Didn't like the emails? Well, then generate again.</h2>")
        put_html('<h3 style="text-align:center"><a href="https://gs-random-email.herokuapp.com/">Generate Again</a></h3>')





     else:

         for i in fname:
             whole_list.append(i)
         for j in lname:
             whole_list.append(j)
         m=0
         while m<=5:
          email=''
          for i in range(0, int(length)):
           email += random.choice(whole_list)
          m+=1
          email_list.append(email)
         put_html('<h1 style="text-align:center">Your randomly generated emails are:</h1>')
         for _ in range(len(email_list)):
             put_html(f'<div style="line-height:1.5"><ul><li style="font-size:20px; color: #3D087B">{email_list[_]}@{service}.com </li></ul><div>')
         pywebio.output.put_html("<h2 style='text-align:center'>Didn't like the emails? Well, then generate again.</h2>")
         put_html('<h3 style="text-align:center"><a href="https://gs-random-email.herokuapp.com/">Generate Again</a></h3>')








if __name__ == '__main__':
    run()

