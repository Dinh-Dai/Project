import os 

def name():
    user = os.getlogin()
    if user == 'Thang':
        return 'Nguyễn Hữu Thắng'
    else:
        return 'Vô Danh'


