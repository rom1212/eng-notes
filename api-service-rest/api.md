# Considerations
* Pagination
* ID

# Default value
* the value is automatically filled.
* the value can change when system change default value

# CRUD API
## Update API
* probably the most complex API
* Difficult cases
  * null value vs no-care-value
    * Always clean up for different exclusive cases, e.g. if we have a column called "relationship", which doesn't matter
      if it is there is only one value in "attrs", otherwise,  "relationship" has a given value.
    * In this case, if we don't specify a value for "relationship" when there is only one value in "attrs", it could become a
      meaningless/wrong value when the previous "relationship" has a value for two values in "attrs". Since we don't clean up or
      specify a value for it when we update for only one value in "attrs". However, if all the "relationship" with more than one
      values on "attrs" works for only one value in "attrs", that might be fine to not update "attrs" for only one value in
      "attrs".
  * clean up a value vs no-update
    * How to differentiate that users want to clean up a value, or will not update that value
    * when the API doesn't specify a value, i.e. it is null (e.g. java null pointer), we don't update it.
    * when the API specifies an empty value, e.g. empty string "", empty list - a list with size 0, we clean it up.
    * with Google proto buffer, we can check with has_value() to see whether we no-update or clean up.
  * How to clean up a value
