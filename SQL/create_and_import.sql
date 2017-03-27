DROP TABLE IF EXISTS raw_data;

CREATE TABLE `hmis`.`raw_data` (`Row_ID` int, `Ethinicity` varchar(50), `Gender` varchar(30), `Primary_Race` varchar(50), `Client_Secondary_Race` varchar(50), `ProviderID` text, `ProviderName` text,`ProviderCounty` text,`ProviderPlace` text,`ProviderCode` text,
 `Entry_Exit_Provider_Program_Type_Code` text, `EntryDate` varchar(20), `ExitDate` varchar(20), `Client_Veteran_Status` varchar(10), `ServedInMilitary` varchar(10), `ClientHomeless` varchar(10),
 `ChronicallyHomeless` varchar(10), `HousingStatus` text, `PrimaryHomelessnessReason` text, `SecondaryHomelessnessReason` text, `HmlessDueToForeclose` varchar(10), `WhereStayedNightBefore` text,
 `TypeOfLivingSituation` text, `LengthOfStayLivingSituation` text, `LastPermZipCode` int, `ZipCodeQuality` text, `HousingCategory` text, `Report_Date_File` text, `ISC_ClientID` int,
 `ISC_EEUid` int, `ISC_Household_Uid` int);

LOAD DATA INFILE 'D:/SSDI_Sprints/raw_data/HMIS.csv' 
INTO TABLE hmis.raw_data 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

CREATE TABLE hmis.places ('placeID' int, 'providerName' VARCHAR(50), 'providerCounty' VARCHAR(50), 'Adress' VARCHAR(100), 'addrType' VARCHAR(30), 'addrLocat' VARCHAR(30), 'Y' DECIMAL(11, 8), 'X' DECIMAL(10, 8))