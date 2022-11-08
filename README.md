# vertical Search Engine

* Search Engine:
This is the power house of an information retrieval system. A search engine is a system designed to carry out searches based on the query passed by searching through the database in a systematic way. It then presents the results matching the query in a ranked order. A search engine consists of three main components;

* Web crawler: 
A web crawler often shortened to a crawler is an internet bot that is operated by a search engine and is responsible for systematically browsing through the web to get new data or update existing data in the data base. Which will be passed to the indexer. 

* Preprocessing:  
The data stored in the database needs to go through preprocessing before being passed to the indexer, this plays an important role in information retrieval so our search engine can extract relevant information matching the query, the steps of preprocessing involve Tokenization, stop word removal, remove punctuation, remove whitespaces, Lemmatization and Stemming for the text documents Keywords.

* Indexer: 
This is the component of the search engine that performs the indexing on the processed data. Indexing is the process of mapping each term in the database to their respective document that contains them and stores them as an inverted index which will be used by the query processor for retrieval.

* Query Processor: 
The query processor is the subcomponent of the search engine that processes user query and retrieves its matching documents. A user or an applications program, interacts with the query processor and the query processor, in turn interacts with the storage engine (Database). Essentially, the query processor receives an instruction or instructions, chooses a plan for executing the instructions and carries out the plan.
