# slws
A Simple Local Web Server to deliver files to local apps using http rather than file system


## Usage

0. Compile app to single executable file by launching `make-exe.bat` (find slws.exe in /dist folder). Compiled exe is also attached in this repo.

1. Start server using: 
```
  slws.exe --port 8080 --folder my_files                                                                                
  slws.exe --port 8080
  slws.exe --folder my_files                                                                                            
  slws.exe              # defaults: port 5000, folder shared_files
```

2. In same folder as slws.exe, a new folder will be created (`shared_files` by default, or as per argument you chose) after you launched slws.exe
3. Copy any files you wish in that folder 
4. Access the files by going to `http://127.0.0.1:5000` (or any ports that is open and that you chose in your argument)
5. Profit

Note : the files will be delivered AS IS (it's not a PHP, node etc server, simply delivering files).
