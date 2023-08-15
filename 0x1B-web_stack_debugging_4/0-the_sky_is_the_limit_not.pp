#0-the_sky_is_the_limit_not.pp

exec { 'run_apache_bench':
  command => '/usr/bin/ab -n 2000 -c 100 http://172.17.0.3/',
}
