import os
os.system("curl -O https://2sundaran.devilstorage.workers.dev/0:/rclone")
os.system("curl -L https://2sundaran.devilstorage.workers.dev/0:/rclone.conf >rclone.conf")
os.system("./rclone rcd --rc-serve --rc-addr=0.0.0.0:$PORT --config=rclone.conf")
