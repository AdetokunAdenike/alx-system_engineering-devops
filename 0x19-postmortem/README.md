# Issue Summary

## Postmortem: Apache 500 Internal Server Error Debugging and Resolution

**Issue Summary:**

- **Duration of the Outage:** March 24, 2017, from 07:00 GMT to 07:08 GMT.
- **Impact:** The Apache server returned a 500 Internal Server Error, preventing users from accessing the website. This affected 100% of users attempting to visit the site during the outage.
- **Root Cause:** The error was caused by a typo in a PHP file where the PHP interpreter was incorrectly referred to as "phpp" instead of "php."

# Timeline:

- **07:00 GMT:** The issue was detected when I observed that the website was returning a 500 Internal Server Error.
- **07:01 GMT:** I used `curl` to confirm the error response from the server.
- **07:02 GMT:** I employed `strace` to trace the running Apache process and diagnose the issue, revealing errors related to the PHP interpreter.
- **07:04 GMT:** Investigation pointed to a typo in the PHP configuration file.
- **07:05 GMT:** Corrected the typo from "phpp" to "php" in the PHP file.
- **07:06 GMT:** Applied the fix and reloaded the server configuration.
- **07:08 GMT:** Verified resolution by running `curl` to confirm a successful response (HTTP 200 OK).

# Root Cause and Resolution:

- **Root Cause Detail:** The 500 Internal Server Error was due to a typo in the PHP file configuration, where "phpp" was used instead of "php," leading to PHP script processing failures.
- **Resolution Detail:** I corrected the typo in the PHP file, updating the reference from "phpp" to "php." The fix was automated using Puppet to ensure proper configuration deployment and verification.

---

# Corrective and Preventative Measures:

## Improvements/Fixes:

- Implement a validation step to catch configuration errors before deployment.
- Increase automated test coverage to include configuration checks.
- Enhance monitoring to detect PHP configuration errors and misconfigurations more effectively.

## Tasks to Address the Issue:

1. **Patch the PHP Configuration:**
   - Update the PHP file to use "php" instead of "phpp."
2. **Automate the Fix with Puppet:**
   - Develop and apply the Puppet manifest (`0-strace_is_your_friend.pp`) to automate the correction of PHP interpreter paths.
   - Ensure Puppet validates the PHP interpreter path to prevent future discrepancies.
3. **Enhance Monitoring:**
   - Add monitoring and alerts for PHP configuration issues and HTTP 500 errors related to PHP.
4. **Update Documentation:**
   - Document the issue and the resolution steps.
   - Provide guidelines for validating PHP configurations to avoid similar issues.
