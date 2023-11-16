#!/usr/bin/bash

cat > webtech.service << END
# /etc/systemd/system/helloapp.service
[Unit]
Description=Advanced Webtech App
After=network.target

[Service]
Type=simple
User=root
Group=root
WorkingDirectory=/home/$USER/starlord/starlord
ExecStart=/home/$USER/starlord/starlord/bin/waitress-serve --listen=127.0.0.1:5000 app:app
Restart=always

[Install]
WantedBy=multi-user.target
END
