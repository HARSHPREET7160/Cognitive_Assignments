from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.utils import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
import numpy as np

corpus = "technology transforms lives. innovation drives technology. smart minds create innovation."

text_tokenizer = Tokenizer()
text_tokenizer.fit_on_texts([corpus])
token_sequence = text_tokenizer.texts_to_sequences([corpus])[0]

sequences = []
for i in range(1, len(token_sequence)):
    sub_sequence = token_sequence[:i+1]
    sequences.append(sub_sequence)

sequence_len = max(len(seq) for seq in sequences)
sequences = pad_sequences(sequences, maxlen=sequence_len)

X_train = sequences[:, :-1]
y_train = sequences[:, -1]

vocab_size = len(text_tokenizer.word_index) + 1

model = Sequential()
model.add(Embedding(vocab_size, 10, input_length=sequence_len - 1))
model.add(LSTM(100))
model.add(Dense(vocab_size, activation='softmax'))
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam')
model.fit(X_train, y_train, epochs=200, verbose=0)

start_text = "technology"
for _ in range(3):
    token_input = text_tokenizer.texts_to_sequences([start_text])[0]
    token_input = pad_sequences([token_input], maxlen=sequence_len - 1)
    prediction = model.predict(token_input, verbose=0)
    predicted_index = np.argmax(prediction)
    for word, idx in text_tokenizer.word_index.items():
        if idx == predicted_index:
            start_text += " " + word
            break

print("Generated Text:", start_text)
