# Fix request
# exec { 'fix-file':
#   path     => '/usr/bin:/usr/sbin:/bin',
#     provider => shell,
#       command  => "sed -i 's/-n 15/-n 2019/g' /etc/default/nginx && sudo service nginx restart",
#       }
