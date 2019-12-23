#
# Copyright 2019 Andrew Lin. All rights reserved.
#
# This software is released under the BSD 3-clause license. See LICENSE.txt or
# https://opensource.org/licenses/BSD-3-Clause for more information.
#
from flask import Flask


class BingoServer(Flask):
    """Bingo Server Front End"""
    def __init__(self, import_name, **kwargs):
        """Constructor."""
        super().__init__(import_name, **kwargs)


app = BingoServer(__name__)
"""
@app.route("/")
def root():
    return the_html / render_template("/templates/root.html")
"""
