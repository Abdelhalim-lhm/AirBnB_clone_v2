# setting the web_static using puppet

package { 'nginx':
  ensure => present,
}

exec {'install':
  command  => 'sudo apt-get update ; sudo apt-get -y install nginx',
  provider => shell,
}

exec { 'create_data':
  command  => 'sudo mkdir -p /data/',
  provider => shell,
}

exec { 'create_web_static':
  command  => 'sudo mkdir -p /data/web_static/',
  provider => shell,
}

exec { 'create_release':
  command  => 'sudo mkdir -p /data/web_static/releases/',
  provider => shell,
}

exec { 'create_shared':
  command  => 'sudo mkdir -p /data/web_static/shared',
  provider => shell,
}

exec { 'create_test':
  command  => 'sudo mkdir -p /data/web_static/releases/test/',
  provider => shell,
}

exec { 'create_index':
  command  => 'sudo touch /data/web_static/releases/test/index.html',
  provider => shell,
}

exec { 'create_index_content':
  command  => 'sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html',
  provider => shell,
}

exec { 'create_link':
  command  => 'sudo ln -sf /data/web_static/releases/test/ /data/web_static/current',
  provider => shell,
}

file { '/data':
  ensure  => directory,
  recurse => true,
  owner   => 'ubuntu',
  group   => 'ubuntu',
}

exec { 'default_index':
  command  => 'sudo sed -i "/listen 80 default_server/a\
        location /hbnb_static/ {\
    \n\t\talias /data/web_static/current/;\
    \n\t}" /etc/nginx/sites-enabled/default',
  provider => shell,
}

exec { 'run':
  command  => 'sudo service nginx restart',
  provider => shell,
}
