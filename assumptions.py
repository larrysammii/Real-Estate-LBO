from dataclasses import dataclass, field
from typing import Optional
import datetime


# Project parameters
@dataclass
class Info:
    duration: int  # years
    acq_cost: float
    acq_date: datetime.datetime
    area: float  # sqft
    area_ratio: Optional[
        dict
    ] = None  # % of total area, e.g. {"commercial": 0.7, "residential": 0.2, "retail": 0.1}
    plot_ratio: float = 1
    wacc: Optional[float] = None  # Weighted average cost of capital(%)
    exit_cap: float = 0  # Exit cap rate(%)

    @property # project gfa calculation
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


# Types of revenue
@dataclass
class Revenue:
    building: Stats
    rental: Optional[float] = None  # rental income per sqft
    lease_term: Optional[int] = None  # lease term(months)
    sale: Optional[float] = None  # sale price per sqft
    rental_growth: Optional[float] = None  # growth rate of rental and sale
    management_fee: Optional[float] = None  # management fee(%)
    vacancy_rate: Optional[float] = None  # vacancy rate(%) or collection loss rate(%)



# Types of cost
@dataclass
class Cost:
    construction_cost: float  # per sqft
    construction_time: float  # months
    maintainance_cost: float  # % of gross revenue or otherwise indicated
    marketing_cost: float  # % of gross revenue or otherwise indicated
    disposition_cost: float  # % cost when exit


# Deductables: Tax, Depreciation
@dataclass
class Deduction:
    vat: Optional[float] = None  # Value added tax(%) excl. land cost
    deprecation: Optional[float] = None  # Depreciation rate(%)
    income_tax: Optional[float] = None  # Income tax rate(%)


@dataclass
class Loan:
    ltv_ratio: float  # Loan to value ratio(%)
    annual_int_rate: float  # Annual interest rate(%)
    loan_period: int  # Loan period(months)
    amortization_period: int  # Amortization period(months)
    repayment_frequency: str  # Repayment frequency, "monthly" or "quarterly" or "semi-annually" or "annually"
    interest_only: bool  # Bullet loan or not
