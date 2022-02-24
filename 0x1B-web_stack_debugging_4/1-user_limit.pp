# User limit
exec { 'fixhard' :
    provider => shell,
    command  => 'sed -i sed -i s/5/4069/ /etc/security/limits.conf'
}
exec { 'fixsoft' :
    provider => shell,
    command  => 'sed -i sed -i s/4/4069/ /etc/security/limits.conf'
}
