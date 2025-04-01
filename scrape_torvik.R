# Load libraries
library(dplyr)   # Contains the pipe operator and `slice_max()`
library(magrittr) # Just in case for the pipe

library(cbbdata)
library(readr)

# Get the year from the command line argument
args <- commandArgs(trailingOnly = TRUE)
year <- as.numeric(args[1])

# Import username and password from environment variables
username <- Sys.getenv("CBB_USERNAME")
password <- Sys.getenv("CBB_PASSWORD")

# Check if the environment variables are set
if (username == "" || password == "") {
  stop("Username or password environment variables not set.")
}

# Login
cbbdata::cbd_login(username = username, password = password)

# Validate the year input
if (is.na(year)) {
  stop("Please provide a valid year as an argument.")
}

# Scrape the data
data <- cbd_torvik_player_game(year = year)

# Save the data to CSV
output_file <- paste0("torvik_player_games_", year, ".csv")
write_csv(data, output_file)



data2 <- cbd_torvik_team_factors(year = year, no_bias = TRUE)
output_file2 <- paste0("torvik_team_rankings_", year, ".csv")
write_csv(data2, output_file2)

cat("Data saved to:", output_file, "\n")
cat("Data saved to:", output_file2, "\n")
