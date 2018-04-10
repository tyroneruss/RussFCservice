

-- -----------------------------------------------------
-- Table `rlgdb`.`websource`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `rlgdb`.`websource` ;

CREATE TABLE IF NOT EXISTS `rlgdb`.`websource` (
  `WebsourceID` SMALLINT NOT NULL AUTO_INCREMENT,
  `Company`  VARCHAR(64) NOT NULL,
  `Type`  VARCHAR(64) NOT NULL,
  `Active` SMALLINT NOT NULL,
  PRIMARY KEY (`WebsourceID`))
ENGINE = InnoDB;
ALTER TABLE websource AUTO_INCREMENT=1;

-- -----------------------------------------------------
-- Table `rlgdb`.`User`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `rlgdb`.`user` ;

CREATE TABLE IF NOT EXISTS `rlgdb`.`user` (
  `UserID` SMALLINT NOT NULL AUTO_INCREMENT,
  `Username` VARCHAR(45) NOT NULL,
  `Password` VARCHAR(30) NOT NULL,
  `Active` SMALLINT NOT NULL,
  UNIQUE INDEX `UserID_UNIQUE` (`UserID` ASC),
  PRIMARY KEY (`UserID`),
  UNIQUE INDEX `Username_UNIQUE` (`Username` ASC))
ENGINE = InnoDB;
ALTER TABLE user AUTO_INCREMENT=1000;

Insert into websource (Company,Type,Active)
Values('Adridgepite','Law firm',1);

Insert into websource (Company,Type,Active)
Values('Brock & Scott','Law firm',1);

Insert into websource (Company,Type,Active)
Values('Martin & Brunavs','Law firm',1);

Insert into websource (Company,Type,Active)
Values('McCalla & Raymer','Law firm',1);

Insert into websource (Company,Type,Active)
Values('Rubin & Lublin','Law firm',1);

Insert into websource (Company,Type,Active)
Values('Shapiro & Gasting','Law firm',1);

Insert into websource (Company,Type,Active)
Values('Equity Depot','Home Listing  Service',1);

Insert into websource (Company,Type,Active)
Values('RealtyTrac','Home Listing  Service',1);

Insert into websource (Company,Type,Active)
Values('Realty.com','Home Listing  Service',1);

Company                         Type
Adridgepite			Law firm
Martin & Brunavs		Law firm
McCalla & Raymer		Law firm
Rubin & Lublin			Law firm
Shapiro & Gasting		Law firm
Realty.com			Home Listing Company
Equity Depot			Home Listing Company
RealtyTrac                      Home Listing Company
Brock & Scott			Law firm
Duplicates
Total number of records