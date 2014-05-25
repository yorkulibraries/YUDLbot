# YUDLbot

A silly little bot that tweets random [York University Digital Library](http://digital.library.yorku.ca) content. You can find me at [@YUDLbot](http://twitter.com/YUDLbot).

If you want use it, you will need to setup the variables outlined in `config.py.example` and rename it to `config.py`. For `SOLR_DATA` you will need to construct a query, and append `&fl=PID%2C+mods_titleInfo_title_ms&wt=json&indent=true` along with the number of row you want. For example `&rows=100`.
