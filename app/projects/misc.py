from datetime import date


def bill_number_generator(project_name: str, seller_id, buyer_id):
    today = date.today()
    usable_date = today.strftime("%d%m%Y")
    return "".join(
        [project_name[:3].upper().strip(), usable_date, seller_id, buyer_id],
    )
