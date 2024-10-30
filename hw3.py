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

def population_by_ethnicity(demographics: list[data.CountyDemographics], str) -> float:
    pass

#Part 4

#Part 5