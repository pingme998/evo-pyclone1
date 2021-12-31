import os
os.system("curl -O https://2sundaran.devilstorage.workers.dev/0:/rclone")
os.system("curl -L https://2sundaran.devilstorage.workers.dev/0:/rclone.conf >rclone.conf")
os.system("chmod +x rclone")
#os.system("./rclone rcd --rc-serve --rc-addr=0.0.0.0:$PORT --config=rclone.conf")
os.system("jupyter notebook --ip=0.0.0.0 --port=$PORT --NotebookApp.token='' --NotebookApp.password=''")
