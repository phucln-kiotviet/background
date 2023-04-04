import ansible_runner
import json
# import os


def run(event_handler, callback):
    private_data_dir = "../phucln-ansible"
    inventory = "../phucln-ansible/inventory/inventory.yml"
    playbook = "../phucln-ansible/playbook/tcpdump-linux.yml"
    extra_vars = dict(
        {"cap_length": "20", "dst_filter": "192.168.122.22", "ansible_user": "root"})
    ansible_runner.run(
        playbook=playbook,
        private_data_dir=private_data_dir,
        quiet=True,
        extravars=extra_vars,
        inventory=inventory,
        event_handler=event_handler,
        finished_callback=callback
    )
