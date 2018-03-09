# psrecord
* https://github.com/astrofrog/psrecord
* For accuracy is to 0.1 second (which is the Linux limitation of update the system information)
  * also specified here in psutil: https://psutil.readthedocs.io/en/latest/
```bash
# Install pip if needed
sudo apt/yum install pip
sudo pip install -U pip

# Install psutil
sudo apt/yum install gcc
sudo apt/yum install python-devel
sudo pip install psutil

# Install
sudo pip install psrecord
sudo pip install matplotlib
sudo apt install python-tk or sudo yum install tkinter

# Config - for running on a host without Xwindow
echo "backend: agg" > .config/matplotlib/matplotlibrc
cat .config/matplotlib/matplotlibrc

# run
psrecord 20173 --plot plot.png --duration 60 --interval 0.1

# include subprocesses - useful if the process spawn more processes
psrecord 20173 --plot plot.png --duration 60 --interval 0.1 --include-children
```

# cpustat
* memory information is not good, don't have min/max/avg for memory
* https://github.com/uber-common/cpustat 
* https://www.tecmint.com/cpustat-monitors-cpu-utilization-by-processes-in-linux/


