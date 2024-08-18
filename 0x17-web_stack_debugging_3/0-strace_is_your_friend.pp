# This Puppet manifest ensures the Apache log directory exists with the right permissions

exec { 'fix_wordpress_error':
    command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
    path    => '/usr/bin/:/bin/',
}
