Task:
START

DISPLAY ___________________________

INPUT ___________________________

IF ___________________________ THEN
    DISPLAY "Login successful"
ELSE
    DISPLAY ___________________________

END

Answer:
START

SET correct_password TO 1623

DISPLAY "Please enter your 4 digit password"

INPUT (0-9999)

IF INPUT=correct_password THEN
    DISPLAY "Login successful"
ELSE
    DISPLAY "Login unsuccessful"

END