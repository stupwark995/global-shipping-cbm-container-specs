"""Zero-dependency shipping CBM & volumetric weight helper.
Online interactive version: https://www.80616.com/
"""


def calc_shipment(cartons: list[dict]) -> dict:
    """Calculate total CBM, actual kg, express chargeable kg (÷5000), and air chargeable kg (÷6000)."""
    total_cbm = 0.0
    total_actual_kg = 0.0
    total_qty = 0
    for item in cartons:
        qty = int(item.get("qty", 1))
        cbm = (item["l_cm"] * item["w_cm"] * item["h_cm"]) / 1_000_000
        total_cbm += cbm * qty
        total_actual_kg += item["weight_kg"] * qty
        total_qty += qty
    cm3 = total_cbm * 1_000_000
    return {
        "total_qty": total_qty,
        "total_cbm": round(total_cbm, 4),
        "actual_kg": round(total_actual_kg, 2),
        "express_chargeable_kg": round(max(total_actual_kg, cm3 / 5000), 2),
        "air_chargeable_kg": round(max(total_actual_kg, cm3 / 6000), 2),
    }


if __name__ == "__main__":
    sample = [{"l_cm": 50, "w_cm": 40, "h_cm": 30, "weight_kg": 8.5, "qty": 10}]
    print(calc_shipment(sample))
