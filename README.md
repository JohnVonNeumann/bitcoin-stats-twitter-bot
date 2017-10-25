# bitcoin-stats-twitter-bot

> This bot harvests statistics from a full node using RPC calls to craft tweets that hopefully give insights into the network, without you having to consult various sites. If you are looking for a particular stat, tweet at @JanosVonNeumann and he will see what he can do.

## Notes

This project took a while to get finished largely due to having to reconfigure an entire WAN/LAN to get the node running, I learnt a lot in the process. It's been a lot of fun and I hope to keep building more useful technology for the Bitcoin community.

I built this in Python as I work with it (not enough, hence working more with it on this project) and I also find it to be a very kind language.

I've used crontab to manage/automate the calls, had some issues with this one too due to envvar handling, took a few hours but ended up writing a bash script for it to handle the environment in a kinder way.

## Things I learnt
* Bitcoin RPC: I've had (and continue to) a lot of fun experience with the command line and also the node itself over this project. In particular, learning how the network works, how the nodes communicate and then all the configuration options available is mind blowing. I think I'm going go through the lightning node stuff next.

* Crontab: I'd had what I can safely call no experience with this before this project. I did actually think it would be "easier" to get going but now that I look back it it. it IS easy to use, but handling the envvars and virtualenvs with it was just an awkward way of learning it. 

* Port Forwarding: I'd had no experience with this and to be honest when I'd seen this included in tasks in other projects before I probably shied away from it, it was really interesting and taught me a lot about how networks work. 

* Networking: I pulled apart a home network and wired up everything again, complete with DHCP servers and separate access points. Nuff said on this one, was a lot of fun. 
