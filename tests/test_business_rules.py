"""Tests for the Copper Kettle business rules."""

from business_rules import (
    calculate_bean_cost,
    calculate_shipment_total,
    format_shipment_line,
    get_bulk_discount,
    largest_shipment,
    needs_pallet,
    requires_prepayment,
    total_shipped,
)


def test_bean_cost_multiples_price_by_bags() -> None:
    """Bean cost is price per bag times bags."""
    assert round(calculate_bean_cost(12.50, 10), 2) == 125.00


def test_no_discount_at_19_bags() -> None:
    """19 bags is below the first tier and gets no discount."""
    assert get_bulk_discount(19) == 0.0


def test_standard_discount_at_20_bags() -> None:
    """20 bags is the start of the 9% tier."""
    assert get_bulk_discount(20) == 0.09


def test_standard_discount_at_79_bags() -> None:
    """79 bags is the top of the 9% tier."""
    assert get_bulk_discount(79) == 0.09


def test_large_discount_at_80_bags() -> None:
    """80 bags is the start of the 14% tier."""
    assert get_bulk_discount(80) == 0.14


def test_partner_gets_no_bonus_under_20_bags() -> None:
    """Partner gets no extra discount below 20 bags."""
    assert get_bulk_discount(19, partner=True) == 0.0


def test_partner_bonus_at_20_bags() -> None:
    """Partner gets 13% at 20 bags."""
    assert get_bulk_discount(20, partner=True) == 0.13


def test_partner_bonus_at_80_bags() -> None:
    """Partner gets 18% at 80 bags."""
    assert get_bulk_discount(80, partner=True) == 0.18


def test_partner_changes_shipment_total() -> None:
    """Partner status lowers the total on a 40-bag shipment."""
    assert round(calculate_shipment_total(10.00, 40), 2) == 364.00
    assert round(calculate_shipment_total(10.00, 40, partner=True), 2) == 348.00


def test_no_shipping_fee_at_250() -> None:
    """A discounted cost of exactly $250 has no shipping fee."""
    assert round(calculate_shipment_total(25.00, 10), 2) == 250.00


def test_shipping_fee_added_below_250() -> None:
    """A discounted cost of $249.99 gets the $35 fee."""
    assert round(calculate_shipment_total(249.99, 1), 2) == 284.99


def test_prepayment_required_at_1500() -> None:
    """A total of exactly $1500 requires prepayment."""
    assert requires_prepayment(1500.00) is True


def test_no_prepayment_at_1499_99() -> None:
    """A total just under $1500 does not require prepayment."""
    assert requires_prepayment(1499.99) is False


def test_pallet_no_pallet_at_60_bags() -> None:
    """60 bags does not need a pallet even with a high total."""
    assert needs_pallet(60, 800.00) is False


def test_pallet_needed_at_61_bags() -> None:
    """61 bags with a high total needs a pallet."""
    assert needs_pallet(61, 800.00) is True


def test_no_pallet_at_700_total() -> None:
    """A total of exactly $700 does not need a pallet even with many bags."""
    assert needs_pallet(100, 700.00) is False


def test_pallet_needed_above_700_total() -> None:
    """A total just over $700 with many bags needs a pallet."""
    assert needs_pallet(100, 700.01) is True


def test_total_shipped_adds_shipment_totals() -> None:
    """Total shipped adds every shipment total in the list."""
    shipments = [
        {"buyer": "Uptown Bakery", "bag_price": 14.00, "bags": 10, "partner": False},
        {"buyer": "Wren Hotel", "bag_price": 13.00, "bags": 40, "partner": False},
    ]
    assert round(total_shipped(shipments), 2) == 648.20


def test_total_shipped_empty_list() -> None:
    """An empty list ships a total of zero."""
    assert round(total_shipped([]), 2) == 0.00


def test_largest_shipment_returns_biggest_buyer() -> None:
    """Largest shipment returns the buyer with the highest total."""
    shipments = [
        {"buyer": "Uptown Bakery", "bag_price": 14.00, "bags": 10, "partner": False},
        {"buyer": "Wren Hotel", "bag_price": 13.00, "bags": 40, "partner": False},
    ]
    assert largest_shipment(shipments) == "Wren Hotel"


def test_largest_shipment_tie_returns_first() -> None:
    """On a tie, the buyer that comes first in the list wins."""
    shipments = [
        {"buyer": "First Cafe", "bag_price": 12.00, "bags": 30, "partner": False},
        {"buyer": "Second Cafe", "bag_price": 12.00, "bags": 30, "partner": False},
    ]
    assert largest_shipment(shipments) == "First Cafe"


def test_largest_shipment_empty_list() -> None:
    """An empty list returns an empty string."""
    assert largest_shipment([]) == ""


def test_format_line_with_no_and_no() -> None:
    """A line shows no for both flags and two decimal places."""
    line = format_shipment_line("Uptown Bakery", 175.00, False, False)
    assert line == "Uptown Bakery: $175.00 | prepayment: no | pallet: no"


def test_format_line_with_yes_and_yes() -> None:
    """A line shows yes for both flags."""
    line = format_shipment_line("Zenith Grocers", 1892.0, True, True)
    assert line == "Zenith Grocers: $1892.00 | prepayment: yes | pallet: yes"
