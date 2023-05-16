'''
CREATE TABLE IF NOT EXISTS `musk_twitter`(
   `id` INT UNSIGNED AUTO_INCREMENT,
   `update_time` DATETIME NOT NULL,
   `ttime` VARCHAR(100) NOT NULL,
   `ttype` VARCHAR(40) NOT NULL,
   `content` VARCHAR(500) NOT NULL,
   PRIMARY KEY ( `id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `formula_news`(
   `id` INT UNSIGNED AUTO_INCREMENT,
   `update_time` DATETIME NOT NULL,
   `ntime` VARCHAR(100) NOT NULL,
   `ntype` VARCHAR(40) NOT NULL,
   `content` VARCHAR(500) NOT NULL,
   `url` VARCHAR(200) NOT NULL,
   `tokens` VARCHAR(200) NOT NULL, 
   PRIMARY KEY ( `id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
ALTER TABLE formula_news ADD `ntype_num` INT NOT NULL;

CREATE TABLE IF NOT EXISTS `web3_jobs`(
  `id` INT UNSIGNED AUTO_INCREMENT,
   `update_time` DATETIME NOT NULL,
   `jtype` VARCHAR(40) NOT NULL,
   `content` VARCHAR(500) NOT NULL,
   PRIMARY KEY ( `id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''

import pymysql.cursors


# Connect to the database
connection = pymysql.connect(host='rm-2vcm58w8rgd7p3i9rio.mysql.cn-chengdu.rds.aliyuncs.com',
                             user='root',
                             password='Aa337877123',
                             database='tg',
                             cursorclass=pymysql.cursors.DictCursor)


def insert_musk(ttime, ttype, content):
  with connection.cursor() as cursor:
    # Create a new record
    sql = "INSERT INTO `musk_twitter` (`update_time`, `ttime`, `ttype`, `content`) VALUES (now(), %s, %s, %s)"
    cursor.execute(sql, (ttime, ttype, content))

  # connection is not autocommit by default. So you must commit to save
  # your changes.
  connection.commit()


def insert_news(ntime, ntype, content, url, tokens, ntype_num):
  with connection.cursor() as cursor:
    # Create a new record
    sql = "INSERT INTO `formula_news` (`update_time`, `ntime`, `ntype`, `content`, `url`, `tokens`, `ntype_num`) VALUES (now(), %s, %s, %s, %s, %s, %s)"
    try:
      cursor.execute(sql, (ntime, ntype, content, url, tokens, ntype_num))
    except Exception as e:
      print('Exception: ', e)
  # connection is not autocommit by default. So you must commit to save
  # your changes.
  connection.commit()

def insert_jobs(jtype, content):
  with connection.cursor() as cursor:
    # Create a new record
    sql = "INSERT INTO `web3_jobs` (`update_time`, `jtype`, `content`) VALUES (now(), %s, %s)"
    cursor.execute(sql, (jtype, content))

  # connection is not autocommit by default. So you must commit to save
  # your changes.
  connection.commit()


if __name__ == '__main__':
  insert_musk('12:00', 'reply', 'I love Doge')
  insert_news('12:00', 'reply', 'I love Doge', 'www.baidu.com', '$DOGE')
  insert_jobs('招聘', 'I love Doge')
