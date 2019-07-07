a={'Name':'Fatima'}
try:
    
    with open('data.csv','w'):
        pass
    print('I am after open file')
    print(a['Name'])

except KeyError:
    print('This key does not exist in this ADT')
except FileNotFoundError as e:
    print(e)
    print('File does not exist') 
except Exception:
    print('This is unknown exception')
finally:
    print('I am finally block!!')

print('Ennding')