import os

LOCAL = '/usr/local/bin:/usr/local/sbin:'  
HOME = '~'  ### !!! REPLACE WITH YOUR HOME PATH !!! ###  
RVM = HOME + '/.rvm/bin:'

# Sublime's default path is
# /usr/bin:/bin:/usr/sbin:/sbin
os.environ['PATH'] += ':'  
os.environ['PATH'] += LOCAL  
os.environ['PATH'] += RVM

print 'PATH = ' + os.environ['PATH']  
