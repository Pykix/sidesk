from datetime import date


def bill_number_generator(project_name: str, buyer_id, seller_id):
    today = date.today()
    usable_date = today.strftime("%d%m%Y")
    return f"{project_name[:3].upper()}{usable_date}{seller_id}{buyer_id}"
