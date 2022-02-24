#increment the users nginx
exec { 'change-limit':
  provider => 'shell',
  command  => 'sed -i s/15/4069/ /etc/default/nginx; sudo service nginx restart'
}
