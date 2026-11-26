# Global Shipping Volumetric Weight, CBM & Container Specs

Open reference dataset and calculation formulas for international logistics, express couriers (DHL, FedEx, UPS), IATA air freight, and sea freight container loading (20GP / 40GP / 40HQ).

**Live Online Multi-Box Calculator:** [https://www.80616.com/](https://www.80616.com/)

## Key Tools Included Online
- [Multi-Box Volumetric Weight & CBM Calculator](https://www.80616.com/)
- [DHL Volumetric Weight Calculator (÷5000 / ÷139)](https://www.80616.com/dhl-volumetric-weight-calculator/)
- [FedEx Dimensional Weight Calculator](https://www.80616.com/fedex-dimensional-weight-calculator/)
- [Air Freight Chargeable Weight Calculator (IATA ÷6000)](https://www.80616.com/air-freight-chargeable-weight-calculator/)
- [40ft High Cube (40HQ) Container Load Calculator](https://www.80616.com/40hq-container-load-calculator/)

## Standard Volumetric Divisors

| Mode | Metric (cm / kg) | Imperial (inch / lbs) | 1 CBM Equivalent |
| :--- | :--- | :--- | :--- |
| Express Courier (DHL / FedEx / UPS / TNT) | `L × W × H ÷ 5000` | `L × W × H ÷ 139` | 200 kg |
| IATA Air Freight | `L × W × H ÷ 6000` | `L × W × H ÷ 166` | 166.67 kg |
| Sea Freight LCL | `1 CBM` | `35.315 cu ft` | 1,000 kg (W/M) |

## Files in This Repository
- `containers.json`: Internal dimensions, door openings, theoretical CBM, practical CBM, and max payload for 20GP, 40GP, 40HQ, and 45HQ containers.
- `shipping_calc.py`: Zero-dependency Python helper to compute CBM, chargeable weight, and container utilization.
