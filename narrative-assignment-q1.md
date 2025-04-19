Comments, Feedback and Unclear requirements:
1. Will there be any data transformation, validation or schema alignment while migrating the data from existing DB to AWS S3?
2. Data volume is not clearly mentioned for each table. Detailed distribution of data sizes across the tables would help in writing performance related scenarios.
3. What is the CTA for failed uploads or a failure in fetching the data from DB to AWS S3? 
4. Can there be a chance of leak while migration if a step fails or there are retry systems present?
5. What kind of data is stored in the source, are there privacy concerns? Will there be some data encrypted?
6. What kind of job is being scheduled on the deployment day for the first 300 tables? 
7. How will the jobs be monitored? Daily and monthly.
8. Test environment not defined to validate monthly deployments?
9. The methods defined are not clear and do not clarify how the tables are categorized into these methods. What are the criteria?
10. QA will need some samples from each category to understand each method thoroughly.
11. CDC3 and CDC7 are not exporting all the data, hence QA will need a document of the records which needs to be exported to validate the migration.
12. What is the comparison record for CDC7 as the system will only fetch the changed records. So, a validating source is missing.
13. Are source and target schemas identical? What is the CTA if schema changes in the source DB (e.g. addition or removal of column)?
14. How will the test data be simulated for full-migration, partial-migration and selective-transfer?
15. What checkpoints need to be set up in case of job failure or if data gets corrupted on AWS S3?
16. What is defined as “right data”? The validations should be on record count, record type, record value or any other business rule?
17. Does “correct amount” imply row by row and column by column match?
