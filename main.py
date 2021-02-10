class Shopping:
    def __init__(self, shopping_list, email_list):
        self.shopping_list = shopping_list
        self.email_list = email_list

        if len(shopping_list) == 0 or len(email_list) == 0:
            raise ValueError('Shopping list or email list can not be empty.')

        for item in self.shopping_list:
            if (
                ('name' not in item or not isinstance(item['name'], str)) or
                ('amount' not in item or not isinstance(item['amount'], int)) or
                ('value' not in item or not isinstance(item['value'], int))
            ):
                raise Exception('Invalid item structure.')

    @property
    def total_sum(self):
        return sum([i['amount'] * i['value'] for i in self.shopping_list])

    def divide_equally(self):
        total = self.total_sum
        value = int(total / len(self.email_list)) # discards decimal part
        email_map = {}
        for email in self.email_list:
            email_map[email] = value
        rest =  total% len(self.email_list)
        i = 0
        while rest != 0:
            email_map[self.email_list[i]] += 1
            rest -= 1
            i += 1

        return email_map


if __name__ == '__main__':
    # Simple example
    shopping_list = [
        {'name': 'item01', 'amount': 3, 'value': 10},
        {'name': 'item02', 'amount': 3, 'value': 10},
        {'name': 'item03', 'amount': 4, 'value': 10},
    ]
    email_list = [f'test{i}@email.com' for i in range(3)]

    shopping = Shopping(shopping_list, email_list)
    email_map = shopping.divide_equally()
    total = shopping.total_sum

    print('Total:', total)
    for k, v in email_map.items():
        print(f'{k}: {v}')
