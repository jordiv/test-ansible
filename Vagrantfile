# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.define 'nginx'
  config.vm.box = "ubuntu/trusty64"
  config.vm.hostname = 'nginx'
  config.hostsupdater.aliases = ["testapp"]

  # accessing "localhost:8080" will access port 80 on the guest machine.
  config.vm.network "forwarded_port", guest: 80, host: 8080
  config.vm.network "private_network", ip: "192.168.33.10"
  config.vm.synced_folder "data", "/vagrant_data"

  config.vm.provider "virtualbox" do |vb|
    # Customize the amount of memory on the VM:
    vb.memory = "1024"
  end
  config.vm.provision 'ansible' do |ansible|
    ansible.playbook = 'tasks/nginx-reverse-proxy.yml'
    ansible.raw_arguments = ['--check', '-vvvv']
  end
end
