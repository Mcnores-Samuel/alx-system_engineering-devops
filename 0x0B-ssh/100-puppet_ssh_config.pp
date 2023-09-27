# Sets up client SSH configuration file so that it can connect to a server without typing a password.
# Requirements:
#   private key ~/.ssh/school
#   configured to refuse to authenticate using a password

class ssh_config {
  file {
    '/etc/ssh/ssh_config':
    path => '/etc/ssh/ssh_config',
    ensure => present,
    line => "IdentityFile ~/.ssh/school"
  }

  file {
    '/etc/ssh/sshd_config':
    path => '/etc/ssh/sshd_config',
    ensure => present,
    line => "PasswordAuthentication no"
  }
}
