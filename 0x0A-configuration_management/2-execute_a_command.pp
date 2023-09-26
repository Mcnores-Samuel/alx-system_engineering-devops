# kills a process named killmenow.
# Requirements:
#   Must use the exec Puppet resource
#   Must use pkill

exec { 'killmenow':
  command => '/usr/bin/pkill killmenow',
  onlyif  => '/usr/bin/pgrep killmenow'
}
