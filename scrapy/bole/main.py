from scrapy.cmdline import execute
import sys
import os


# Add project direction to the environment path
#os.path.abspath(__file__)  get the path of main.py
#os.path.dirname(os.path.abspath(__file__)  get the parent direction of main.py
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(['scrapy','crawl','jobbole'])
