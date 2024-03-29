# Sets up client SSH configuration file so that it can connect to a server without typing a password.
# Requirements:
#   private key ~/.ssh/school
#   configured to refuse to authenticate using a passwor
file_line { 'identity_file':
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/school',
}

file_line { 'passwd_auth':
  path    => '/etc/ssh/ssh_config',
  line    => 'PasswordAuthentication no',
}
