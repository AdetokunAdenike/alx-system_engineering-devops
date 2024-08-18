### Postmortem: Apache 500 Internal Server Error Debugging and Resolution

**Issue Summary:**

- **Duration of the Outage:** The issue was present from 07:00 GMT to 07:08 GMT on March 24, 2017.
- **Impact:** Apache server was returning a 500 Internal Server Error, which resulted in users being unable to access the website hosted on the server. Approximately 100% of users trying to access the site during this period were affected.
- **Root Cause:** The error was caused by a typo in a PHP file where the PHP interpreter was incorrectly referred to as "phpp" instead of "php".

**Timeline:**

- **07:00 GMT:** The issue was detected when an engineer noticed that the website was down and returned a 500 Internal Server Error.
- **07:01 GMT:** The issue was initially detected through the curl command, which confirmed the error response from the server.
- **07:02 GMT:** `strace` was used to attach to the running Apache process to diagnose the problem. This revealed errors related to the PHP interpreter.
- **07:04 GMT:** Investigations showed that the problem was a typo in a PHP script.
- **07:05 GMT:** The erroneous script was identified, and the incorrect interpreter reference was corrected from "phpp" to "php".
- **07:06 GMT:** The change was made, and the configuration was reloaded.
- **07:08 GMT:** The incident was resolved, and a successful response (HTTP 200 OK) was confirmed using curl.

**Root Cause and Resolution:**

- **Root Cause Detail:** The root cause of the 500 Internal Server Error was a typo in the PHP file configuration. The script referenced the PHP interpreter as "phpp" instead of "php," which caused the server to fail when processing PHP scripts.
- **Resolution Detail:** The issue was fixed by correcting the typo in the PHP configuration file. The script was updated to use the correct PHP interpreter. Following this, Puppet was used to automate the fix. The Puppet code ensured that the correct configuration was applied and verified.

**Corrective and Preventative Measures:**

- **Improvements/Fixes:**
  - Implement a validation step to catch such configuration errors before deployment.
  - Increase the coverage of automated tests to include configuration checks.
  - Enhance monitoring to catch PHP errors and misconfigurations more effectively.
- **Tasks to Address the Issue:**
  1. **Patch the PHP Configuration:**
     - Update the PHP script to use the correct "php" interpreter instead of "phpp."
  2. **Automate the Fix with Puppet:**
     - Create and apply the Puppet manifest (`0-strace_is_your_friend.pp`) to automate the configuration correction.
     - Ensure Puppet code validates the PHP interpreter path and corrects any discrepancies.
  3. **Enhance Monitoring:**
     - Add monitoring to detect and alert on configuration issues with PHP files.
     - Implement logs and alerts for HTTP 500 errors specifically caused by PHP configuration issues.
  4. **Update Documentation:**
     - Document the issue and resolution steps to prevent similar issues in the future.
     - Include guidelines for proper PHP configuration and validation checks.

This postmortem outlines the steps taken to resolve the Apache 500 error, from detection to resolution, and provides a plan for preventing similar issues in the future.
