
# In: src/phoneticbn/__init__.py

from .engine import transliterate
from .reverse_engine import reverse_transliterate

# Create convenient aliases for forward conversion
convert = transliterate
bn = transliterate

# Create convenient aliases for reverse conversion
bn_reverse = reverse_transliterate
reverse = reverse_transliterate

__all__ = ['transliterate', 'convert', 'bn', 'reverse_transliterate', 'bn_reverse', 'reverse']
