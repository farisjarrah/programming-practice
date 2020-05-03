a = {"key1": {"subkey1": "subvalue1", "subkey2": "subvalue2"}, "key2": {"subkey3": "subvalue3", "subkey4": "subvalue4"}, "key3": {"key3-subkey1": "key3-subvalue1", "key3-subvalue2": {"key3-subsubkey1": "key3-subsubvalue1"}}}
print(a["key3"]["key3-subvalue2"]["key3-subsubkey1"])

# This should return the deepest sub-sub-value
# key3-subsubvalue1
