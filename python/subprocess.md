# subprocess
## check_output
```python
from subprocess import check_output, CalledProcessError, STDOUT
import os
import sys
from datetime import datetime
def main():
    try:
        # out = check_output(['cd', os.path.dirname(__file__)])
        os.chdir(os.path.dirname(__file__))
        out = check_output(['git', 'pull'], stderr=STDOUT)  # make sure stderr appear in out or ex.output
        print 'output:', out
        if 'Already up-to-date' in out:
            with open(os.path.join(os.path.dirname(__file__), 'cron.log'), 'a+') as f:
                f.write(datetime.utcnow().isoformat() + ": Cible already up-to-date\n")
            # keep going because some thing could keep failing for some time.
    except CalledProcessError as ex:
        print 'exception happend: ex:', ex
        print 'exception happend: ex.cmd:', ex.cmd
        print 'exception happend: ex.returncode:', ex.returncode
        print 'exception happend: ex.output:', ex.output
        sys.exit(0)
if __name__ == "__main__":
    main()
```
