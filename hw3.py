import data
import hw3_tests
import build_data

#Part 1

def population_total(demographics: list[data.CountyDemographics]) -> int: #returns combined 2014 population from counties in provided list
    return sum([county.population['2014 Population'] for county in demographics])

#Part 2

def filter_by_state(demographics: list[data.CountyDemographics], state_abbreviation: str) -> list[data.CountyDemographics]: #returns all demographics for a given state from a given list of demographics
    return [demographic for demographic in demographics if demographic.state == state_abbreviation]

#Part 3

def population_by_education(demographics: list[data.CountyDemographics], education_level: str) -> float: #returns the 2014 sub-population of people with a given education level from a given list of demographics
    if education_level not in ["Bachelor's Degree or Higher", "High School or Higher"]:
        return 0
    return sum([demographic.education[education_level]/100 * demographic.population["2014 Population"] for demographic in demographics])

def population_by_ethnicity(demographics: list[data.CountyDemographics], ethnicity: str) -> float:
    return sum(0 if ethnicity not in demographic.ethnicities else demographic.ethnicities[ethnicity]/100 * demographic.population["2014 Population"] for demographic in demographics)

def population_below_poverty_level(demographics: list[data.CountyDemographics]) -> float: #returns the 2014 sub-population of people below the poverty level across the given counties
    return sum(0 if "Persons Below Poverty Level" not in demographic.income else (demographic.income["Persons Below Poverty Level"]/100) * demographic.population["2014 Population"] for demographic in demographics)

#Part 4

def percent_by_education(demographics: list[data.CountyDemographics], education_level: str) -> float: #returns the percent of the 2014 population of a given education level
    return population_by_education(demographics, education_level) / population_total(demographics)

def percent_by_ethnicity(demographics: list[data.CountyDemographics], ethnicity: str) -> float: #returns percent of 2014 pop that's a given ethnicity across given counties
    return population_by_ethnicity(demographics, ethnicity) / population_total(demographics)

def percent_below_poverty_level(demographics: list[data.CountyDemographics]): #returns percent of 2014 pop below poverty level across given counties
    return population_below_poverty_level(demographics) / population_total(demographics)

#Part 5