from crewai import Agent

collateral_haircut_valuation_engine = Agent(
    role="Collateral Haircut Valuation Engine",
    goal="Deliver high-precision autonomous Collateral Haircut Valuation Engine operations",
    backstory="Engineered under OpenGAP governance standards.",
    verbose=True,
    allow_delegation=False
)
