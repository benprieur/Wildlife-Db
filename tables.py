TABLES = {}
TABLES['MAINTABLE'] = (
    " CREATE TABLE OKFN.MAINTABLE (" 
    " ID INT not null auto_increment," 
    " nom VARCHAR(200) NULL,"     
    " wikidataid VARCHAR(200) NULL," 
    " image VARCHAR(200) NULL," 
    " rangtaxinomique VARCHAR(200) NULL,"     
    " nomscientifique VARCHAR(200) NULL," 
    " taxonsuperieur VARCHAR(200) NULL," 
    " citesid VARCHAR(200) NULL,"     
    " PRIMARY KEY (ID)" 
    " ) ENGINE=InnoDB;")