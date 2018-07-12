# Forum Libre Redirect

The script scrapes [r/France](https://reddit.com/r/france) for the daily Forum Libre thread and serves its URL on a subdirectory of my domain.

Instead of sifting through posts to access the thread (which is sometimes hidden), one can just bookmark [this link](https://kacem.xyz/FL) and each day it will take them to the correct thread.

The script runs every 5 minutes of the 2 hours following the thread's theoratical posting time (7AM on weekdays and midnight on Saturdays) just in case of a delay.

## Rolling your own version

Rolling your own version is as simple as changing `/srv/kacem.xyz` in `FL.py` to your web server's root dir and `/home/khll/scripts` in `crontab` to where you placed `FL.py`. 

The next and final step would be to configure *cron* with the contents of `crontab` (make sure to take your server's timezone into account).
