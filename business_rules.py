"""Business rules for Cooper Kettle Coffee Roasters wholesale shipments"""

MIN_DISCOUNT_BAGS = 20
LARGE_ORDER_BAGS = 80
STANDARD_DISCOUNT = 0.09
LARGE_DISCOUNT = 0.14
PARTNER_BONUS = 0.04
SHIPPING_FEE = 35.00
FREE_SHIPPING_THRESHOLD = 250.00
PREPAYMENT_THRESHOLD = 1500.00
PALLET_BAG_LIMIT = 60
PALLET_TOTAL_LIMIT = 700.00

def calculate_bean_cost(bag_price: float, bags: int) -> float:
    """Return the bean cost before any discount."""
    return bag_price * bags

def get_bulk_discount(bags: int, partner: bool = False) -> float:
    """Return the discount rate as a decimal based on bags and partner status."""
    if bags < MIN_DISCOUNT_BAGS:
        return 0.0
    if bags < LARGE_ORDER_BAGS :
        rate = STANDARD_DISCOUNT
    else: 
        rate = LARGE_DISCOUNT
    if partner:
        rate = rate + PARTNER_BONUS
    return round(rate, 2)

def calculate_shipment_total(bag_price: float, bags: int, partner: bool = False) -> float:
    """Return the shipment total: discounted cost plus shipping when it applies"""
    cost = calculate_bean_cost(bag_price, bags)
    rate = get_bulk_discount(bags, partner)
    discounted_cost = cost * (1 - rate)
    if discounted_cost < FREE_SHIPPING_THRESHOLD:
        discounted_cost = discounted_cost + SHIPPING_FEE
    return round(discounted_cost, 2)

def requires_prepayment(total: float) -> bool:
    """Return True when the shipment total requires prepayment."""
    return total >= PREPAYMENT_THRESHOLD

def needs_pallet(bags: int, total: float) -> bool:
    """Return True when the shipment needs a freight pallet."""
    return bags > PALLET_BAG_LIMIT and total > PALLET_TOTAL_LIMIT

def total_shipped(shipments: list) -> float:
    """Return the sum of the shipment totals for every shipment in the list."""
    running_total = 0.0
    for shipment in shipments:
        shipment_total = calculate_shipment_total(
            shipment["bag_price"], shipment["bags"], shipment["partner"]
        )
        running_total = running_total + shipment_total
    return round(running_total, 2)

def largest_shipment(shipments: list) -> str:
    """Return the buyer of the shipment with the largest total."""
    largest_buyer = ""
    largest_total = None
    for shipment in shipments:
        shipment_total = calculate_shipment_total(
            shipment["bag_price"], shipment["bags"], shipment["partner"]
        )
        if largest_total is None or shipment_total > largest_total:
            largest_total = shipment_total
            largest_buyer = shipment["buyer"]
    return largest_buyer

def format_shipment_line(buyer: str, total: float, prepayment: bool, pallet: bool) -> str:
    """Return one formatted line of the shipment report."""
    prepayment_text = "yes" if prepayment else "no"
    pallet_text = "yes" if pallet else "no"
    return f"{buyer}: ${total:.2f} | prepayment: {prepayment_text} | pallet: {pallet_text}"


