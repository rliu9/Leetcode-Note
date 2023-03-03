# Why scan QR code login is not safe?


## Fake QR codes
Attackers can use a variety of means to create fake QR codes that look identical to normal QR codes but direct users to a fake login page to steal sensitive information such as account numbers and passwords.

## Man-in-the-middle attack
- The attacker obtains the QR code that the user scans during normal login through various means and forges it into their own QR code.
- After the user scans the forged QR code, their login information is sent to the attacker's server, allowing the attacker to obtain sensitive information.
- The attacker passes the forged QR code to the server, masquerading as a successful user login and starting to perform various operations.
- The user continues to use this forged login session without realizing it, allowing the attacker to control their account and carry out malicious operations.
