#Puppet install Pacakge
  exec { 'puppet-lint': #InstallPackagePuppet lint
	command => '/bin/gem install puppet-lint -v 2.5.0'
    }
