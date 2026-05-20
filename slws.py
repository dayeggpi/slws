import http.server
import socketserver
import os
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, default=5000)
parser.add_argument("--folder", type=str, default="shared_files")
args = parser.parse_args()

PORT = args.port
FOLDER_NAME = args.folder

# 1. Determine where the script or .exe is currently located
if getattr(sys, 'frozen', False):
    base_dir = os.path.dirname(sys.executable)
else:
    base_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Set the exact path to the folder we want to deliver over HTTP
SHARED_FOLDER_PATH = os.path.join(base_dir, FOLDER_NAME)

# 3. Create the folder automatically if it doesn't exist yet
os.makedirs(SHARED_FOLDER_PATH, exist_ok=True)

# 4. Change the built-in working directory so the server focuses ONLY on this folder
os.chdir(SHARED_FOLDER_PATH)

# Use the standard Basic Handler (no custom arguments required)
Handler = http.server.SimpleHTTPRequestHandler

if __name__ == "__main__":
    # 5. Start the server
    try:
        # Binding to 127.0.0.1 means it's localized to your computer.
        with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
            print("="*50)
            print(" Simple Local Web Server is Running! ")
            print(f" Serving folder : {SHARED_FOLDER_PATH}")
            print(f" Access URL     : http://127.0.0.1:{PORT}/")
            print("="*50)
            print("Drop any file into the folder.")
            print("Press Ctrl+C in this window to stop the server.")
            
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")