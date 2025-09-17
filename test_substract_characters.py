
import io
import sys
import pytest
import characters
import difflib

def string_similarity(s1, s2):
    # Calculate similarity ratio
    s1 = s1.replace(" ", "").replace("\n", "")
    s2 = s2.replace(" ", "").replace("\n", "")

    similarity_ratio = difflib.SequenceMatcher(None, s1, s2).ratio()
    return similarity_ratio

def subtract_chars(char1, char2):
    # Test the add_chars function
    char1 = 'b'
    char2 = 'a'
    sum = ord(char1) - ord(char2)
    expected_output = "Difference of "+char1+" and "+char2+" = "+str(sum)+ "\nCharacter = " + chr(sum)+"\n"
    
    characters.subtract_chars(char1, char2)
    captured_output = sys.stdout.getvalue()
    
       ##comparison
    similarity_threshold = 0.99  # Set your desired threshold here

    similarity_score = string_similarity(captured_output, expected_output)

    
    success = True
    if similarity_score >= similarity_threshold:
        feedback = "Strings are similar enough (score: {0:.2f}%). Test passed!".format(similarity_score * 100)
       
    else:
       feedback = "Test failed: Strings are not similar enough (score: {0:.2f}%).\n".format(similarity_score * 100)
       feedback = feedback + "Expected:" + expected_output+"\n"
       feedback = feedback + "Captured:" + captured_output+"\n"
       success =False
    print(feedback)
    assert success,feedback