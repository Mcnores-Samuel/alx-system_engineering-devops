# kills a process named killmenow.
# Requirements:
#   Must use the exec Puppet resource
#   Must use pkill

exec { 'killmenow':
  command => 'pkill killmenow',
  onlyif  => 'pgrep killmenow'
}
