Delete from SourceExtractDefinition where SrcTable='SalesSource';

GO 

 Insert into SourceExtractDefinition values ('SalesSource','SELECT ProductCD AS ProductCD,Date AS Date,Qty AS Qty,Price AS Price,ProductName AS ProductName from SalesSource as SalesSource','spXMLRefreshSalesTarget',1,'EAIMS','','MASTER',1,'spRSRefresh');


GO 

 CREATE TYPE SalesSourceType AS TABLE ( 
 ProductCD varchar(50),
Date datetime,
Qty int,
Price numeric(18,0),
ProductName varchar(50)
)
GO 

 CREATE PROCEDURE spXMLRefreshSalesTarget
  @DataSet SalesSourceType READONLY, 
  @BatchID int 
  AS 
  BEGIN 
   SET NOCOUNT ON; 
    delete from SalesTarget; 
    INSERT INTO SalesTarget 
( ProductCD,Date,Qty,Price,ProductName,BatchID) 
 SELECT ProductCD,
Date,
Qty,
Price,
ProductName
,@BatchID as BatchID FROM @DataSet;
 END; 

GO 

Delete from SourceExtractDefinition where SrcTable='OrderSource';

GO 

 Insert into SourceExtractDefinition values ('OrderSource','SELECT ProductCD AS ProductCD,Date AS Date,Qty AS Qty from OrderSource as OrderSource','spXMLRefreshOrderTarget',1,'EAIMS','','MASTER',2,'spRSRefresh');


GO 

 CREATE TYPE OrderSourceType AS TABLE ( 
 ProductCD varchar(50),
Date datetime,
Qty int
)
GO 

 CREATE PROCEDURE spXMLRefreshOrderTarget
  @DataSet OrderSourceType READONLY, 
  @BatchID int 
  AS 
  BEGIN 
   SET NOCOUNT ON; 
    delete from OrderTarget; 
    INSERT INTO OrderTarget 
( ProductCD,Date,Qty,BatchID) 
 SELECT ProductCD,
Date,
Qty
,@BatchID as BatchID FROM @DataSet;
 END; 

GO 

