# FLASKTASKTRACKER
This is a simple task tracker written by me with a help of a ChatGPT (Such an amazing tool! :D) I would like to update it in the future. Please help yourself if You need it as a boilerplate.

To run it:
- Download all files
- use command `python3 app.py` inside directory with all files

It will automatically run the server locally on `127.0.0.1:5000`

If You want to serve it on your local machine for hosts inside your network just change last line in the app.py from: `app.run(debug=True)` to `app.run(host="0.0.0.0", port=5000, debug=True)`

To identify Your IP use `ifconfig`/`ip a` on Linux or `ipconfig` on Windows
