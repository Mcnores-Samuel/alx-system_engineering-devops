#  Creates a custom HTTP header response, but with Puppet
#  Server's default HTTP header response as a base.

exec { 'puppetserver-add-custom-header':
  command  => "sudo apt-get update -y; sudo apt-get install nginx -y; echo 'add_header X-Served-By $HOSTNAME' >> /etc/nginx/sites-available/default; sudo service nginx restart",
  provider => shell,
}

