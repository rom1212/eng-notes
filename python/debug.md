# Find all the processes with a given name
```
# Find all python processes
import subprocess
log.info('xxxxlog: pgrep -a python: {}'.format(subprocess.check_output(['pgrep', '-a', 'python']).split('\n')))
```
