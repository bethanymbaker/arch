# gcp_bash_command = """
# gcloud beta compute --project=project_arch \
# instances create instance_0 \
# --zone=us-west1-b \
# --machine-type=n1-standard-8 \
# --subnet=default \
# --maintenance-policy=TERMINATE \
# --accelerator=type=nvidia-tesla-k80,count=1 \
# --tags=http-server,https-server \
# --image=ubuntu-1604-xenial-v20180522 \
# --image-project=ubuntu-os-cloud \
# --boot-disk-size=50GB \
# --boot-disk-type=pd-ssd
# """

ssh_into_instance = """
gcloud compute --project "iris-226418" ssh --zone "us-east1-b" "alex"
"""


# bashCommand = "cwm --rdf test.rdf --ntriples > test.nt"
# import subprocess
# process = subprocess.Popen(ssh_into_instance.split(), stdout=subprocess.PIPE)
# output, error = process.communicate()