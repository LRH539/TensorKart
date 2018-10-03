# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"

  config.vm.synced_folder ".", "/vagrant", type: "rsync"

  config.vm.provider "virtualbox" do |vb|
    vb.gui = true
    vb.memory = "4096"
    vb.customize ["modifyvm", :id, "--usb", "on"]
    vb.customize ['usbfilter', 'add', '0', '--target', :id, '--name', 'GAMEPAD', '--vendorid', '0x045e', '--productid', '0x028e']
    vb.customize ["modifyvm", :id, "--vram", "16"]
  end

  # Most dependencies are being installed through apt, but
  # matplotlib from apt is built with pyqt4 support instead
  # of pyqt5, so it's installed through pip3.

  config.vm.provision "shell", env: {"DEBIAN_FRONTEND" => "noninteractive", "GAMEPAD" => "HJC Game GAMEPAD", "BRANCH" => "develop"}, inline: <<-SHELL
    apt-get update \
    && apt-get install -y xorg fluxbox build-essential cmake pkg-config linux-headers-$(uname -r) virtualbox-guest-dkms virtualbox-guest-x11 python-pip libpng-dev libfreetype6-dev python-tk mupen64plus \
    && pip install --upgrade pip \
    && modprobe vboxvideo \
    && cd /vagrant \
    && pip install -r requirements.txt \
    && mkdir -p /vagrant/mupen64plus-src && cd $_ \
    && [ -d mupen64plus-core ] || git clone https://github.com/mupen64plus/mupen64plus-core \
    && [ -d gym-mupen64plus ] || git clone --single-branch --branch multiplayer https://github.com/emomicrowave/gym-mupen64plus \
    && [ -d mupen64plus-input-bot ] || git clone --single-branch --branch multiplayer https://github.com/emomicrowave/mupen64plus-input-bot \
    && cd /vagrant/mupen64plus-src/gym-mupen64plus \
    && pip install -e . \
    && apt-get install -y libjson-c-dev libjson-c2 xvfb \
    && cd /vagrant/mupen64plus-src/mupen64plus-input-bot \
    && make all \
    && make install \
    && wget -q -O "/vagrant/mupen64plus-src/gym-mupen64plus/gym_mupen64plus/ROMs/marioKart.n64" "https://cdn.rawgit.com/ozanerhansha/FileToPNG/00619a66/filepng/Mario%20Kart%2064%20(USA).n64" \
    && cd /tmp \
    && wget -q https://netix.dl.sourceforge.net/project/virtualgl/2.6/virtualgl_2.6_amd64.deb \
    && dpkg -i virtualgl_2.6_amd64.deb \
    && grep -q "\[$GAMEPAD\]" /usr/share/games/mupen64plus/InputAutoCfg.ini || sed -i "/\[Microsoft X-Box 360 pad\]/a\[$GAMEPAD\]" $_ \
    && usermod -a -G input vagrant
  SHELL
end
