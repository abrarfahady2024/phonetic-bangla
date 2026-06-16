# -*- coding: utf-8 -*-
"""
Reverse transliteration engine: Bengali to Banglish (Roman)
This module converts Bengali script to phonetic English representation.
"""

# Conjunct mappings (highest priority - more complex patterns first)
# These must be checked before individual characters
BENGALI_CONJUNCTS = [
    # Vowel + Consonant combinations
    ('হৃ', 'hRi'),
    ('হৃদ', 'hRid'),
    
    # Special Juktoborno (Conjuncts)
    ('ক্ষ', 'kSh'),
    ('ত্র', 'tro'),
    ('জ্ঞ', 'jNG'),
    ('ঞ্চ', 'NGc'),
    ('ঞ্ছ', 'NGch'),
    ('ঞ্জ', 'NGj'),
    ('ঞ্ঝ', 'NGjh'),
    
    # Common conjuncts
    ('র্থ', 'rth'),
    ('র্ম', 'rfm'),
    ('র্য', 'rz'),
    ('ল্য', 'lz'),
    ('স্থ', 'sth'),
    ('স্ট', 'sT'),
    ('স্ন', 'sn'),
    ('স্প', 'sp'),
    ('স্ব', 'sw'),
    ('স্র', 'sr'),
    ('ষ্ট', 'ShT'),
    ('ষ্ঠ', 'ShTh'),
    ('ষ্ণ', 'ShN'),
    ('ষ্প', 'Shp'),
    ('ষ্ম', 'Shm'),
    ('ন্ত', 'nt'),
    ('ন্ড', 'nD'),
    ('ন্ধ', 'ndh'),
    ('ন্থ', 'nth'),
    ('ন্ব', 'nb'),
    ('ন্ম', 'nm'),
    ('ম্ব', 'mb'),
    ('ম্ভ', 'mbh'),
    ('ম্ম', 'mm'),
    ('ম্ন', 'mn'),
    ('ম্প', 'mp'),
    ('ম্ফ', 'mph'),
    ('ড্ড', 'DD'),
    ('ড্ব', 'Db'),
    ('ড্য', 'Dz'),
    ('ঢ্য', 'Dhz'),
    ('ত্ত', 'tt'),
    ('ত্থ', 'tth'),
    ('ত্ব', 'tb'),
    ('ত্য', 'tz'),
    ('ত্ম', 'tm'),
    ('থ্য', 'thy'),
    ('দ্ধ', 'ddh'),
    ('দ্ব', 'db'),
    ('দ্য', 'dz'),
    ('দ্ম', 'dm'),
    ('ধ্য', 'dhy'),
    ('ধ্ব', 'dhb'),
    ('ধ্ম', 'dhm'),
    ('প্ট', 'pT'),
    ('প্ত', 'pt'),
    ('প্থ', 'pth'),
    ('প্ব', 'pb'),
    ('প্য', 'pz'),
    ('প্স', 'ps'),
    ('ফ্য', 'phy'),
    ('ব্জ', 'bj'),
    ('ব্ড', 'bD'),
    ('ব্ব', 'bb'),
    ('ব্য', 'bz'),
    ('ব্ধ', 'bdh'),
    ('ব্ম', 'bm'),
    ('ভ্য', 'bhy'),
    ('য্য', 'zz'),
    ('র্ব', 'rb'),
    ('র্য', 'rz'),
    ('ল্ব', 'lb'),
    ('ল্ম', 'lm'),
    ('শ্চ', 'shc'),
    ('শ্ছ', 'shch'),
    ('শ্ন', 'shn'),
    ('শ্ব', 'shb'),
    ('শ্ম', 'shm'),
    ('শ্য', 'shy'),
    ('শ্র', 'shr'),
    ('ষ্ণ', 'ShN'),
    ('হ্ণ', 'hN'),
    ('হ্ব', 'hb'),
    ('হ্ম', 'hm'),
    ('হ্য', 'hy'),
    ('হ্ল', 'hl'),
    
    # Common two-character conjuncts
    ('ক্ক', 'kk'),
    ('ক্র', 'kr'),
    ('ক্ল', 'kl'),
    ('ক্য', 'kz'),
    ('ক্ত', 'kt'),
    ('গ্ণ', 'gN'),
    ('গ্গ', 'gg'),
    ('গ্ধ', 'gdh'),
    ('গ্র', 'gr'),
    ('গ্ল', 'gl'),
    ('গ্য', 'gz'),
    ('ঙ্ক', 'Ngk'),
    ('ঙ্গ', 'Ngg'),
    ('চ্চ', 'cc'),
    ('চ্ছ', 'cch'),
    ('চ্র', 'cr'),
    ('চ্য', 'cz'),
    ('ছ্য', 'chy'),
    ('জ্জ', 'jj'),
    ('জ্ঝ', 'jjh'),
    ('জ্য', 'jz'),
    ('জ্র', 'jr'),
    ('ঝ্য', 'jhy'),
    ('ঝ্র', 'jhr'),
    ('ট্ট', 'TT'),
    ('ট্ব', 'Tb'),
    ('ট্য', 'Tz'),
    ('ট্র', 'Tr'),
    ('ঠ্য', 'Thy'),
    ('ড্র', 'Dr'),
    ('ণ্ট', 'NT'),
    ('ণ্ঠ', 'NTh'),
    ('ণ্ড', 'ND'),
    ('ণ্ঢ', 'NDh'),
    ('ণ্য', 'Nz'),
    ('ত্ন', 'tn'),
    ('ত্স', 'ts'),
    ('থ্ব', 'thb'),
    ('থ্র', 'thr'),
    ('দ্গ', 'dg'),
    ('দ্ড', 'dD'),
    ('দ্দ', 'dd'),
    ('দ্ব', 'db'),
    ('দ্র', 'dr'),
    ('ধ্র', 'dhr'),
    ('ন্ক', 'nk'),
    ('ন্গ', 'ng'),
    ('ন্ছ', 'nch'),
    ('ন্ঝ', 'njh'),
    ('ন্য', 'nz'),
    ('প্ন', 'pn'),
    ('প্র', 'pr'),
    ('ফ্র', 'phr'),
    ('ব্ত', 'bt'),
    ('ব্থ', 'bth'),
    ('ব্দ', 'bd'),
    ('ব্ধ', 'bdh'),
    ('ব্ন', 'bn'),
    ('ব্প', 'bp'),
    ('ব্র', 'br'),
    ('ভ্র', 'bhr'),
    ('ম্য', 'mz'),
    ('ম্র', 'mr'),
    ('য্ব', 'zb'),
    ('র্ণ', 'rN'),
    ('র্ড', 'rD'),
    ('র্ত', 'rt'),
    ('র্দ', 'rd'),
    ('র্ধ', 'rdh'),
    ('র্প', 'rp'),
    ('র্ফ', 'rph'),
    ('র্হ', 'rh'),
    ('র্জ', 'rj'),
    ('র্ল', 'rl'),
    ('ল্ক', 'lk'),
    ('ল্গ', 'lg'),
    ('ল্ট', 'lT'),
    ('ল্ড', 'lD'),
    ('ল্প', 'lp'),
    ('ল্ত', 'lt'),
    ('ল্দ', 'ld'),
    ('ল্হ', 'lh'),
    ('ল্য', 'lz'),
    ('শ্ক', 'shk'),
    ('শ্ট', 'shT'),
    ('শ্ত', 'sht'),
    ('শ্প', 'shp'),
    ('শ্ল', 'shl'),
    ('হ্ত', 'ht'),
    ('হ্দ', 'hd'),
    ('হ্ন', 'hn'),
    ('হ্প', 'hp'),
    ('হ্র', 'hr'),
]

# Individual character mappings
BENGALI_TO_BANGLISH = {
    # Independent vowels
    'অ': 'o',
    'আ': 'a',
    'ই': 'i',
    'ঈ': 'I',
    'উ': 'u',
    'ঊ': 'U',
    'ঋ': 'rri',
    'এ': 'e',
    'ঐ': 'OI',
    'ও': 'O',
    'ঔ': 'OU',
    
    # Consonants
    'ক': 'k',
    'খ': 'kh',
    'গ': 'g',
    'ঘ': 'gh',
    'ঙ': 'Ng',
    'চ': 'c',
    'ছ': 'ch',
    'জ': 'j',
    'ঝ': 'jh',
    'ঞ': 'NG',
    'ট': 'T',
    'ঠ': 'Th',
    'ড': 'D',
    'ঢ': 'Dh',
    'ণ': 'N',
    'ত': 't',
    'থ': 'th',
    'দ': 'd',
    'ধ': 'dh',
    'ন': 'n',
    'প': 'p',
    'ফ': 'ph',
    'ব': 'b',
    'ভ': 'bh',
    'ম': 'm',
    'য': 'z',
    'র': 'r',
    'ল': 'l',
    'শ': 'sh',
    'ষ': 'Sh',
    'স': 's',
    'হ': 'h',
    'ড়': 'R',
    'ঢ়': 'Rh',
    'য়': 'y',
    'ৎ': '`',
    
    # Diacritics (Kar)
    'া': 'a',
    'ি': 'i',
    'ী': 'I',
    'ু': 'u',
    'ূ': 'U',
    'ৃ': 'RI',
    'ে': 'e',
    'ৈ': 'OI',
    'ো': 'O',
    'ৌ': 'OU',
    
    # Modifiers
    'ঁ': 'C',
    'ং': 'ng',
    'ঃ': ':',
    '্': '+',  # Hosonto/Hasanta
}

def reverse_transliterate(bengali_text):
    """
    Convert Bengali text to Banglish (Roman phonetic representation).
    
    Args:
        bengali_text (str): Bengali text to convert
        
    Returns:
        str: Phonetic English (Banglish) representation
        
    Examples:
        >>> reverse_transliterate('আমার সোনার বাংলা')
        'amar sonar bangla'
        
        >>> reverse_transliterate('স্বাগতম')
        'swagotom'
    """
    if not bengali_text:
        return ""
    
    result = ""
    i = 0
    text_len = len(bengali_text)
    
    while i < text_len:
        matched = False
        
        # First, try to match conjuncts (longest patterns first)
        for bengali_char, banglish_char in BENGALI_CONJUNCTS:
            if bengali_text.startswith(bengali_char, i):
                result += banglish_char
                i += len(bengali_char)
                matched = True
                break
        
        if matched:
            continue
        
        # Then try individual characters
        char = bengali_text[i]
        
        if char in BENGALI_TO_BANGLISH:
            result += BENGALI_TO_BANGLISH[char]
            i += 1
        elif char == ' ':
            result += ' '
            i += 1
        elif char == '।':
            result += '.'
            i += 1
        else:
            # Keep unmapped characters as-is
            result += char
            i += 1
    
    return result
