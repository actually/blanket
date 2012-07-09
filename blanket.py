
"""
At this point there is really no reason to run this as a daemon, but maybe someday

Authors: Nobody worth mentioning

Requires: Python 2.7
          fabric (fabfile.org)
"""

import os
import signal
import errno

from config import setupConfigAndLogging
from optparse import OptionParser
from lib.daemon import createDaemon

log = None
config = None

def main():
    """ Parse config options, daemonize, setup loging and run the manager. """
    global log
    global config

    parser = OptionParser()
    parser.add_option("-e", "--env-name", dest="envName",
           help="Environment name")
    parser.add_option("--action", dest="action", 
                     help="stop, start")     

    options, args = parser.parse_args()
    if not options.envName:
        parser.error("Environment name (-e) is required!")

    setupConfigAndLogging(options.envName)

    from config import config
    import logging
    log = logging.getLogger(__name__)

    runningPid = checkAlreadyRunning()

    if (not options.action or options.action == "start"):
        if runningPid:
            sys.exit("Another instance is running as pid %s." % runningPid)

        createDaemon(config.out_err_log)
        writePid()
        signal.signal(signal.SIGTERM, handleSigTERM)
        print config.out_err_log

        import product.manager
        try:
            product.manager.run()
        except:
            log.error("Exception caught.", exc_info=1)
        finally:
            cleanup()
    elif (options.action == "stop"):
        if runningPid:
            os.kill(runningPid, signal.SIGTERM)
        else:
            sys.exit("Not running.")

def checkAlreadyRunning():
    """ Check the PID to make sure another instance is not already running."""
    if os.path.exists(config.pid_file):
        try:
            pid = int(open(config.pid_file).read())
        except ValueError:
            sys.exit('Error parsing pidfile %s' % config.pid_file)
        try:
            os.kill(pid, 0)
        except OSError, e:
            if e[0] == errno.ESRCH:
                os.remove(config.pid_file)
            else:
                sys.exit("Can not communicate with pid %s." % pid )
        else:
            return pid
    return False

def writePid():
    """ Store Process ID in the PID file. """
    pidfile = open(config.pid_file, 'w')
    pidfile.write(str(os.getpid()))
    pidfile.close()

def handleSigTERM(sig, frame):
    """ Wrapper for signal handler. """
    cleanup()

def cleanup():
    """ Remove PID and quit. """
    log.info("Exiting.")
    os.remove(config.pid_file)
    os._exit(0)

if __name__ == "__main__":
    main()
