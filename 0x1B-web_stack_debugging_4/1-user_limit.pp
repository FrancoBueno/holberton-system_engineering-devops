# User limit
exec { 'hard':
    provider => shell,
    command  => 'sed -i sed -i s/5/4069/ /etc/security/limits.conf'
}
exec { 'soft':
    provider => shell,
    command  => 'sed -i sed -i s/4/4069/ /etc/security/limits.conf'
}
