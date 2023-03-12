

create database studentID;
drop database studentID;



create table school(
    id  INT NOT NULL AUTO_INCREMENT,PRIMARY KEY(id),
    name varchar(20) NOT null
)

INSERT INTO school (name) VALUES ('anas'), ('imran'), ('aqueel'), ('mujju');