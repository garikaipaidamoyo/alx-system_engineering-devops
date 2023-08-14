class apache_config_fix {
  file { '/etc/apache2/sites-available/my-site.conf':
    ensure  => file,
    source  => 'puppet:///modules/alx-system_engineering-devops/0x17-web_stack_debugging_3/my-site.conf',  
    notify  => Service['apache2'],
  }
  
  service { 'apache2':
    ensure => running,
    enable => true,
  }
  
  notify { "File path: ${modulepath('alx-system_engineering-devops/0x17-web_stack_debugging_3')}": }
}

include apache_config_fix
