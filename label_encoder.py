#!/usr/bin/env python3
"""Label encoding"""

import numpy as np
from sklearn import preprocessing

#Sample input labels
INPUT_LABELS = ['red', 'black', 'red', 'green', 'black', 'yellow', 'white']

# Create label ENCODER and fit the labels
ENCODER = preprocessing.LabelEncoder()
ENCODER.fit(INPUT_LABELS)

# Print the mapping
print("\nLabel mapping:")
for i, item in enumerate(ENCODER.classes_):
    print(item, '-->', i)

# Encode a set of labels using the ENCODER
TEST_LABELS = ['green', 'red', 'black']
ENCODED_VALUES = ENCODER.transform(TEST_LABELS)
print("\nLabels =", TEST_LABELS)
print("Encoded values =", list(ENCODED_VALUES))

# Decode a set of values using the ENCODER
ENCODED_VALUES = [3, 0, 4, 1]
DECODED_LIST = ENCODER.inverse_transform(ENCODED_VALUES)
print("\nEncoded values = ", ENCODED_VALUES)
print("Decoded values =", list(DECODED_LIST))
