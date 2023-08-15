# Flipper Zero IR Tools
IR Tools for Flipper Zero. Useful for IR contributors

## Description

Written in Python. IR_Signal class that provides IR signal processing functionality + several scripts that use it

## ir_duplicate_checker.py
searches in `<first_dump>` for matching (for type: parsed) or similar (for type: raw) signals from `<second_dump>` 

### Usage

```bash
chmod+x ir_duplicate_checker.py
ir_duplicate_checker.py <first_dump> <second_dump>
```
or
```bash
python3 ir_duplicate_checker.py <first_dump> <second_dump>
```
