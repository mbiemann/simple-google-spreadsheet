import os
from simple_google_spreadsheet.spreadsheet import SpreadSheet

def test_spreadsheet():
    
    spreadsh = SpreadSheet(
        spreadsheet_id=os.environ['TEST_SPREADSHEET_ID'],
        credentials_filename='./tests/credentials.json',
        token_filename='./tests/token.json'
    )

    # Clear
    spreadsh.clear_values('page1')

    # Set Values
    input_values = [
        {
            'col1': 'val a 1',
            'col2': 'val a 2',
        },
        {
            'col1': 'val b 1',
            'col3': 'val b 3',
        }
    ]
    spreadsh.set_values(input_values, 'page1')

    # Get Values
    values = spreadsh.get_values('page1')
    assert values == [
        {
            'col1': 'val a 1',
            'col2': 'val a 2',
            'col3': None,
        },
        {
            'col1': 'val b 1',
            'col2': None,
            'col3': 'val b 3',
        }
    ]
