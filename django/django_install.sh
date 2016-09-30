#/bin/bash
basedir=/usr/local/src
cd $basedir
tar -zxf Python-2.7.7.tgz && cd Python-2.7.7
./configure --prefix=/usr/local/python  --enable-shared CFLAGS=-fPIC
make && make install

cd $basedir
tar -zxf apr-1.5.0.tar.gz
cd apr-1.5.0
./configure --prefix=/usr/local/apr
make && make install

cd $basedir
tar -zxf apr-util-1.5.3.tar.gz
cd apr-util-1.5.3
./configure --prefix=/usr/local/apr-util --with-apr=/usr/local/apr/bin/apr-1-config
make && make install

cd $basedir
tar -zxf pcre-8.39.tar.gz
cd pcre-8.39
./configure --prefix=/usr/local/pcre
make && make install

cd $basedir
tar -zxf httpd-2.4.23.tar.gz
cd  httpd-2.4.23
./configure --prefix=/usr/local/apache2 --with-apr=/usr/local/apr --with-apr-util=/usr/local/apr-util/  --with-pcre=/usr/local/pcre/
make && make install

cd $basedir
tar -zxf mod_wsgi-4.5.7.tar.gz
cd mod_wsgi-4.5.7
./configure --with-apxs=/usr/local/apache2/bin/apxs --with-python=/usr/local/python/bin/python
make && make install

chmod 755 /usr/local/apache2/modules/mod_wsgi.so

sed -i '/Listen 80/i\Listen 8'  /usr/local/apache2/conf/httpd.conf

cat >> /usr/local/apache2/conf/httpd.conf <<EOF
<VirtualHost *:800>
    DocumentRoot /web/mysite/mysite/
    <Directory /web/mysite/mysite/>
         Order allow,deny   
         Allow from all   
         Require all granted    
     </Directory>
WSGIScriptAlias / /web/mysite/mysite/wsgi.py
</VirtualHost>
EOF
pip install Djang

mkdir /tmp/.trac_egg
chown daemon:daemon /tmp/.trac_egg
#在wsgi.py添加配置
#sys.path.append("/web/mysite/") 
#os.environ['PYTHON_EGG_CACHE'] = '/tmp/.trac_egg'
