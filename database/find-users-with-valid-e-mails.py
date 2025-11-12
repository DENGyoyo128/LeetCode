import pandas as pd

# def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
#     pattern = r'^[A-Za-z][A-Za-z0-9_.-]*@leetcode\.com$'
#     mask = users['mail'].str.match(pattern, na=False)
#     valid = users[mask]
#     return valid

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    
    is_valid = lambda x: set(x).issubset(valid_chars)
    letters = set(ascii_letters)
    valid_chars = letters | set(digits) | {'_', '.', '-'}

    return users[(users.mail.str[0].isin(letters)) &         # <--1)
                 (users.mail.str[~12:] == '@leetcode.com') & # <--2)
                 (users.mail.str[:~12].apply(is_valid))]     # <--3)

