from dataclasses import dataclass, field
from typing import Optional
import datetime


# Project parameters
@dataclass
class Info:
    duration: int  # years
    acq_cost: float
    acq_date: datetime
    area: float
    exit_cap: float = 0  # Exit cap rate(%)
    plot_ratio: float = 1
    area_ratio: Optional[
        dict
    ] = None  # % of total area, e.g. {"commercial": 0.7, "residential": 0.2, "retail": 0.1}
    wacc: Optional[float] = None  # Weighted average cost of capital(%)

    @property  # project gfa calculation
    def project_gfa(self) -> float:
        return self.area * self.plot_ratio


# Building's basic facts
@dataclass
class Stats:
    building_type: str  # Commercial or Residential or Retail
    area: float  # sqft
    phase: Optional[int] = None  # Number of phases
    number_of_buildings: Optional[int] = None  # Number of buildings
    units: Optional[int] = None  # Number of units


@dataclass
class LeaseTerm:
    building: Stats
    lease_id: int  # eg. lease id 1 or 2 or 3
    rental_price: float  # rental price per sqft
    lease_term: int  # lease term(months)
    rental_growth: float  # growth rate of rental price
    growth_frequency: int  # step-up every x months
    vacancy_rate: Optional[float]  # vacancy rate(%)


@dataclass
class Sale:
    building: Stats
    phase_id: int  # eg. phase id 1 or 2 or 3
    sale_year: int  # year of sale
    sale_price_sqft: float  # sale price per sqft
    sale_growth: Optional[float] = None  # growth rate of sale price
    percentage_sold: Optional[float] = None  # percentage of sqft sold (%)


# Types of revenue
@dataclass
class Revenue:
    building: Stats
    management_fee: Optional[float] = None  # management fee(%)


# Types of cost
@dataclass
class Cost:
    building: Stats
    construction_cost: float  # per sqft
    construction_time: float  # months
    phase_id: Optional[int] = None  # eg. phase id 1 or 2 or 3
    maintainance_cost: Optional[
        float
    ] = None  # % of gross revenue or otherwise indicated
    marketing_cost: Optional[float] = None  # % of gross revenue or otherwise indicated
    disposition_cost: Optional[float] = None  # % cost when exit
    util_expense: Optional[float] = None  # utility expense per sqft


# Deductables: Tax, Depreciation
@dataclass
class Deduction:
    building: Stats
    vat: Optional[float] = None  # Value added tax(%) excl. land cost
    depreciation: Optional[int] = None  # Depreciation years
    income_tax: Optional[float] = None  # Income tax rate(%)
    tax_pay_on: Optional[int] = None  # Tax pay on year


@dataclass
class Loan:
    ltv_ratio: float  # Loan to value ratio(%)
    annual_int_rate: float  # Annual interest rate(%)
    loan_period: int  # Loan period(months)
    repayment_frequency: int  # Repayment frequency, monthly = 1, quarterly = 3, semi-annually = 6, annually = 12
    amortization_period: Optional[int] = None  # Amortization period(months)
    loan_type: Optional[str] = None  # Bullet or Amortized
