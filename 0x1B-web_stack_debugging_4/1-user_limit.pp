# Increase the file descriptor limits for the holberton user to prevent "Too many open files" error.

exec { 'increase-hard-file-limit-holberton-user':
  command => 'sed -i "/^holberton.*hard.*nofile/ s/[0-9]\\+$/50000/" /etc/security/limits.conf || echo "holberton hard nofile 50000" >> /etc/security/limits.conf',
  path    => '/usr/local/bin:/bin:/usr/bin:/usr/sbin:/sbin',
  onlyif  => 'grep -q "^holberton.*hard.*nofile" /etc/security/limits.conf',
}

exec { 'increase-soft-file-limit-holberton-user':
  command => 'sed -i "/^holberton.*soft.*nofile/ s/[0-9]\\+$/50000/" /etc/security/limits.conf || echo "holberton soft nofile 50000" >> /etc/security/limits.conf',
  path    => '/usr/local/bin:/bin:/usr/bin:/usr/sbin:/sbin',
  onlyif  => 'grep -q "^holberton.*soft.*nofile" /etc/security/limits.conf',
}
