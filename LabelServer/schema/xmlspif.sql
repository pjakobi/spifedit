CREATE TABLE dbo.[categoryGroup] 
( 
	[categoryGroup_id] int Identity(1,1),
	[tagSetRef] 
    
      Tag Set Name
    
    

        varchar
      

    (256)

  
    
  ,
	[tagType] 
    
      Type of security category
    
    

        varchar
      
      
      
      
      
    
  ,
	[enumType] 
    
      Type of enumerated security category
    
    

        varchar
      
      
    
  ,
	[lacv] 
    
  ,
	[all] bit

	PRIMARY KEY ( [categoryGroup_id] )
)

CREATE TABLE dbo.[excludedCategory] 
( 
	[excludedCategory_id] int Identity(1,1),
	[tagSetRef] 
    
      Tag Set Name
    
    

        varchar
      

    (256)

  
    
  ,
	[tagType] 
    
      Type of security category
    
    

        varchar
      
      
      
      
      
    
  ,
	[enumType] 
    
      Type of enumerated security category
    
    

        varchar
      
      
    
  ,
	[lacv] 
    
  ,
	[all] bit

	PRIMARY KEY ( [excludedCategory_id] )
)

CREATE TABLE dbo.[requiredCategory] 
( 
	[requiredCategory_id] int Identity(1,1),
	[] ,
	[operation] 
    
      How associated categories should be applied
    
    

        varchar
      
      
      
    
  

	PRIMARY KEY ( [requiredCategory_id] )
)

CREATE TABLE dbo.[equivalentClassification] 
( 
	[equivalentClassification_id] int Identity(1,1),
	[policyRef] 
    
      Policy Name
    
    

        varchar
      

    (256)

  
    
  ,
	[lacv] 
    
      Label and Certificate integer or bit alue
    
    
  ,
	[applied] 
    
      When equivalencies can be applied
    
    

        varchar
      
      
      
    
  

	PRIMARY KEY ( [equivalentClassification_id] )
)

CREATE TABLE dbo.[equivalentPolicy] 
( 
	[equivalentPolicy_id] int Identity(1,1),
	[name] 
    
      Policy Name
    
    

        varchar
      

    (256)

  
    
  ,
	[id] 
    
      Object Identifier
    
    

        varchar
      
    
  ,
	[userRefURI] ,
	[docRefURI] 

	PRIMARY KEY ( [equivalentPolicy_id] )
)

CREATE TABLE dbo.[equivalentPolicies] 
( 
	[equivalentPolicies_id] int Identity(1,1),
	[] 

	PRIMARY KEY ( [equivalentPolicies_id] )
)

CREATE TABLE dbo.[privacyMark] 
( 
	[privacyMark_id] int Identity(1,1),
	[name] 

        varchar(255),
	[obsolete] bit

	PRIMARY KEY ( [privacyMark_id] )
)

CREATE TABLE dbo.[privacyMarks] 
( 
	[privacyMarks_id] int Identity(1,1),
	[] 

	PRIMARY KEY ( [privacyMarks_id] )
)

CREATE TABLE dbo.[markingData] 
( 
	[markingData_id] int Identity(1,1),
	[] ,
	[phrase] 
    
      Marking Phrase
    
    

        varchar
      

    (256)

  
    
  

	PRIMARY KEY ( [markingData_id] )
)

CREATE TABLE dbo.[securityClassification] 
( 
	[securityClassification_id] int Identity(1,1),
	[]  NULL,
	[]  NULL,
	[]  NULL,
	[name] 
    
      Classification  Name
    
    

        varchar
      

    (256)

  
    
  ,
	[color] 
    
  ,
	[lacv] 
    
      Label and Certificate integer or bit alue
    
    
  ,
	[hierarchy] 
    
      Hierarchy - used for dominance check
    
    
  ,
	[obsolete] bit

	PRIMARY KEY ( [securityClassification_id] )
)

CREATE TABLE dbo.[securityClassifications] 
( 
	[securityClassifications_id] int Identity(1,1),
	[] 

	PRIMARY KEY ( [securityClassifications_id] )
)

CREATE TABLE dbo.[equivalentSecCategoryTag] 
( 
	[equivalentSecCategoryTag_id] int Identity(1,1),
	[policyRef] 
    
      Policy Name
    
    

        varchar
      

    (256)

  
    
  ,
	[tagSetId] 
    
      Object Identifier
    
    

        varchar
      
    
  ,
	[tagType] 
    
      Type of security category
    
    

        varchar
      
      
      
      
      
    
  ,
	[enumType] 
    
      Type of enumerated security category
    
    

        varchar
      
      
    
  ,
	[lacv] 
    
  ,
	[applied] 
    
      When equivalencies can be applied
    
    

        varchar
      
      
      
    
  

	PRIMARY KEY ( [equivalentSecCategoryTag_id] )
)

CREATE TABLE dbo.[tagCategory] 
( 
	[tagCategory_id] int Identity(1,1),
	[]  NULL,
	[]  NULL,
	[]  NULL,
	[]  NULL,
	[]  NULL,
	[name] 

        varchar(255),
	[lacv] 
    
  ,
	[userInput] 
    
      The format of a category value to be entered by the user.
    
    

        varchar
      
      
      
    
  ,
	[requiredClass] 
    
      Classification  Name
    
    

        varchar
      

    (256)

  
    
  ,
	[obsolete] bit

	PRIMARY KEY ( [tagCategory_id] )
)

CREATE TABLE dbo.[qualifier] 
( 
	[qualifier_id] int Identity(1,1),
	[markingQualifier] 
    
      Marking Phrase
    
    

        varchar
      

    (256)

  
    
  ,
	[qualifierCode] 
    

        varchar
      
      
      
    
  

	PRIMARY KEY ( [qualifier_id] )
)

CREATE TABLE dbo.[markingQualifier] 
( 
	[markingQualifier_id] int Identity(1,1),
	[] ,
	[markingCode] 
    
      Location to display a component of the security label
    
    

        varchar
      
      
      
      
      
      
      
      
    
  

	PRIMARY KEY ( [markingQualifier_id] )
)

CREATE TABLE dbo.[securityCategoryTag] 
( 
	[securityCategoryTag_id] int Identity(1,1),
	[]  NULL,
	[]  NULL,
	[name] 

        varchar(255),
	[tagType] 
    
      Type of security category
    
    

        varchar
      
      
      
      
      
    
  ,
	[enumType] 
    
      Type of enumerated security category
    
    

        varchar
      
      
    
  ,
	[tag7Encoding] 
    

        varchar
      
      
    
  ,
	[singleSelection] bit

	PRIMARY KEY ( [securityCategoryTag_id] )
)

CREATE TABLE dbo.[securityCategoryTagSet] 
( 
	[securityCategoryTagSet_id] int Identity(1,1),
	[] ,
	[name] 
    
      Tag Set Name
    
    

        varchar
      

    (256)

  
    
  ,
	[id] 
    
      Object Identifier
    
    

        varchar
      
    
  

	PRIMARY KEY ( [securityCategoryTagSet_id] )
)

CREATE TABLE dbo.[securityCategoryTagSets] 
( 
	[securityCategoryTagSets_id] int Identity(1,1),
	[] 

	PRIMARY KEY ( [securityCategoryTagSets_id] )
)

CREATE TABLE dbo.[defaultSecurityPolicyId] 
( 
	[defaultSecurityPolicyId_id] int Identity(1,1),
	[name] 
    
      Policy Name
    
    

        varchar
      

    (256)

  
    
  ,
	[id] 
    
      Object Identifier
    
    

        varchar
      
    
  

	PRIMARY KEY ( [defaultSecurityPolicyId_id] )
)

CREATE TABLE dbo.[securityPolicyId] 
( 
	[securityPolicyId_id] int Identity(1,1),
	[name] 
    
      Policy Name
    
    

        varchar
      

    (256)

  
    
  ,
	[id] 
    
      Object Identifier
    
    

        varchar
      
    
  

	PRIMARY KEY ( [securityPolicyId_id] )
)

CREATE TABLE dbo.[SPIF] 
( 
	[SPIF_id] int Identity(1,1),
	[]  NULL,
	[] ,
	[]  NULL,
	[] ,
	[]  NULL,
	[]  NULL,
	[]  NULL,
	[]  NULL,
	[schemaVersion] 
    
      Supported versions of the XML SPIF
    
    

        varchar
      
    
  ,
	[version] ,
	[creationDate] 
    
      Tag Set Name
    
    

        varchar
  ,
	[originatorDN] 

        varchar(255),
	[keyIdentifier] 

        varchar(255),
	[privilegeId] 
    
      Object Identifier
    
    

        varchar
      
    
  ,
	[rbacId] 
    
      Object Identifier
    
    

        varchar
      
    
  ,
	[userRefURI] ,
	[docRefURI] 

	PRIMARY KEY ( [SPIF_id] )
)


    
      Security Policy Information File
    
    
      
        
        
        
        
        
        
        
        
      
      
      
      
      
      
      
      
      
      
      
    
    
      
      
    
    
      
      
    
    ALTER TABLE dbo.
	ADD CONSTRAINT [FK__] FOREIGN KEY 
	( 
		[]
	) 
	REFERENCES dbo.
	( 
		[]
	) 


    ALTER TABLE dbo.
	ADD CONSTRAINT [FK__] FOREIGN KEY 
	( 
		[]
	) 
	REFERENCES dbo.
	( 
		[]
	) 


    
      
      
    
    
      
      
    
    
      
      
    
    ALTER TABLE dbo.
	ADD CONSTRAINT [FK__] FOREIGN KEY 
	( 
		[]
	) 
	REFERENCES dbo.
	( 
		[]
	) 


    ALTER TABLE dbo.
	ADD CONSTRAINT [FK__] FOREIGN KEY 
	( 
		[]
	) 
	REFERENCES dbo.
	( 
		[]
	) 


    
      
      
    
    ALTER TABLE dbo.
	ADD CONSTRAINT [FK__] FOREIGN KEY 
	( 
		[]
	) 
	REFERENCES dbo.
	( 
		[]
	) 


    ALTER TABLE dbo.
	ADD CONSTRAINT [FK__] FOREIGN KEY 
	( 
		[]
	) 
	REFERENCES dbo.
	( 
		[]
	) 


    ALTER TABLE dbo.
	ADD CONSTRAINT [FK__] FOREIGN KEY 
	( 
		[]
	) 
	REFERENCES dbo.
	( 
		[]
	) 


  