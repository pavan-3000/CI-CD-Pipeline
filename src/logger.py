import logging
import os
from datetime import datetime

log_files = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path = os.path.join(os.getcwd(),"logs",log_files)
os.makedirs(log_path,exist_ok=True)

LOG_PATH  = os.path.join(log_path,log_files)

logging.basicConfig(
    filename=LOG_PATH,
    format="[%(asctime)s] %(lineno)s %(name)s  - %(levelname)s - %(message)s",
    level= logging.INFO

)