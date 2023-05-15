CREATE USER 'eurostat_ro' IDENTIFIED BY 'eurostat_ro';
GRANT SELECT ON eurostat.* TO 'eurostat_ro';
FLUSH PRIVILEGES;