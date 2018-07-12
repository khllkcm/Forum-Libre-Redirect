## Forum Libre Redirect

Le script gratte [r/France](https://reddit.com/r/france) pour localiser le Forum Libre du jour et sert son URL sur un sous-répertoire de mon domaine.

Au lieu de passer au crible les publications pour accéder au FL (qui est parfois caché), on peut simplement mettre [ce lien](https://kacem.xyz/FL) en marque page et chaque jour on s'amènera au bon fil de discussion.

Le script s'exécute toutes les 5 minutes des 2 heures suivants l'heure d'affichage théorique du FL (7h en semaine et minuit le samedi) juste en cas de retard.


### Rouler votre propre version

Faire rouler votre propre version est aussi simple que de changer `/srv/kacem.xyz` dans `FL.py` au répertoire racine de votre serveur web et `/home/khll/scripts` dans `crontab` à l'endroit où vous avez placé `FL.py`.

L'étape suivante et finale serait de configurer cron avec le contenu de crontab (assurez-vous de prendre en compte le fuseau horaire de votre serveur).

---

## Forum Libre Redirect

The script scrapes [r/France](https://reddit.com/r/france) for the daily Forum Libre thread and serves its URL on a subdirectory of my domain.

Instead of sifting through posts to access the thread (which is sometimes hidden), one can just bookmark [this link](https://kacem.xyz/FL) and each day it will take them to the correct thread.

The script runs every 5 minutes of the 2 hours following the thread's theoratical posting time (7AM on weekdays and midnight on Saturdays) just in case of a delay.

### Rolling your own version

Rolling your own version is as simple as changing `/srv/kacem.xyz` in `FL.py` to your web server's root dir and `/home/khll/scripts` in `crontab` to where you placed `FL.py`. 

The next and final step would be to configure *cron* with the contents of `crontab` (make sure to take your server's timezone into account).

