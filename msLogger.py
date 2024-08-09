import logging, os
from termcolor import colored
from msConfig import maStConf
class logs:
    def __init__(self):
        self.logger= self.create_logger("BACKEND", maStConf.mainlogfile, '%(asctime)s|%(levelname)s|%(message)s',"a")

    def create_logger(self, name, filename, logformat, writeMode):
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)
        handler = logging.FileHandler(filename, mode=writeMode, encoding='utf-8')
        handler.setFormatter(logging.Formatter(logformat, datefmt=maStConf.logdateformat))
        logger.addHandler(handler)
        return logger
    
    def write(self,*contents):
        for content in contents:
            self.logger.info(content)
            print(colored(content,'cyan'))
    def writeError(self,*contents):
        for content in contents:
            self.logger.error(content)
            print(colored(content,'red'))
    def writeWarning(self,*contents):
        for content in contents:
            self.logger.warning(content)
            print(colored(content,'yellow'))
logger=logs()
if __name__ == "__main__":
    
    logger.write("Log test process started.","Inline log written")
    logger.writeWarning("Warning log written")
    logger.writeError("Error log written")