# Increase the file descriptor limits for the holberton user to prevent "Too many open files" errors.

# Increase the file descriptor limits for the holberton user to prevent "Too many open files" errors

exec { 'increase-hard-file-limit-holberton-user':
  command => 'sed -i "/^holberton.*hard.*nofile/ s/[0-9]\\+$/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin:/bin:/usr/bin:/usr/sbin:/sbin',
}

exec { 'increase-soft-file-limit-for-holberton-user':
  command => 'sed -i "/^holberton.*soft.*nofile/ s/[0-9]\\+$/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin:/bin:/usr/bin:/usr/sbin:/sbin',
}
