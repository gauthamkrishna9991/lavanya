"""
Lavanya

Upload an Audio file, and save it into your computer (UUID-based).

Copyright (c) 2022 Goutham Krishna K V

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""

__version__ = '0.1.0'

# -- IMPORTS: Libraries

# - Standard Library Imports
from os import getcwd, path

# - Flask Imports
from flask import Flask, redirect, url_for, send_file


def create_app(test_config = None):
    """
    create_app

    This function creates the standard flask app, and includes the blueprint
    for our standard app onto the main app.
    """
    # -- INITIALIZE APP --
    app = Flask(__name__, instance_relative_config=True)

    # -- APP CONFIG --
    app.config.from_mapping(SECRET_KEY="lavanya_dev")

    # -- BLUEPRINT INCLUDES --

    # - Include App Blueprint
    from . import app as mod_app

    # - Register the Blueprint
    app.register_blueprint(mod_app.app_bp)

    # -- APP ROUTES --

    # - This returns "Hello, World!"
    @app.route("/hello")
    def hello() -> str:
        """
        This just returns the string "Hello, World!"
        """
        return "Hello, World!"

    # - This redirects to app root ("/app")
    @app.route("/")
    def redirect_to_app():
        """
        Redirect from root to app.root path ("/app")
        """
        return redirect(url_for('app.root'))

    # - Add favicon access
    @app.route("/favicon.ico")
    def get_favicon():
        """
        This sets the favicon for the website.
        """
        return send_file(path.join(getcwd(), "favicon.ico"))

    #  -- RETURN FLASK APP --    
    return app
