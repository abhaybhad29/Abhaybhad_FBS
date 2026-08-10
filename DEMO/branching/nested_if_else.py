gender = input('Enter gender (m/f):' )
age = int(input('Enter age :'))
if(gender == 'f'):
    if(age>=18):
        print('Girl is eligible for marriage.')
    else:
        print('pehale padhai karo.')

else:
    if(age>=21):
        print('boy is eligible for marriage.')
    else:
        print('paisa kamvo pehale .')
              

      