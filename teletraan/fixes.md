# Potential Bugs
* Failed deployment could become SUCCEEDING after some time.
* PRE_DOWNLOAD is actually executing the PRE_DOWNLOAD of a previous deployment.
* table environs.last_update is not updated when new deployments is created for it. Maybe this is not considered as an update.

#  formatting
* AutoPromoter.java: String newDeployId, wrong indentation and new line
