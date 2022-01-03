  file { '/tmp/school': #the path of the new file
    content => 'I love Puppet',
    owner   => 'www-data',
    group   => 'www-data',
    mode    => '0744',
    }
