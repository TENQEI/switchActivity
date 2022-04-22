SwitchActivity
=========

This project aims at creating a customed database for Nintendo switch, of which combining data from various sources, including [Nintedo Switch Parental Controls app for iOS](https://itunes.apple.com/us/app/nintendo-switch-parental-cont/id1190074407), Nintendo Switch Online, and the annual activity by [Nintendo](www.nintendo.com).
Since Nintendo does not provide its activity API as others do, there's this work-around.

In order for these scripts to talk to the API, a number of variables will need to be discovered, including your device identifier, "smart" device identifier, client identifier, and a session token. The best way to get these is to download the parental controls app to an iOS device, and then to set up a network proxy to inspect the traffic that the app sends during authentication. I personally used [Charles Proxy](https://www.charlesproxy.com) for this purpose, which provides the necssary [MITM proxy](https://www.charlesproxy.com/documentation/proxying/ssl-proxying/) features. 
However, the API tokens refresh itself pretty fast. For the best user expeirence, it'll be great to obtain the token the same way people get their access to Parental Control. 

Once you've got things configured properly in `conf.py`, you can first run `fetch.py`, which will write out a `summary.json` file. Then, you can run `process.py`, which will require some light editing for your use case. 

The goal is to create a database that mainly consists of 4 tables: Game library, Monthly activity, Daily activity and User information.
* The game library table contains the game ID and link to a cover image. The database can also add customed names to the game. A total play/updated time can calculated/stored in this table, too. These data are provided by Nintendo's annual activity record via Nintendo Swith Online(only available in some regions).
* The Monthly activity table can be obtained via Parental Control. Once a device is linked to Parental Control, we can trace back its lifetime activity by months. Monthly records ranks games played in time and days, which will be good to calculate the total time played by each game. As a result, even without the annual activity service, we can reconstruct the statistics with Parental Control alone.
* The Daily activity table is also obtained from Parental Control. Compared to monthly records, it has detailed playtime in terms of days. Nintendo's server only offers daily records for the last 30 days, unfortunately. If we obtain data from the server periodically, we can have a data stream for a further timespan.
* Since one switch can hold multiple users, we can use the User information table to diffrentiate users. Identical Users on different switch devices is theoretically one unique user. If the device is dereigstered from Parental Control, however, one can be unable to link the data via Parental Control.

> Note:
> All of this was inspired by [Eddie Hinkle](https://eddiehinkle.com), who did this first!
> Forked from [cleverdevil/switchpub](https://github.com/cleverdevil/switchpub).
