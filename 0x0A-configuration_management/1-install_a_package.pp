# install flask from pip3.
# Requirements:
#   Install flask
#   Version must be 2.1.0
exec {
  'install flask':
  command => '/usr/bin/pip3 install flask==2.1.0'
}
