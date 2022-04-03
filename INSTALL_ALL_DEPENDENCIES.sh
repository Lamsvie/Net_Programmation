#!/bin/sh
# Author:   Fatima Cissé & Mouhamed
#---------------------------------------------------------------------
    # This file is part of MySQL and iRedMail dependencies'installation,
    # which is an open source database and mail server
    # solution for Red Hat(R) Enterprise Linux, CentOS, Debian and Ubuntu.
    #
    # iRedMail is free software: we can redistribute it and/or modify
    # it under the terms of the GNU General Public License as published by
    # the Free Software Foundation, either version 3 of the License, or
    # (at your option) any later version.
    #
    # MySQL is a fast, multi-threaded, multi-user, and robust SQL database server. 
    # It is intended for mission-critical,heavy-load production systems and mass-deployed software. 
    #---------------------------------------------------------------------

# ------------------------------
# Define some global variables to locate dependencies.
# ------------------------------

#-------------------------------
	#MYSQL
#------------------------------

LIST_OF_MYSQL_DEPENDENCIES= "libaio1 libcgi-fast-perl libcgi-pm-perl libevent-core-2.1-7
  libevent-pthreads-2.1-7 libfcgi-perl libhtml-template-perl libmecab2
  mecab-ipadic mecab-ipadic-utf8 mecab-utils mysql-client-8.0
  mysql-client-core-8.0 mysql-server-8.0 mysql-server-core-8.0 "

apt-get update
apt-get install -y $LIST_OF_MYSQL_DEPENDENCIES


#-------------------------------    
         #Iredmail-server
#------------------------------

LIST_OF_IREDMAIL_DEPENDENCIES= "nginx mariadb-server dovecot postfix mlmmj amavisd
 iredapd sogo clamav spamassassin roundcube fail2ban "

apt-get install -y $LIST_OF_IREDMAIL_DEPENDENCIES
wget https://github.com/iredmail/iRedMail/archive/refs/tags/1.5.2.tar.gz
tar xvf iRedMail-1.5.2.tar.gz
cd iRedMail-1.5.2/
chmod + x iRedMail.sh
bash iRedMail.sh
