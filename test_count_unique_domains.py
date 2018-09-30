#!/usr/bin/env python

from count_unique_domains import is_valid_local_part, is_valid_domain_label, is_valid_domain, is_valid_email, count_unique_domains
import unittest


class TestLocalPartValidation(unittest.TestCase):
    """
    Tests is_valid_local_part() based on restrictions in README.md
    """

    def test_valid(self):
        self.assertTrue(is_valid_local_part('aZ102.9!#$%.&\'*+-.=?^_`{|.}~€ƒŒϬ'))

    def test_illegal_chars(self):
        self.assertFalse(is_valid_local_part('abc@,�'))

    def test_empty(self):
        self.assertFalse(is_valid_local_part(''))

    def test_min_length(self):
        self.assertTrue(is_valid_local_part('a'))

    def test_max_length(self):
        self.assertTrue(is_valid_local_part('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'))

    def test_too_long(self):
        self.assertFalse(is_valid_local_part('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab'))

    def test_dot_first(self):
        self.assertFalse(is_valid_local_part('.a'))

    def test_dot_last(self):
        self.assertFalse(is_valid_local_part('a.'))


class TestDomainLabelValidation(unittest.TestCase):
    """
    Tests is_valid_domain_label() based on restrictions in README.md
    """

    def test_valid(self):
        self.assertTrue(is_valid_domain_label('aZ1029--€ƒŒϬ'))

    def test_illegal_chars(self):
        self.assertFalse(is_valid_domain_label('abc@,�'))

    def test_empty(self):
        self.assertFalse(is_valid_domain_label(''))

    def test_min_length(self):
        self.assertTrue(is_valid_domain_label('a'))

    def test_max_length(self):
        self.assertTrue(is_valid_domain_label('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'))

    def test_too_long(self):
        self.assertFalse(is_valid_domain_label('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab'))

    def test_hyphen_first(self):
        self.assertFalse(is_valid_domain_label('-a'))

    def test_hyphen_last(self):
        self.assertFalse(is_valid_domain_label('a-'))


class TestDomainValidation(unittest.TestCase):
    """
    Tests is_valid_domain() based on restrictions in README.md
    """

    def test_valid(self):
        self.assertTrue(is_valid_domain('aZ1029--€ƒŒϬ.1111.a.com'))

    def test_empty(self):
        self.assertFalse(is_valid_domain(''))

    def test_min_length(self):
        self.assertTrue(is_valid_domain('a'))

    def test_max_length(self):
        self.assertTrue(is_valid_domain('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.'
                                        'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.'
                                        'ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc.'
                                        'ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd'))

    def test_too_long(self):
        self.assertFalse(is_valid_domain('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.'
                                         'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.'
                                         'ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc.'
                                         'ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd.e'))

    def test_all_numeric_tld(self):
        self.assertFalse(is_valid_domain('test.1234'))

    def test_consecutive_dots(self):
        self.assertFalse(is_valid_domain('aaa..bbb'))


class TestEmailValidation(unittest.TestCase):
    """
    Tests is_valid_email() based on restrictions in README.md
    """

    def test_valid(self):
        self.assertTrue(is_valid_email('aZ102.9!#$%.&\'*+-.=?^_`{|.}~€ƒŒϬ@aZ1029--€ƒŒϬ.1111.a.com'))

    def test_multiple_at_symbol(self):
        self.assertFalse(is_valid_email('a@awdij@awdohu'))

    def test_no_at_symbol(self):
        self.assertFalse(is_valid_email('test'))

    def test_at_symbol_first(self):
        self.assertFalse(is_valid_email('@test'))

    def test_at_symbol_last(self):
        self.assertFalse(is_valid_email('test@'))

    def test_max_length(self):
        self.assertTrue(is_valid_email('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa@'
                                       'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.'
                                       'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.'
                                       'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'))

    def test_too_long(self):
        self.assertFalse(is_valid_email('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa@'
                                       'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.'
                                       'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.'
                                       'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab'))


class TestCountUniqueDomains(unittest.TestCase):
    """
    Tests count_unique_domains()
    """

    def test_case_difference(self):
        data = ['test@abc.com', 'test2@ABC.cOm']
        self.assertEqual(count_unique_domains(data)['abc.com'], 2)


if __name__ == '__main__':
    unittest.main()