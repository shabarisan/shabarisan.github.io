build a file-based key-value data store that supports the basic crd (create, read, and delete) operations. this data store is meant to be used as a local storage for one single process on one laptop. the data store must be exposed as a library to clients that can instantiate a class and work with the data store. 
the data store will support the following functional requirements.
 1. it can be initialized using an optional file path. if one is not provided, it will reliably create itself in a reasonable location on the laptop.
 2. a new key-value pair can be added to the data store using the create operation. the key is always a string - capped at 32chars. the value is always a json object - capped at 16kb.
 3. if create is invoked for an existing key, an appropriate error must be returned.
 4. a read operation on a key can be performed by providing the key, and receiving the value in response, as a json object. 
5. a delete operation can be performed by providing the key. 
6. every key supports setting a time-to-live property when it is created. this property is optional. if provided, it will be evaluated as an integer defining the number of seconds the key must be retained in the data store. once the time-to-live for a key has expired, the key will no longer be available for read or delete operations. 
7. appropriate error responses must always be returned to a client if it uses the data store in unexpected ways or breaches any limits. 
the data store will also support the following non-functional requirements. 
1. the size of the file storing data must never exceed 1gb.
 2. more than one client process cannot be allowed to use the same file as a data store at any given time.
 3. a client process is allowed to access the data store using multiple threads, if it desires to. the data store must therefore be thread-safe. 
4. the client will bear as little memory costs as possible to use this data store, while deriving maximum performance with respect to response times for accessing the data store.





















