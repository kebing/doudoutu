
-- 创建数据库时，带指定语言
CREATE DATABASE ip469 CHARACTER SET gbk COLLATE gbk_bin;

-- 导数据时，要用下面的方式
SELECT * FROM ip_ipv4info INTO OUTFILE '/tmp/ipv4info.txt';
LOAD DATA INFILE '/tmp/ipv4info.txt' INTO TABLE ip_ipv4info;
