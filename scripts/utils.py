'''
utils

各種共通関数
'''
################################
# Libraries
################################
import os
from datetime import datetime as dt

################################
# Functions
################################

# Prepare directory
def prepare_savedir(ROOT:str, name:str)->str:
    '''
    Args
        ROOT (str) : Directory for save
        name (str) : Save directory name
    '''

    # define directory
    savedir = os.path.join(ROOT, name)
    # make direcotry
    os.makedirs(savedir, exist_ok=True)

    return savedir

def getdate():
    '''
    Args
        None
    '''

    return dt.now().strftime("%Y%m%d_%H%M")