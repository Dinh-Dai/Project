from lib.ham_ho_tro import xoa_file, xoa_thu_muc, tao_thu_muc
import os

xoa_file('data/data1/init.txt')
xoa_file('data/data2/init.txt')
xoa_thu_muc('lib/__pycache__')
xoa_file('weights storage/CNN/init.txt')
xoa_file('weights storage/LSTM/init.txt')
tao_thu_muc("share")

os.chdir('share')
os.system('git init')
os.system('git branch -M main')
os.system('git remote add intro_AI https://github.com/Huutkang/share.git')
os.system('git pull intro_AI main')



