CREATE TABLE DividendsHistorical (
                symbol VARCHAR(100) NOT NULL,
                symbolDate DATE NOT NULL,
                label VARCHAR(100),
                adjDividend FLOAT,
                dividend FLOAT,
                recordDate DATE,
                paymentDate DATE,
                declarationDate DATE,
                PRIMARY KEY (symbol, symbolDate)
);


CREATE TABLE DelistedCompanies (
                symbol VARCHAR(50) NOT NULL,
                companyName VARCHAR(200),
                exchange VARCHAR(100),
                ipoDate DATE,
                delistedDate DATE,
                PRIMARY KEY (org_id)
);