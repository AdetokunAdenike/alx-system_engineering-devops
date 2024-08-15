# This Puppet manifest ensures the Apache log
# directory exists with the correct permissions

file { '/var/log/apache2':
  ensure => directory,
  owner  => 'root',
  group  => 'adm',
  mode   => '0755',
}

service { 'apache2':
  ensure => running,
  enable => true,
}
