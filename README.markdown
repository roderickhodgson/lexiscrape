## What is Lexiscrape

Lexiscrape is a simple Scrapy crawler that makes it dead easy to return a list of weighted tags for a given URL.

## Installation

Lexiscrape only requires Scrapy and its dependencies to function.

To install Scrapy, run ```pip install scrapy```.

Then just ```git clone git://github.com/roderickhodgson/lexiscrape.git```

## Running Lexiscrape

You can run lexiscrape as you would any other Scrapy project. The crawler name is lexi. The additional parameter -a url is required. 

From within the root of the repository

```
scrapy crawl lexi -a url=https://news.google.com -o google_news_tags.json -t json
```

## Future work

As of writing this, I have only spent a couple of hours on this project. There is much still to be done. Such as:

* Accept more than one URL
* Disambiguate tags, or provide any Linked Data information

## License
(The MIT License)

Copyright © 2012 Roderick Hodgson

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the ‘Software’), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED ‘AS IS’, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

