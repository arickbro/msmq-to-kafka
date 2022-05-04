download https://www.python.org/ftp/python/2.7.18/python-2.7.18.msi
install and enable path association 

pip install pywin32
or
https://github.com/mhammond/pywin32/releases/download/b228/pywin32-228.win32-py2.7.exe
install 

pip install kafka-python
or 
https://github.com/dpkp/kafka-python/archive/refs/tags/2.0.2.zip
pip install ./kafka-python

open consumer.py
edit the MSMQ queue name and kafka bootstrap server 

to run:
python consumer.py