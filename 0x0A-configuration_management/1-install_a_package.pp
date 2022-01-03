#Puppet install Pacakge
  package { 'puppet-lint': #InstallPackagePuppet lint
  ensure   => '2.5.0',
  provider => 'gem'
    }
