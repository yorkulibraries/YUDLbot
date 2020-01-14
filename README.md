# YUDLbot

## Overview

A bot that tweets random [York University Digital Library](http://digital.library.yorku.ca) content. You can find implementations at:
* [@YUDLbot](http://twitter.com/YUDLbot)
* [@YUDLcat](http://twitter.com/YUDLcat)
* [@YUDLdog](http://twitter.com/YUDLdog)

If you want use it, you will need to setup the variables outlined in `config.py.example` and rename it to `config.py`. You will also need a Solr query. These queries from an Islandora 7.x instance. Feel free to crib from the example queries in the repo:
* [`yudlbot-cat.query`](yudlbot-cat.query)
* [`yudlbot-desc.query`](yudlbot-desc.query)
* [`yudlbot-dog.query`](yudlbot-dog.query)
* [`yudlbot.query`](yudlbot.query)

You can automate it with a cron job like so:

```
17 */5 * * * /usr/bin/python /path/to/YUDLbot.py
```

## License

[Public Domain](LICENSE)
