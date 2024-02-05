from cerberus import Validator


def validation(dictionary, validation_rule):
    for key, rule in validation_rule.items():
        if key not in dictionary:
            raise "Dict doens't contain the key"

        value = dictionary[key]

        keys_items = ['min_length', 'max_length', 'min_value', 'max_value']

        for item in keys_items:
            if item in rule:
                if not isinstance(rule[item], int):
                    raise ValueError('min_length should be an integer')
                if item.startswith('min') and not isinstance(value, int) and len(value) < rule[item]:
                    return False
                if item.startswith('max') and not isinstance(value, int) and len(value) > rule[item]:
                    return False

        if 'bool' in rule:
            if not isinstance(rule['bool'], bool):
                raise ValueError('bool should be boolean')
            if rule['bool'] != value:
                return False

    return True

    # def cerberus_validator(data, rule):
    #     v = Validator(rule)
    #     result = v.validate(data)

    #     return result
