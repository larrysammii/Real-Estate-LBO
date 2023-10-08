import projectinfo as pj
import polars as pl
import numpy_financial as npf
from dateutil.relativedelta import relativedelta
from collections import OrderedDict

# Creating amoritization schedule

# Loan start date
start_date = pj.overview.acq_date

# Loan amount
loan = pj.loan
loan_amount = loan.ltv_ratio * pj.overview.acq_cost

# Payment per period
npmt = 12 / loan.repayment_frequency

# Interest rate per period
int_rate = loan.annual_int_rate / npmt

# Number of periods
term = loan.loan_period


# Amortization schedule function
def amortize(start_date, int_rate, loan_amount, term):
    starting_period = 1

    # Beginning balance per period
    beginning_balance = loan_amount

    # Ending balance proxy
    ending_balance = loan_amount

    # Payment per period
    pmt = -npf.pmt(int_rate, term, beginning_balance)

    while ending_balance > 0:
        # Interest payment per period
        ipmt = beginning_balance * int_rate

        # Principal payment per period
        principle = pmt - ipmt

        # Ending balance per period
        ending_balance = beginning_balance - principle

        yield OrderedDict(
            [
                ("Period", starting_period),
                ("Month", start_date),
                ("Beginning Balance", beginning_balance),
                ("Payment", pmt),
                ("Principal", principle),
                ("Interest", ipmt),
                ("Ending Balance", ending_balance),
            ]
        )

        # Increment period
        starting_period += 1
        start_date += relativedelta(months=1)
        beginning_balance = ending_balance


# Create dataframe
schedule = pl.DataFrame(amortize(start_date, int_rate, loan_amount, term))
print(schedule)
