# Using Puppet to make changes to our configuration file.

file { '/etc/ssh/ssh_config':
	ensure	=> 'file',
	owner	=> 'root',
	group	=> 'root',
	mode	=> '0644',
}

file_line { 'Turn off passwd auth':
	path	=> '/etc/ssh/ssh_config',
	line	=> 'PasswordAuthentication no',
	match	=> '^#?PasswordAuthentication',
}

file_line { 'Declare identity file':
	path	=> '/etc/ssh/ssh_config',
	line	=> 'IdentityFile ~/.ssh/school',
	match	=> '^#>IdentityFile',
}
