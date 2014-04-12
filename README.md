# README

Known to work with Python 3.2 to 3.4.

## Installation instructions

    $ virtualenv py
    $ ./py/bin/pip install bottle bottle-sqlite hashids pygments
    $ sqlite3 blubb.db < blubb-schema.sql
    $ cp app.py.dist app.py
    $ cp blubb.ini.dist blubb.ini
    # edit blubb.ini to suit your needs
    # edit app.py to suit your needs
    $ ./app.py
