# -*- coding: utf-8 -*-
"""
Command-line interface for phonetic-bangla transliterator
"""

import argparse
from .engine import transliterate
from .reverse_engine import reverse_transliterate

def main():
    parser = argparse.ArgumentParser(
        description='Phonetic Bengali Transliterator - Convert between Banglish and Bengali',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Forward: Banglish to Bengali
  phonetic-bangla "amar sonar bangla"
  # Output: আমার সোনার বাংলা
  
  # Reverse: Bengali to Banglish
  phonetic-bangla --reverse "আমার সোনার বাংলা"
  # Output: amar sonar bangla
        """
    )
    parser.add_argument(
        'text',
        help='Text to transliterate'
    )
    parser.add_argument(
        '--reverse',
        '-r',
        action='store_true',
        help='Convert from Bengali to Banglish (reverse transliteration)'
    )
    
    args = parser.parse_args()
    
    if args.reverse:
        result = reverse_transliterate(args.text)
    else:
        result = transliterate(args.text)
    
    print(result)

if __name__ == '__main__':
    main()
