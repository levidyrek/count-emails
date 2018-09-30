#!/usr/bin/env python

import sys
import re


def is_valid_local_part(text):
    """
    Validates local-part of an email address. See readme for restrictions.
    """
    if 1 > len(text) or len(text) > 64:
        return False
    return re.match(r'^[a-zA-Z\u007F-\uFFFF0-9!#$%&\'*+\-=?\^_`{|}~]+([.]+[a-zA-Z\u007F-\uFFFF0-9!#$%&\'*+\-=?\^_`{|}~]+)*$', text)


def is_valid_domain_label(text):
    """
    Validates labels of a domain. See readme for restrictions.
    """
    if 1 > len(text) or len(text) > 63:
        return False
    return re.match(r'^[a-zA-Z\u007F-\uFFFF0-9]+(\-+[a-zA-Z\u007F-\uFFFF0-9]+)*$', text)


def is_valid_domain(text):
    """
    Checks domain as a whole, then breaks it into parts and validates each separately.
    """
    if len(text) > 255:
        return False

    labels = text.split('.')
    for label in labels:
        if not is_valid_domain_label(label):
            return False

    # Just need to check that the last segment is not all numerical
    return re.search(r'[a-zA-Z\u007F-\uFFFF]', labels[len(labels) - 1])


def is_valid_email(email):
    """
    Checks email as a whole, then breaks it into local-part and domain and validates them separately.
    """
    if len(email) > 254:
        return False

    parts = email.split('@')
    if len(parts) != 2:
        return False

    return is_valid_local_part(parts[0]) and is_valid_domain(parts[1])


def count_unique_domains(lines):
    """
    Takes in a list of strings and prints out valid domains with their occurrences.
    """
    domains = {}

    for line in lines:
        if is_valid_email(line):
            # Add/increment domain's count in dict 
            domain = line.split('@')[1].lower()
            if domain in domains:
                domains[domain] += 1
            else:
                domains[domain] = 1

    return domains
    

def main():
    # First, check that filename is given as an argument.
    try:
        filename = sys.argv[1]
    except IndexError:
        print("Must provide file. See readme for usage.")
        sys.exit(1)

    try:
        with open(filename, mode='rb') as file:
            lines = []
            for line in file:
                try:
                    # Try to decode as utf-8 and strip off newline characters
                    lines.append(line.decode('utf-8').strip('\r\n'))
                except UnicodeDecodeError as e:
                    # Non-utf-8 lines are treated as invalid
                    pass

            domains = count_unique_domains(lines)

            # Print domains with respective counts.
            for domain, count in domains.items():
                print(str(count) + ': ' + domain)

    except OSError:
        print("File could not be read.")
        sys.exit(1)


if __name__ == '__main__':
    main()