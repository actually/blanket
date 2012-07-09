# you have to have this stuff
_var_dir="CHANGEME"
pid_file = _var_dir + "run/blanket-example.pid"
out_err_log = _var_dir + "logs/example-outerr.log"
log_file = _var_dir + "logs/example-logging.log"
log_format = '%(asctime)s %(levelname)s %(message)s'

global_log_level = "DEBUG"
log_levels = {"test" : "DEBUG"}

soap_port = 'CHANGEME'


# sample config with invalid data
blanketUser = 'your ssh username'
blanketDomain = 'set this to save yourself typing full hostnames'