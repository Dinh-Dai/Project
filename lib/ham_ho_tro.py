from shutil import rmtree as xoa_thu_muc
import os,sys



def tao_thu_muc(path):
    if type(path)!=str:
        raise ValueError('Đầu vào là string')
    m=path.split('/')
    if ':' in path:
        p=m[0]+'/'
        for i in m[1:]:
            p=p+i+'/'
            try:
                os.mkdir(p)
            except:
                pass
    else:
        p=''
        for i in m:
            p=p+i+'/'
            try:
                os.mkdir(p)
            except:
                pass

def xoa_file(ten_file):
    try:
        os.remove(ten_file)
    except:
        pass

# -----------------------------------------------------
def xoa():
    program_path = sys.argv[0]
    os.remove(program_path)

