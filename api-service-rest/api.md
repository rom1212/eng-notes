# Considerations
* Pagination
* ID

# CRUD API
## Update API
* probably the most complex API
* Difficult cases
  * null value vs real value
  * clean up a value vs no-update
    * How to differentiate that users want to clean up a value, or will not update that value
    * when the API doesn't specify a value, i.e. it is null (e.g. java null pointer), we don't update it.
    * when the API specifies an empty value, e.g. empty string "", empty list - a list with size 0, we clean it up.
    * with Google proto buffer, we can check with has_value() to see whether we no-update or clean up.
  * How to clean up a value
