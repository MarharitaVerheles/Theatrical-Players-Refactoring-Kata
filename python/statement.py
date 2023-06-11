import math


def statement(invoice, plays):
    result = f'Statement for {invoice["customer"]}\n'

    def format_as_dollars(amount):
        return f"${amount:0,.2f}"

    def calculate_amount(play, audience):
        if play['type'] == "tragedy":
            amount = 40000
            if audience > 30:
                amount += 1000 * (audience - 30)
        elif play['type'] == "comedy":
            amount = 30000
            if audience > 20:
                amount += 10000 + 500 * (audience - 20)
            amount += 300 * audience
        else:
            raise ValueError(f'unknown type: {play["type"]}')

        return amount

    def calculate_volume_credits(play, audience):
        volume_credits = max(audience - 30, 0)
        if play["type"] == "comedy":
            volume_credits += math.floor(audience / 5)
        return volume_credits

    total_amount = 0
    volume_credits = 0

    for perf in invoice['performances']:
        play = plays[perf['playID']]
        this_amount = calculate_amount(play, perf['audience'])
        volume_credits += calculate_volume_credits(play, perf['audience'])

        result += f' {play["name"]}: {format_as_dollars(this_amount / 100)} ({perf["audience"]} seats)\n'
        total_amount += this_amount

    result += f'Amount owed is {format_as_dollars(total_amount / 100)}\n'
    result += f'You earned {volume_credits} credits\n'
    return result  
