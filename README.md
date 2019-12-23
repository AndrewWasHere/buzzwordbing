# Buzzword Bingo

Website to host buzzword bingo games.

## Use

To launch the buzzword bingo website, use

```python buzzword_bingo.py buzzwords.txt```

or

```python buzzword_bingo.py -h```

for a list of all command line options.

## Disclaimer

This application uses `Flask.run()` to spin up the website, which is horribly
insecure. To quote the 
[documentation](https://flask.palletsprojects.com/en/1.1.x/api/?highlight=flask%20run#flask.Flask.run),

    Do not use run() in a production setting. It is not intended to meet 
    security and performance requirements for a production server.
    
If you stick this application on your webserver out in the wild and bad things
happen, it's not my fault.

## License

Copyright 2019, Andrew Lin.
All rights reserved.

This software is released under the BSD 3-clause license. See
LICENSE.txt or https://opensource.org/licenses/BSD-3-Clause for more
information.
