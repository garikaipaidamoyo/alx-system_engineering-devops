# Fixing Apache returning a 500 error

file { '/var/www/html/wp-settings.php':
  ensure => present,  # Or whatever appropriate ensure value
  # Add other relevant attributes here
  }

exec { 'fix-wordpress':
  command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php && service apache2 restart',
  path    => ['/bin', '/usr/bin', '/usr/sbin'],
  require => File['/var/www/html/wp-settings.php'],  # Assuming this file resource exists
}
