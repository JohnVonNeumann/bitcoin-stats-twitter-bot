# bitcoin-stats-twitter-bot

This bot harvests statistics from a full node using RPC calls to craft tweets that hopefully give insights into the network, without you having to consult various sites. If you are looking for a particular stat, tweet at @JanosVonNeumann and he will see what he can do.

This project took a while to get finished largely due to having to reconfigure an entire WAN/LAN to get the node running, I learnt a lot in the process. It's been a lot of fun and I hope to keep building more useful technology for the Bitcoin community.

I built this in Python as I work with it (not enough, hence working more with it on this project) and I also find it to be a very kind language.

I've used crontab to manage/automate the calls, had some issues with this one too due to envvar handling, took a few hours but ended up writing a bash script for it to handle the environment in a kinder way.
