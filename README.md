# About

This application will take in a list of email addresses (separated by new lines) and outputs a list of domains with their respective number of occurrences in the given file.


# Usage

Linux:

python ./count_unique_domains.py <filename>

Windows:

python count_unique_domains.py <filename>

Note: Python 3 is required


# Design Decisions

Encoding:

I have made the decision that all valid lines in a given input file must be UTF-8 encoded to be considered valid. 


Email Validation:

In the interest of time, I have decided to use the following rules to validate email addresses/domains (Derived in part from https://en.wikipedia.org/wiki/Email_address#Syntax):

local-part can contain:
- uppercase and lowercase latin letters (a-z, A-Z)
- all international UTF-8 characters above U+007F
- digits 0-9
- special characters !#$%&'*+-/=?^_`{|}~
- dots (.), but not as first or last letter
- up to 64 characters total (1 character minimum)

domain can contain:
- uppercase and lowercase latin letters (a-z, A-Z)
- all international UTF-8 characters above U+007F
- digits 0-9, provided that the highest level domain is not all digits (e.g. example.111 is invalid)
- dots (.), but not as first or last letter, nor can they appear consecutively
- hyphens (-), but not as first or last character
- up to 255 characters (63 characters per label, 1 character minimum)

entire email:
- cannot be more than 254 characters total


Other:

I decided to use regular expressions to validate emails, as it is the most precise and efficient way to do so. 

I decided to use a dict to keep track of the domains because it is backed by a hashtable and has O(1) lookups and inserts.


Testing:

I've also created test_count_unique_domains.py, which has unit tests for functions in count_unique_domains.py.

Run them with:

Linux:

python ./test_count_unique_domains.py

Windows:

python test_count_unique_domains.py

Note: Python 3 is required