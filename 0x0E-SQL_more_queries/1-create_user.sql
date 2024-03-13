-- Creates user_0d_1 with password user_0d_1_pwd
-- Grants user_0d_1 all privileges
-- Script should not fail if user_0d_1 exists
    CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';

GRANT ALL PRIVILEGES
   ON *.*
   TO 'USER_0d_1'@'localhost'
 WITH GRANT OPTION;

FLUSH PRIVILEGES;