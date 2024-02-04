

def validation(dictionary, validation_rule):
    for key, rule in validation_rule.items():
        if key not in dictionary:
            raise "Dict doens't contain the key"
        
        value = dictionary[key]

        if 'bool' in rule and rule['bool'] != value:
            return False

        if 'min_length' in rule and 'max_length' in rule:
            if len(value) < rule['min_length'] or len(value) > rule['max_length']:
                return False
            
        if 'min_value' in rule and 'max_value' in rule:
            if value < rule['min_value'] or value > rule['max_value']:
                return False
            
    return True

