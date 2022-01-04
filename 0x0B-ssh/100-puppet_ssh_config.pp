# Client configuration file (w/ Puppet)
include stdlib

#import identity file

file_line { 'Declare line identity':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/school',
  replace => true
#Disable Auntentication in ssh_config
}
file_line { 'Turn off passwd auth':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => 'PasswordAutentication no',
  replace => true,
}
