import http.server
import socketserver
import webbrowser
import os
import sys

# Set the port
PORT = 8000

# Get the directory of this script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Change directory to where the HTML files are stored
os.chdir(script_dir)

# Create a handler to serve files
Handler = http.server.SimpleHTTPRequestHandler

# Set up the server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    # Automatically open the default browser to the right address
    print(f"Serving at http://localhost:{PORT}")
    webbrowser.open(f"http://localhost:{PORT}")

    # Keep the server running
    httpd.serve_forever()
