# Scripts for automatation :computer:

The purpose of this repository is automate basic task by running a Command or by a Cron job.

___

## How to run :beginner:

First you need to download the repository. Just by clicking the [here](https://www.github.com/xsami/scripts/archive/master.zip) or cloning it, and following these steps:

1. Unzip the file on the directory of your prefered
2. Open your terminal or console and go to the directory of script you want to excecute
3. TODO


## Configurations :hammer:

To make the script run automatically on your system every directory contain a list of dependecies that your machine must meet before excecute.

For [Unix](https://en.wikipedia.org/wiki/Unix) users:
1. Open the terminal
2. Open the crontab editor using `vi`
```sh
$ sudo export VISUAL=vi
$ sudo export EDITOR=vi
$ sudo crontab -e
```
3. Now add the following example of configuration to the job
```sh
# Ansiable: Send sms message every minute
* * * * * * ./<directory_where_repo_downloaded>/python/sms_to.py >> /var/log/sms_to.log 2>&1
```

For [Windows](https://en.wikipedia.org/wiki/Microsoft_Windows) users:

1. Open the console (**Run as administrator**)
2. Open the Windows task schedule 
```sh
> control schedtasks
```
3. TODO