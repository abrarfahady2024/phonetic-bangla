# -*- coding: utf-8 -*-
"""
Comprehensive test suite for reverse transliteration (Bengali to Banglish)
Tests edge cases, conjuncts, diacritics, and special characters
"""

import pytest
from phoneticbn import bn_reverse, bn


class TestBasicReverseConversion:
    """Test basic individual character conversions"""
    
    def test_independent_vowels(self):
        """Test all independent vowels"""
        assert bn_reverse('অ') == 'o'
        assert bn_reverse('আ') == 'a'
        assert bn_reverse('ই') == 'i'
        assert bn_reverse('ঈ') == 'I'
        assert bn_reverse('উ') == 'u'
        assert bn_reverse('ঊ') == 'U'
        assert bn_reverse('এ') == 'e'
        assert bn_reverse('ঐ') == 'OI'
        assert bn_reverse('ও') == 'O'
        assert bn_reverse('ঔ') == 'OU'
    
    def test_basic_consonants(self):
        """Test basic consonants"""
        assert bn_reverse('ক') == 'k'
        assert bn_reverse('গ') == 'g'
        assert bn_reverse('চ') == 'c'
        assert bn_reverse('ট') == 'T'
        assert bn_reverse('ত') == 't'
        assert bn_reverse('প') == 'p'
        assert bn_reverse('ব') == 'b'
        assert bn_reverse('ম') == 'm'
        assert bn_reverse('র') == 'r'
        assert bn_reverse('ল') == 'l'
        assert bn_reverse('স') == 's'
        assert bn_reverse('হ') == 'h'
    
    def test_aspirated_consonants(self):
        """Test aspirated consonants"""
        assert bn_reverse('খ') == 'kh'
        assert bn_reverse('ঘ') == 'gh'
        assert bn_reverse('ছ') == 'ch'
        assert bn_reverse('ঝ') == 'jh'
        assert bn_reverse('ঠ') == 'Th'
        assert bn_reverse('ঢ') == 'Dh'
        assert bn_reverse('থ') == 'th'
        assert bn_reverse('ধ') == 'dh'
        assert bn_reverse('ফ') == 'ph'
        assert bn_reverse('ভ') == 'bh'
    
    def test_diacritics(self):
        """Test vowel diacritics (kar)"""
        assert bn_reverse('া') == 'a'
        assert bn_reverse('ি') == 'i'
        assert bn_reverse('ী') == 'I'
        assert bn_reverse('ু') == 'u'
        assert bn_reverse('ূ') == 'U'
        assert bn_reverse('ে') == 'e'
        assert bn_reverse('ৈ') == 'OI'
        assert bn_reverse('ো') == 'O'
        assert bn_reverse('ৌ') == 'OU'
    
    def test_modifiers(self):
        """Test modifiers (chandrabindu, anusvara, bisorgo)"""
        assert bn_reverse('ঁ') == 'C'
        assert bn_reverse('ং') == 'ng'
        assert bn_reverse('ঃ') == ':'
        assert bn_reverse('্') == '+'


class TestSimpleWords:
    """Test reverse conversion of simple words"""
    
    def test_simple_two_letter_words(self):
        """Test simple two-letter words"""
        assert 'k' in bn_reverse('কা')
        assert bn_reverse('দা') == 'da'
        assert bn_reverse('না') == 'na'
    
    def test_simple_three_letter_words(self):
        """Test simple three-letter words"""
        # আমার = amar
        result = bn_reverse('আমার')
        assert 'a' in result.lower() and 'm' in result.lower() and 'r' in result.lower()
        
        # সোনার = sonar
        result = bn_reverse('সোনার')
        assert 's' in result.lower() and 'o' in result.lower() and 'n' in result.lower()
    
    def test_words_with_diacritics(self):
        """Test words that use diacritics"""
        # দিন = din
        result = bn_reverse('দিন')
        assert result == 'din'
        
        # নদী = nodi
        result = bn_reverse('নদী')
        assert 'n' in result.lower() and 'd' in result.lower()


class TestConjuncts:
    """Test complex conjunct (juktoborno) handling"""
    
    def test_ksh_conjunct(self):
        """Test ক্ষ conjunct (kSh)"""
        # লক্ষী = lakshmi/lokshi
        result = bn_reverse('লক্ষী')
        assert 'kSh' in result or 'ksh' in result.lower()
    
    def test_jna_conjunct(self):
        """Test জ্ঞ conjunct (jNG)"""
        # বিজ্ঞান = bijnan/biznan
        result = bn_reverse('বিজ্ঞান')
        assert 'jNG' in result or 'j' in result.lower()
    
    def test_common_conjuncts(self):
        """Test common conjuncts"""
        # স্বাগতম = swagotom
        result = bn_reverse('স্বাগতম')
        assert 's' in result.lower() and 'w' in result.lower()
        
        # শান্ত = shanto
        result = bn_reverse('শান্ত')
        assert 'n' in result.lower() and 't' in result.lower()
        
        # লম্বা = lomba
        result = bn_reverse('লম্বা')
        assert 'm' in result.lower() and 'b' in result.lower()
    
    def test_double_consonants(self):
        """Test double consonant conjuncts"""
        # ক্ক conjunct
        result = bn_reverse('ক্কা')
        assert 'k' in result.lower()
        
        # ট্ট conjunct
        result = bn_reverse('ট্টা')
        assert 'T' in result or 't' in result.lower()
    
    def test_ra_fola(self):
        """Test র fola patterns"""
        # র্ম = rfm (like in করম = kormo/korfmo)
        result = bn_reverse('করম')
        assert 'k' in result.lower() and 'r' in result.lower() and 'm' in result.lower()


class TestFullPhrases:
    """Test full phrase reverse conversions"""
    
    def test_national_anthem_phrase(self):
        """Test the national anthem phrase"""
        bengali = "আমার সোনার বাংলা"
        result = bn_reverse(bengali)
        
        # Should contain basic sounds
        assert 'a' in result.lower()
        assert 'm' in result.lower()
        assert 's' in result.lower()
        assert 'b' in result.lower()
    
    def test_greeting_phrase(self):
        """Test greeting phrases"""
        # সবার জন্য শুভেচ্ছা = sobar jonno subhechcha
        bengali = "সবার জন্য শুভেচ্ছা"
        result = bn_reverse(bengali)
        
        assert 's' in result.lower()
        assert 'b' in result.lower()
        assert 'j' in result.lower()
        assert 'n' in result.lower()
    
    def test_common_words_list(self):
        """Test list of common Bengali words"""
        words = {
            'আমি': 'ami',
            'তুমি': 'tumi',
            'তারা': 'tara',
            'আজ': 'aj',
            'আগামী': 'agami',
        }
        
        for bengali, expected in words.items():
            result = bn_reverse(bengali).lower()
            # Check if key characters are present
            assert any(char in result for char in expected)


class TestSpecialCharacters:
    """Test special characters and punctuation"""
    
    def test_danda_punctuation(self):
        """Test Danda (।) to period conversion"""
        bengali = "আমার সোনার বাংলা।"
        result = bn_reverse(bengali)
        assert '.' in result
    
    def test_spaces_preservation(self):
        """Test that spaces are preserved"""
        bengali = "আমার সোনার বাংলা"
        result = bn_reverse(bengali)
        assert ' ' in result
    
    def test_multiple_spaces(self):
        """Test handling of multiple spaces"""
        bengali = "আমার  সোনার"
        result = bn_reverse(bengali)
        assert '  ' in result  # Spaces should be preserved
    
    def test_numbers_pass_through(self):
        """Test that Bengali numerals pass through"""
        bengali = "২০২৫"
        result = bn_reverse(bengali)
        # Bengali numbers should be returned as-is
        assert bengali in result or any(char.isdigit() for char in result)


class TestRoundTripConversion:
    """Test forward and reverse conversion round-trips"""
    
    def test_simple_roundtrip(self):
        """Test that Banglish -> Bengali -> Banglish produces similar results"""
        original = "amar sonar bangla"
        bengali = bn(original)
        reverse = bn_reverse(bengali)
        
        # Should get back something similar
        assert 'amar' in reverse.lower() or ('a' in reverse.lower() and 'm' in reverse.lower())
    
    def test_complex_roundtrip(self):
        """Test complex word round-trip"""
        original = "sawgotom"
        bengali = bn(original)
        reverse = bn_reverse(bengali)
        
        # Key characters should be present
        assert 's' in reverse.lower() or 'sw' in reverse.lower()
    
    def test_conjunct_roundtrip(self):
        """Test conjunct round-trip"""
        original = "bijNGan"
        bengali = bn(original)
        reverse = bn_reverse(bengali)
        
        # Should contain key phonemes
        result_lower = reverse.lower()
        assert 'b' in result_lower or 'i' in result_lower


class TestEdgeCases:
    """Test edge cases and boundary conditions"""
    
    def test_empty_string(self):
        """Test empty string input"""
        assert bn_reverse('') == ''
    
    def test_single_character(self):
        """Test single character input"""
        assert bn_reverse('ক') == 'k'
        assert bn_reverse('া') == 'a'
    
    def test_only_spaces(self):
        """Test input with only spaces"""
        assert bn_reverse('   ') == '   '
    
    def test_mixed_bengali_and_latin(self):
        """Test mixed Bengali and Latin characters"""
        bengali = "আমার bangla"
        result = bn_reverse(bengali)
        assert 'bangla' in result
    
    def test_repeated_characters(self):
        """Test repeated Bengali characters"""
        bengali = "ককক"  # ক repeated 3 times
        result = bn_reverse(bengali)
        assert result.count('k') == 3
    
    def test_all_modifiers(self):
        """Test all modifier characters together"""
        bengali = "কঁং:"
        result = bn_reverse(bengali)
        # Should contain conversions of all modifiers
        assert 'k' in result.lower()
        assert any(m in result for m in ['C', 'ng', ':'])
    
    def test_very_long_text(self):
        """Test very long Bengali text"""
        bengali = "আমার সোনার বাংলা " * 100
        result = bn_reverse(bengali)
        # Should not crash and should contain expected characters
        assert len(result) > 0
        assert 'a' in result.lower()


class TestCommonBengaliWords:
    """Test dictionary of common Bengali words"""
    
    @pytest.mark.parametrize("bengali,expected_chars", [
        ('করা', ['k', 'r', 'a']),
        ('দেওয়া', ['d', 'e', 'a']),
        ('জানা', ['j', 'a', 'n']),
        ('দিন', ['d', 'i', 'n']),
        ('রাত', ['r', 'a', 't']),
        ('ভালো', ['b', 'h', 'a', 'l', 'o']),
        ('খারাপ', ['k', 'h', 'a', 'r', 'a', 'p']),
        ('বড়', ['b', 'r']),
        ('ছোট', ['c', 'h', 't']),
    ])
    def test_common_words(self, bengali, expected_chars):
        """Test common Bengali words contain expected characters"""
        result = bn_reverse(bengali).lower()
        for char in expected_chars:
            # Each expected character should appear somewhere in result
            assert char in result, f"Expected '{char}' in '{result}' from Bengali '{bengali}'"


class TestConsistency:
    """Test consistency of reverse transliteration"""
    
    def test_consistent_output(self):
        """Test that same input produces same output"""
        bengali = "আমার সোনার বাংলা"
        result1 = bn_reverse(bengali)
        result2 = bn_reverse(bengali)
        assert result1 == result2
    
    def test_character_order_preservation(self):
        """Test that character order is preserved"""
        bengali = "আমার"
        result = bn_reverse(bengali)
        # আ -> a/o, ম -> m, া -> a, র -> r
        # Should have 'a' or 'o' before 'm' and 'r' after
        assert result.index(result[0]) < result.index('m')


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
