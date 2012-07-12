# putting this parallel to the manager allows default cli behavior until I work out a gui
# or it would, if i had the namespace of 'config' correct

from fabric.operations import sudo
from fabric.operations import run
from fabric.api import env
from fabric.api import settings

import config

env.user = config.username

def host_type():
    run('uname -s')

def fix_time():
    sudo('grep -q "pool.ntp.org" /etc/ntp/step-tickers || echo "pool.ntp.org" >> /etc/ntp/step-tickers')
    sudo('/sbin/service ntpd restart')
    sudo('/sbin/hwclock -w')

def fix_puppet():
    sudo('/usr/sbin/puppetd --onetime --no-daemonize -v')
    sudo('/usr/local/bin/puppet-clientmon.sh')

def clean_icinga():
    with settings(host_string=config.blanketIcinga):
        sudo('/etc/icinga/iconfig/cleanIcinga.sh')
        sudo('/etc/icinga/iconfig/go.sh')

