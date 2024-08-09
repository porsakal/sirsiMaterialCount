import os
from datetime import datetime
from termcolor import colored
from pprint import pp

def withDate(format):
        return datetime.now().strftime(format)
class matstatconfig:
    def __init__(self):
        ## Directories and types

        self.mainpath=os.getcwd()

        # Logs
        self.logspath=os.path.join(self.mainpath,"logs")
        self.logdateformat='%Y-%m-%d %H:%M:%S %z'
        self.logdate=withDate(self.logdateformat)
        self.monthfolder=withDate("%Y-%m")
        self.mainlogfile=os.path.join(self.logspath,self.monthfolder,withDate("matStat-%Y-%m-%d.log"))
        
        self.fileToProcess=os.path.join(self.mainpath,"test.txt")
maStConf= matstatconfig() 

if __name__ == "__main__":
     
     print("Main path:",colored(maStConf.mainpath,'green'))
     print("Log path:",colored(maStConf.logspath,'green'))
     