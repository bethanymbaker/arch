import subprocess

command_1 = 'gcloud config set project iris-226418'

process = subprocess.Popen(command_1.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

ssh_command = """
gcloud compute --project "iris" ssh --zone "us-east1-b" "arceus"
"""

process = subprocess.Popen(ssh_command.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
