su -
dnf -y update
dnf -y install vim bash-completion curl wget telnet
dnf -y install httpd
dnf -y install apache2
dnf -y install git
dnf -y install mariadb-server
setenforce 0
sed -i 's/^SELINUX=.*/SELINUX=disabled/g' /etc/selinux/config
dnf -y install php php-cli php-php-gettext php-mbstring php-mcrypt php-mysqlnd php-pear php-curl php-gd php-xml php-bcmath php-zip

