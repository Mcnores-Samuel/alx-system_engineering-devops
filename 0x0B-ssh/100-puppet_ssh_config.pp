# Sets up client SSH configuration file so that it can connect to a server without typing a password.
# Requirements:
#   private key ~/.ssh/school
#   configured to refuse to authenticate using a password

file {
  '~/.ssh/config':
  ensure  => present,
  content => 'Host *\n\tIdentityFile ~/.ssh/school\nPubkeyAuthenticarion no'
}
