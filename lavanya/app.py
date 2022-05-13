"""
app

This holds all "app" operations.

Copyright (c) 2022 Goutham Krishna K V

All file saving and uploading operations are UUID-based, so that no information
about the audio are there in URL. This method is more secure because:

1. No data about the file is sent as part of the URL.
2. Since UUID is randomly generated, one can't access different audio files
    by just changing the id in path. UUIDs are randomly generated, so finding
    an existing file is close to impossible.

Templates can be accessed from `./templates/`
"""

# -- IMPORTS: Libraries

# - Standard Library Imports

#   - "os" imports for file access, file operations
from os import getcwd, path, mkdir, walk

#   - "uuid" imports as all operations are UUID-based
from uuid import UUID, uuid4

# - Flask Imports
from flask import (
    Blueprint,
    flash,
    render_template,
    request,
    redirect,
    url_for,
    send_file,
)


# -- INITIALIZE CONSTANTS

FILEPATH_ROOT = "files"


# - INITIALIZE APP BLUEPRINT

app_bp = Blueprint("app", __name__, url_prefix="/app")


# -- BLUEPRINT ROUTES

# - Get app root
@app_bp.route("/", methods=["GET"])
def root():
    """
    root

    This provides tha website root.
    """
    return render_template("index.html")


# - Accept uploading file
@app_bp.route("/upload", methods=["POST"])
def upload_audio_file():
    """
    upload_audio_file

    This gets an audio file, assigns a UUID for the audio file, and redirects to
    an "uploaded" file where you can play the uploaded file, or download it to
    your computer.
    """
    if request.method == "POST":
        # Check if files are there
        file = request.files.get("file-upload", None)
        if file:
            # Try to save the file.
            try:
                # Create the file names for us.
                file_uuid = str(uuid4())
                root_path = path.join(FILEPATH_ROOT, file_uuid)
                # Create the file directory, you want the files in.
                mkdir(root_path)
                # Join the paths to form the saveable file url.
                full_file_path = path.join(root_path, (file.filename))
                # Full File Path
                print(full_file_path)
                # Save the file
                file.save(full_file_path)
                # File has been saved.
                flash("File saved.", category="success")
                return render_template(
                    "uploaded.html", uploaded=True, uploaded_filename=file_uuid
                )
            except FileNotFoundError as fe:
                flash(f"File not found: {fe.filename}", category="danger")
            except OSError as ose:
                flash(f"OS Error: {ose.filename}", category="danger")
            return render_template("uploaded.html", uploaded=False)
        flash("Cannot find file in form.", category="danger")
    return redirect(url_for(".root"))


@app_bp.route("/audio/<uuid:audio_uuid>")
def get_audio(audio_uuid: UUID):
    """
    get_audio

    This method provides the user the option to either download the audio, or to
    play it in your browser itself.
    """
    # - Whether to download or play?
    download_file = request.args.get("download", False) == "true"
    # Generate the file path
    root_path = path.join(getcwd(), FILEPATH_ROOT, str(audio_uuid))
    # Get the first (only) file inside the directory
    _, _, file = list(walk(root_path))[0]
    file = file[0]
    # Send back the file
    return send_file(
        path.join(root_path, file), download_name=file, as_attachment=download_file
    )
