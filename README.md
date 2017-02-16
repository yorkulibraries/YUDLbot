# YUDLbot

## Overview

A bot that tweets random [York University Digital Library](http://digital.library.yorku.ca) content. You can find implementations at:
* [@YUDLbot](http://twitter.com/YUDLbot)
* [@YUDLcat](http://twitter.com/YUDLcat)
* [@YUDLdog](http://twitter.com/YUDLdog)

If you want use it, you will need to setup the variables outlined in `config.py.example` and rename it to `config.py`. For `SOLR_DATA` you will need to construct a query, and append `&fl=PID%2C+mods_titleInfo_title_ms&wt=json&indent=true` along with the number of rows you want. For example `&rows=100`. You can also crib from the example queries in the repo; [`YUDLbot-desc.query`](YUDLbot-desc.query) and [`YUDLbotCat.query`](YUDLbotCat.query).

## License

[Public Domain](LICENSE)
