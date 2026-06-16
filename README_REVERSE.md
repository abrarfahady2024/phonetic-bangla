# Reverse Transliteration: Bengali to Banglish

## Overview

The `phonetic-bangla` library now supports **bidirectional transliteration**:
- **Forward**: Banglish (English keyboard) → Bengali
- **Reverse**: Bengali → Banglish (English keyboard representation)

## Quick Start

### Forward Conversion (Banglish → Bengali)

```python
from phoneticbn import bn

banglish = "amar sonar bangla"
bengali = bn(banglish)
print(bengali)  # Output: আমার সোনার বাংলা
```

### Reverse Conversion (Bengali → Banglish)

```python
from phoneticbn import bn_reverse

bengali = "আমার সোনার বাংলা"
banglish = bn_reverse(bengali)
print(banglish)  # Output: amar sonar bangla
```

## Command-Line Usage

### Forward Conversion

```bash
$ phonetic-bangla "amar sonar bangla"
আমার সোনার বাংলা
```

### Reverse Conversion

```bash
$ phonetic-bangla --reverse "আমার সোনার বাংলা"
amar sonar bangla
```

Or using the short flag:

```bash
$ phonetic-bangla -r "আমার সোনার বাংলা"
amar sonar bangla
```

## API Reference

### `bn_reverse(bengali_text: str) -> str`

Convert Bengali text to Banglish (Roman phonetic representation).

**Parameters:**
- `bengali_text` (str): The Bengali text to convert

**Returns:**
- str: The phonetic English representation

**Example:**
```python
from phoneticbn import bn_reverse

result = bn_reverse("স্বাগতম")
print(result)  # Output: swagotom
```

### Aliases

You can use either of these aliases:

```python
from phoneticbn import bn_reverse, reverse

# Both are equivalent
result1 = bn_reverse("আমার")
result2 = reverse("আমার")
```

## Supported Features

### Character Support

✅ All independent Bengali vowels (স্বরবর্ণ)
✅ All consonants (ব্যঞ্জনবর্ণ)
✅ Vowel diacritics (কার/নির্দেশক)
✅ Modifiers (চন্দ্রবিন্দু, অনুস্বার, বিসর্গ, হসন্ত)
✅ Complex conjuncts (যুক্তবর্ণ/Juktoborno)
✅ Special characters and punctuation

### Conjunct Mapping

The library handles all common Bengali conjuncts:

```python
bn_reverse("স্বাগতম")  # swagotom
bn_reverse("বিজ্ঞান")  # bijNGan
bn_reverse("লক্ষী")   # lokShI
bn_reverse("করম")    # kormo
```

## Refinements & Improvements

### Comprehensive Conjunct Mapping

The reverse engine includes mappings for 100+ conjunct combinations, organized by priority:
1. **Complex vowel-consonant combinations** (e.g., হৃ → hRi)
2. **Special three-letter conjuncts** (e.g., ক্ষ → kSh, জ্ঞ → jNG)
3. **Common two-letter conjuncts** (e.g., ক্র → kr, স্ট → sT)

### Smart Diacritic Handling

The engine properly handles both:
- **Diacritics after consonants** (e.g., া after ক → কা = ka)
- **Modifiers** (e.g., ং, ঁ, ঃ)

### Special Character Handling

- **Danda** (।) → Period (.)
- **Spaces** → Preserved
- **Unmapped characters** → Passed through as-is

## Round-Trip Conversion

You can convert text both ways:

```python
from phoneticbn import bn, bn_reverse

# Start with Banglish
original = "amar sonar bangla"

# Convert to Bengali
bengali = bn(original)
print(bengali)  # আমার সোনার বাংলা

# Convert back to Banglish
banglish = bn_reverse(bengali)
print(banglish)  # amar sonar bangla
```

## Examples

### Example 1: Simple Words

```python
from phoneticbn import bn_reverse

words = {
    'দিন': 'day',
    'রাত': 'night',
    'আজ': 'today',
    'ভালো': 'good',
    'খারাপ': 'bad',
}

for bengali, english in words.items():
    banglish = bn_reverse(bengali)
    print(f"{bengali} ({english}): {banglish}")
```

### Example 2: Sentences

```python
from phoneticbn import bn_reverse

sentences = [
    "আমি বাংলা ভাষা ভালোবাসি।",  # I love Bengali language
    "আপনার নাম কী?",                # What is your name?
    "আপনি কেমন আছেন?",             # How are you?
]

for bengali in sentences:
    banglish = bn_reverse(bengali)
    print(f"Bengali: {bengali}")
    print(f"Banglish: {banglish}")
    print()
```

## Testing

The reverse transliteration engine includes comprehensive tests:

```bash
# Run all reverse transliteration tests
pytest tests/test_reverse_comprehensive.py -v

# Run specific test class
pytest tests/test_reverse_comprehensive.py::TestBasicReverseConversion -v

# Run with coverage
pytest tests/test_reverse_comprehensive.py --cov=phoneticbn.reverse_engine
```

## Limitations & Future Improvements

1. **Ambiguity Resolution**: Some Bengali text can have multiple valid Banglish representations (e.g., অ can be 'o' or silent)
2. **Context-Aware Conversion**: Future versions may use context to improve accuracy
3. **Specialized Dictionaries**: Integration with dictionaries for proper nouns and domain-specific terms
4. **Machine Learning Models**: Optional ML-based disambiguation for maximum accuracy

## Contributing

Found an issue with the reverse transliteration? Please report it on [GitHub Issues](https://github.com/abrarfahady2024/phonetic-bangla/issues) with:
- The Bengali text that caused the issue
- The output you got
- The output you expected

## License

MIT License - See LICENSE file for details
