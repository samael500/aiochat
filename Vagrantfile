# vi:syntax=ruby
ip_address = "10.1.1.111"
hostname = "aiochat"
box_name = "samael500/aiochat"

SYNC_FOLDER = true

unless Vagrant.has_plugin?("vagrant-fabric")
  raise "
    vagrant-fabric is not installed!
    please run the follow commands:
      $ vagrant plugin install vagrant-fabric
      $ sudo apt-get install fabric
  "
end

Vagrant.configure(2) do |config|
  # Virtual machine parameters
  config.vm.box = "#{box_name}"
  config.vm.network "private_network", ip: ip_address

  config.vm.synced_folder ".", "/vagrant", disabled: true
  if SYNC_FOLDER then
    if ENV['CI_FLAG'] or ENV['NO_NFS'] then
      config.vm.synced_folder ".", "/home/vagrant/proj", type: "rsync"
    else
      config.vm.synced_folder ".", "/home/vagrant/proj", type: "nfs",
      :mount_options => ['actimeo=2']
    end
  end

  config.vm.hostname = hostname
  config.vm.post_up_message = "#{hostname} dev server successfuly started.
    Connect to host with:
    http://#{ip_address}/
    or over ssh with `vagrant ssh`
  "

  # Set box name
  config.vm.define :"#{hostname}_vagrant" do |t|
  end
  # Virtualbox specific parameters
  config.vm.provider "virtualbox" do |v|
    v.name = "#{hostname}_vagrant"
    v.memory = 2048
    v.cpus = 2
  end
  # Provisioning with Fabric
  config.vm.provision :fabric do |fabric|
    fabric.fabfile_path = "./provision/fabric_provisioner.py"
    fabric.tasks = [
      "common",
      "database",
      "nginx",
      "app",
    ]
    fabric.tasks.push("localserver") unless ENV['CI_FLAG']
  end
end
