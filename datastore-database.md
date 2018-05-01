# SQL Database
## Schema Design
### status
* It is usually an enum, but better not put enum in the database because we will keep adding new enum values. We can put enum in the code as enum, and use string in database. some status values can be
  * Deleted/Inactive
  * Ready/InProgress
  * InUse
* status can be used for deleting, in use, etc.

# Test and Benchmark
* https://github.com/brianfrankcooper/YCSB
* https://www.datastax.com/wp-content/themes/datastax-2014-08/files/NoSQL_Benchmarks_EndPoint.pdf
