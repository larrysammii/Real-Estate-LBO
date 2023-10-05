from assumptions import Info, Stats
import datetime

# create project basic info
overview = Info(
    duration=7,  # years
    acq_cost=9500 * 10**6,  # 9,500 million
    acq_date=datetime.date(2020, 1, 1),
    area=0.5 * 10**6,  # 0.5 million sqft
    area_ratio={
        "Commercial": 0.7,
        "Residential": 0.3,
    },
    plot_ratio=7.0,
    wacc=0.06,
    exit_cap=0.06,
)

# calculate project gfa
gfa = overview.project_gfa

# commercial portion setup
commercial = Stats(
    building_type="Commercial",
    area=gfa * overview.area_ratio["Commercial"],
    number_of_buildings=2,
)
