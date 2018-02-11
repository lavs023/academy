# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.define "w2db" do |w2db|
  w2db.vm.box = "geerlingguy/centos7"
  w2db.vm.network "forwarded_port", guest: 3306, host: 3306
  w2db.vm.network "private_network", ip: "192.168.56.103"
   w2db.vm.provision "ansible_local" do |ansible|
     ansible.playbook = "playbook_db.yml"
      end
    end

  config.vm.define "w2wp" do |w2wp|
  w2wp.vm.box = "geerlingguy/centos7"
  w2wp.vm.network "forwarded_port", guest: 80, host: 80
  w2wp.vm.network "private_network", ip: "192.168.56.102"
   w2wp.vm.provision "ansible_local" do |ansible|
     ansible.playbook = "playbook.yml"
      end
    end

end
