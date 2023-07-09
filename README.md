# Climate Clock Made Simple
## This is not the real climate clock repo
The Climate Clock (https://climateclock.world & https://github.com/climateclock](https://github.com/climateclock) is a beautiful resource that shows multiple clocks and good news on massive public clocks, smaller mobile units, apps and as a widget on your website.  If that's your thing, then you're not in the right place :)

## Want to show the official climate clock widget on your website?
If you just want to show the climate clock on your website, then this isn't the project you need and https://climateclock.world/clocks#digital or the locally hosted version https://github.com/climateclock/climate-clock-widget climate clock widgets are probably what you need.  This project does only one thing and it does it in a stripped-down manner that is probably not right for most people.

## So what is this project for?
The API for the climate clock sends about 8k of data which is cool if you want the full clock in the official colours and everything but is much too heavy for my purposes.  I want just one thing.  The date the planet hits 1.5 degrees C hotter.  This project provides the most minimal way to get that data for anyone that wants it in the most efficient manner.  I'm sure other projects have a similar need and this way we can share and make less of those 8kb calls to get a timestamp.

## How does it work?
The climate clocks countdown timer only changes every few months as the data is analysed and the JSON file itself says to pull this data every 24 hours.  It also contains other fields that update as often as every 15 minutes.  So I decided to poll the file every 6 hours, extract the relevant field, write it to a text file and update the repo with the new value.

## How to use?
The available resources are
https://sparkes.github.io/ClimateClockMinimal/index.html
https://sparkes.github.io/ClimateClockMinimal/deadline.txt
https://sparkes.github.io/ClimateClockMinimal/deadline.xml
https://sparkes.github.io/ClimateClockMinimal/deadline.json

All are extremely lightweight containing the minimal data allowed by the format to present the single datetime element in a clear and concise way.


