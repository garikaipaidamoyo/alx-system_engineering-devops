# Kills a process name killmenow

exec { 'killmenow':
  path     => '/usr/bin:/bin',
  command  => 'pkill killmenow',
  onlyif      => 'pgrep killmenow',
  refreshonly => true,
}
