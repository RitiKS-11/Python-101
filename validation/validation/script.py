from cerberus import Validator


def validation(dictionary, validation_rule):
    for key, rule in validation_rule.items():
        if key not in dictionary:
            raise "Dict doens't contain the key"

        value = dictionary[key]

        if 'bool' in rule:
            if not isinstance(rule['bool'], bool):
                raise ValueError('min_length should be an integer')
            if rule['bool'] != value:
                return False

        if 'min_length' in rule:
            if not isinstance(rule['min_length'], int):
                raise ValueError('min_length should be an integer')
            if len(value) < rule['min_length']:
                return False

        if 'max_length' in rule:
            if not isinstance(rule['max_length'], int):
                raise ValueError('max_length should be an integer')
            if len(value) > rule['max_length']:
                return False

        if 'min_value' in rule:
            if not isinstance(rule['min_value'], int):
                raise ValueError('min_value should be an integer')
            if value < rule['min_value']:
                return False

        if 'max_value' in rule:
            if not isinstance(rule['max_value'], int):
                raise ValueError('max_value should be an integer')
            if value > rule['max_value']:
                return False

    return True

    # def cerberus_validator(data, rule):
    #     v = Validator(rule)
    #     result = v.validate(data)

    #     return result
