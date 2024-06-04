# test_ds_message_protocol.py

# NAME: Nathan Lyum
# EMAIL: nlyum@uci.edu
# STUDENT ID: 63833693

import ds_protocol

def main():
    json_str_1 = '{"key1":"val1", "key2":"val2"}'
    json_dict_1 = ds_protocol.json_to_dict(json_str_1)
    assert json_dict_1
    assert type(json_dict_1) is dict
    assert json_dict_1['key1'] == 'val1'
    assert json_dict_1['key2'] == 'val2'
    assert len(json_dict_1) == 2

    json_str_2 = '{}'
    json_dict_2 = ds_protocol.json_to_dict(json_str_2)
    assert not json_dict_2
    assert type(json_dict_2) is dict
    assert len(json_dict_2) == 0

    json_str_3 = '{"key1":1, "key2":["abc", "def", "ghi"]}'
    json_dict_3 = ds_protocol.json_to_dict(json_str_3)
    assert json_str_3
    assert type(json_dict_3) is dict
    assert len(json_dict_3) == 2
    assert type(json_dict_3['key1']) is int
    assert type(json_dict_3['key2']) is list
    assert len(json_dict_3['key2']) == 3
    

if __name__ == "__main__":
    main()