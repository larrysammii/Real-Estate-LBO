from assumptions import (
    Info,
    Stats,
    LeaseTerm,
    Revenue,
    Cost,
    Sale,
    Deduction,
    Loan,
)
import datetime

# create project basic info
overview = Info(
    duration=7,  # years
    acq_cost=9500 * 10**6,  # 9,500 million
    acq_date=datetime.date(2023, 3, 15),
    area=0.5 * 10**6,  # 0.5 million sqft
    area_ratio={
        "Commercial": 0.7,
        "Residential": 0.3,
    },
    plot_ratio=7.0,
    wacc=0.06,
    exit_cap=0.06,
)

# loan setup, links to amortization.py
loan = Loan(
    ltv_ratio=0.5,  # 50% loan to value ratio
    annual_int_rate=0.07,  # 7% interest rate
    loan_period=30 * 12,  # 30 years loan
    amortization_period=30 * 12,  # 30 years amortization
    repayment_frequency=1,
)

# calculate project gfa
gfa = overview.project_gfa

# commercial portion setup Revenue, Cost, Deduction, Loan
commercial = Stats(
    building_type="Commercial",
    area=gfa * overview.area_ratio["Commercial"],
    number_of_buildings=2,
)

comm_lease1 = LeaseTerm(
    building=commercial,
    lease_id=1,
    rental_price=32.0,
    lease_term=36,  # 3 years lease
    rental_growth=0.03,
    growth_frequency=12,  # step-up annually
    vacancy_rate=0.15,  # 15% vacancy rate first year
)

comm_rev = Revenue(
    building=commercial,
    management_fee=6,  # $6 per sqft
)

comm_cost = Cost(
    building=commercial,
    construction_cost=8000.0,  # $8,000 per sqft
    construction_time=36,  # 3 years construction
    maintainance_cost=0.1,  # 10% of gross revenue
    marketing_cost=0.005,  # 0.5% of gross revenue
    util_expense=2 * 10 * 6,  # $2 million annually
)

comm_deduct = Deduction(
    building=commercial,
    vat=0.08,  # 8% VAT
    depreciation=25 * 12,  # 25 years depreciation
    income_tax=0.33,  # 33% tax on income before tax
    tax_pay_on=5,  # tax pay on May each year
)


# commercial portion setup Revenue, Cost, Deduction, Loan
residential = Stats(
    building_type="Residential",
    area=gfa * overview.area_ratio["Residential"],
    phase=2,
    number_of_buildings=4,
)

resi_ph1_sale_y2 = Sale(
    building=residential,
    phase_id=1,
    sale_year=2,
    sale_price_sqft=20000.0,
    percentage_sold=0.5,
)

resi_ph1_sale_y3 = Sale(
    building=residential,
    phase_id=1,
    sale_year=3,
    sale_price_sqft=20000.0,
    percentage_sold=0.5,
)

resi_ph2_sale_y3 = Sale(
    building=residential,
    phase_id=2,
    sale_year=3,
    sale_price_sqft=20000.0,
    percentage_sold=0.5,
)

resi_ph2_sale_y5 = Sale(
    building=residential,
    phase_id=2,
    sale_year=5,
    sale_price_sqft=20000.0,
    percentage_sold=0.5,
)

resi_ph1_cost = Cost(
    building=residential,
    phase_id=1,
    construction_cost=7000.0,  # $7,000 per sqft
    construction_time=36,  # 3 years construction
    marketing_cost=0.05,  # 5% of gross revenue
    disposition_cost=0.01,  # 1% cost on sale
)

resi_ph2_cost = Cost(
    building=residential,
    phase_id=2,
    construction_cost=7000.0,  # $7,000 per sqft
    construction_time=36,  # 3 years construction
    marketing_cost=0.05,  # 5% of gross revenue
    disposition_cost=0.01,  # 1% cost on sale
)


resi_deduct = Deduction(
    building=residential,
    vat=0.08,  # 8% VAT
    depreciation=25 * 12,  # 25 years depreciation
    income_tax=0.33,  # 33% tax on income before tax
    tax_pay_on=5,  # tax pay on May each year
)
