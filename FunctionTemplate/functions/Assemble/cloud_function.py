def cloud_function(json_input):
    char_list = json_input["char"]
    
    # Processing
    result = "".join(char_list)

    # return the result
    res = {
        "encodedString": result
    }
    return res